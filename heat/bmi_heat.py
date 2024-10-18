#! /usr/bin/env python
"""Basic Model Interface implementation for the 2D heat model."""

from typing import Any

import numpy as np
from bmipy import Bmi
from numpy.typing import NDArray

from .heat import Heat


class BmiHeat(Bmi):
    """Solve the heat equation for a 2D plate."""

    _name = "The 2D Heat Equation"
    _input_var_names = ("plate_surface__temperature",)
    _output_var_names = ("plate_surface__temperature",)

    def __init__(self) -> None:
        """Create a BmiHeat model that is ready for initialization."""
        # self._model: Heat | None = None
        self._model: Heat
        self._values: dict[str, NDArray[Any]] = {}
        self._var_units: dict[str, str] = {}
        self._var_loc: dict[str, str] = {}
        self._grids: dict[int, list[str]] = {}
        self._grid_type: dict[int, str] = {}

        self._start_time = 0.0
        self._end_time = float(np.finfo("d").max)
        self._time_units = "s"

    def initialize(self, filename: str | None = None) -> None:
        """Initialize the Heat model.

        Parameters
        ----------
        filename : str, optional
            Path to name of input file.
        """
        if filename is None:
            self._model = Heat()
        elif isinstance(filename, str):
            with open(filename) as file_obj:
                self._model = Heat.from_file_like(file_obj)
        else:
            self._model = Heat.from_file_like(filename)

        self._values = {"plate_surface__temperature": self._model.temperature}
        self._var_units = {"plate_surface__temperature": "K"}
        self._var_loc = {"plate_surface__temperature": "node"}
        self._grids = {0: ["plate_surface__temperature"]}
        self._grid_type = {0: "uniform_rectilinear"}

    def update(self) -> None:
        """Advance model by one time step."""
        self._model.advance_in_time()

    def update_frac(self, time_frac: float) -> None:
        """Update model by a fraction of a time step.

        Parameters
        ----------
        time_frac : float
            Fraction fo a time step.
        """
        time_step = self.get_time_step()
        self._model.time_step = time_frac * time_step
        self.update()
        self._model.time_step = time_step

    def update_until(self, then: float) -> None:
        """Update model until a particular time.

        Parameters
        ----------
        then : float
            Time to run model until.
        """
        n_steps = (then - self.get_current_time()) / self.get_time_step()

        for _ in range(int(n_steps)):
            self.update()
        self.update_frac(n_steps - int(n_steps))

    def finalize(self) -> None:
        """Finalize model."""
        del self._model
        # self._model = None

    def get_var_type(self, var_name: str) -> str:
        """Data type of variable.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.

        Returns
        -------
        str
            Data type.
        """
        return str(self.get_value_ptr(var_name).dtype)

    def get_var_units(self, var_name: str) -> str:
        """Get units of variable.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.

        Returns
        -------
        str
            Variable units.
        """
        return self._var_units[var_name]

    def get_var_nbytes(self, var_name: str) -> int:
        """Get units of variable.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.

        Returns
        -------
        int
            Size of data array in bytes.
        """
        return self.get_value_ptr(var_name).nbytes

    def get_var_itemsize(self, name: str) -> int:
        return np.dtype(self.get_var_type(name)).itemsize

    def get_var_location(self, name: str) -> str:
        return self._var_loc[name]

    def get_var_grid(self, var_name: str) -> int | None:
        """Grid id for a variable.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.

        Returns
        -------
        int
            Grid id.
        """
        for grid_id, var_name_list in self._grids.items():
            if var_name in var_name_list:
                return grid_id
        return None

    def get_grid_rank(self, grid_id: int) -> int:
        """Rank of grid.

        Parameters
        ----------
        grid_id : int
            Identifier of a grid.

        Returns
        -------
        int
            Rank of grid.
        """
        return len(self._model.shape)

    def get_grid_size(self, grid_id: int) -> int:
        """Size of grid.

        Parameters
        ----------
        grid_id : int
            Identifier of a grid.

        Returns
        -------
        int
            Size of grid.
        """
        return int(np.prod(self._model.shape))

    def get_value_ptr(self, var_name: str) -> NDArray[Any]:
        """Reference to values.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.

        Returns
        -------
        array_like
            Value array.
        """
        return self._values[var_name]

    def get_value(self, var_name: str, dest: NDArray[Any]) -> NDArray[Any]:
        """Copy of values.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.
        dest : ndarray
            A numpy array into which to place the values.

        Returns
        -------
        array_like
            Copy of values.
        """
        dest[:] = self.get_value_ptr(var_name).flatten()
        return dest

    def get_value_at_indices(
        self, var_name: str, dest: NDArray[Any], indices: NDArray[np.int_]
    ) -> NDArray[Any]:
        """Get values at particular indices.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.
        dest : ndarray
            A numpy array into which to place the values.
        indices : array_like
            Array of indices.

        Returns
        -------
        array_like
            Values at indices.
        """
        dest[:] = self.get_value_ptr(var_name).take(indices)
        return dest

    def set_value(self, var_name: str, src: NDArray[Any]) -> None:
        """Set model values.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.
        src : array_like
            Array of new values.
        """
        val = self.get_value_ptr(var_name)
        val[:] = src.reshape(val.shape)

    def set_value_at_indices(
        self, name: str, inds: NDArray[np.int_], src: NDArray[Any]
    ) -> None:
        """Set model values at particular indices.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.
        src : array_like
            Array of new values.
        indices : array_like
            Array of indices.
        """
        val = self.get_value_ptr(name)
        val.flat[inds] = src

    def get_component_name(self) -> str:
        """Name of the component."""
        return self._name

    def get_input_item_count(self) -> int:
        """Get names of input variables."""
        return len(self._input_var_names)

    def get_output_item_count(self) -> int:
        """Get names of output variables."""
        return len(self._output_var_names)

    def get_input_var_names(self) -> tuple[str, ...]:
        """Get names of input variables."""
        return self._input_var_names

    def get_output_var_names(self) -> tuple[str, ...]:
        """Get names of output variables."""
        return self._output_var_names

    def get_grid_shape(self, grid_id: int, shape: NDArray[np.int_]) -> NDArray[np.int_]:
        """Number of rows and columns of uniform rectilinear grid."""
        var_name = self._grids[grid_id][0]
        shape[:] = self.get_value_ptr(var_name).shape
        return shape

    def get_grid_spacing(
        self, grid_id: int, spacing: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        """Spacing of rows and columns of uniform rectilinear grid."""
        spacing[:] = self._model.spacing
        return spacing

    def get_grid_origin(
        self, grid_id: int, origin: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        """Origin of uniform rectilinear grid."""
        origin[:] = self._model.origin
        return origin

    def get_grid_type(self, grid_id: int) -> str:
        """Type of grid."""
        return self._grid_type[grid_id]

    def get_start_time(self) -> float:
        """Start time of model."""
        return self._start_time

    def get_end_time(self) -> float:
        """End time of model."""
        return self._end_time

    def get_current_time(self) -> float:
        return self._model.time

    def get_time_step(self) -> float:
        return self._model.time_step

    def get_time_units(self) -> str:
        return self._time_units

    def get_grid_edge_count(self, grid: int) -> int:
        raise NotImplementedError("get_grid_edge_count")

    def get_grid_edge_nodes(self, grid: int, edge_nodes: NDArray[np.int_]) -> None:
        raise NotImplementedError("get_grid_edge_nodes")

    def get_grid_face_count(self, grid: int) -> None:
        raise NotImplementedError("get_grid_face_count")

    def get_grid_face_nodes(self, grid: int, face_nodes: NDArray[np.int_]) -> None:
        raise NotImplementedError("get_grid_face_nodes")

    def get_grid_node_count(self, grid: int) -> int:
        """Number of grid nodes.

        Parameters
        ----------
        grid : int
            Identifier of a grid.

        Returns
        -------
        int
            Size of grid.
        """
        return self.get_grid_size(grid)

    def get_grid_nodes_per_face(
        self, grid: int, nodes_per_face: NDArray[np.int_]
    ) -> None:
        raise NotImplementedError("get_grid_nodes_per_face")

    def get_grid_face_edges(self, grid: int, face_edges: NDArray[np.int_]) -> None:
        raise NotImplementedError("get_grid_face_edges")

    def get_grid_x(self, grid: int, x: NDArray[np.float64]) -> None:
        raise NotImplementedError("get_grid_x")

    def get_grid_y(self, grid: int, y: NDArray[np.float64]) -> None:
        raise NotImplementedError("get_grid_y")

    def get_grid_z(self, grid: int, z: NDArray[np.float64]) -> None:
        raise NotImplementedError("get_grid_z")
