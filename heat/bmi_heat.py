#! /usr/bin/env python
"""Basic Model Interface implementation for the 2D heat model."""

import types

import numpy as np

from bmi import Bmi

from .heat import Heat


class BmiHeat(Bmi):

    """Solve the heat equation for a 2D plate."""

    _name = "The 2D Heat Equation"
    _input_var_names = ("plate_surface__temperature",)
    _output_var_names = ("plate_surface__temperature",)

    def __init__(self):
        """Create a BmiHeat model that is ready for initialization."""
        self._model = None
        self._values = {}
        self._var_units = {}
        self._grids = {}
        self._grid_type = {}

    def initialize(self, filename=None):
        """Initialize the Heat model.

        Parameters
        ----------
        filename : str, optional
            Path to name of input file.
        """
        if filename is None:
            self._model = Heat()
        elif isinstance(filename, str):
            with open(filename, "r") as file_obj:
                self._model = Heat.from_file_like(file_obj.read())
        else:
            self._model = Heat.from_file_like(filename)

        self._values = {"plate_surface__temperature": self._model.temperature}
        self._var_units = {"plate_surface__temperature": "K"}
        self._grids = {0: ["plate_surface__temperature"]}
        self._grid_type = {0: "uniform_rectilinear_grid"}

    def update(self):
        """Advance model by one time step."""
        self._model.advance_in_time()

    def update_frac(self, time_frac):
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

    def update_until(self, then):
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

    def finalize(self):
        """Finalize model."""
        self._model = None

    def get_var_type(self, var_name):
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
        return str(self.get_value_ref(var_name).dtype)

    def get_var_units(self, var_name):
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

    def get_var_nbytes(self, var_name):
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
        return self.get_value_ref(var_name).nbytes

    def get_var_grid(self, var_name):
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

    def get_grid_rank(self, grid_id):
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
        return len(self.get_grid_shape(grid_id))

    def get_grid_size(self, grid_id):
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
        return np.prod(self.get_grid_shape(grid_id))

    def get_value_ref(self, var_name):
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

    def get_value(self, var_name):
        """Copy of values.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.

        Returns
        -------
        array_like
            Copy of values.
        """
        return self.get_value_ref(var_name).copy()

    def get_value_at_indices(self, var_name, indices):
        """Get values at particular indices.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.
        indices : array_like
            Array of indices.

        Returns
        -------
        array_like
            Values at indices.
        """
        return self.get_value_ref(var_name).take(indices)

    def set_value(self, var_name, src):
        """Set model values.

        Parameters
        ----------
        var_name : str
            Name of variable as CSDMS Standard Name.
        src : array_like
            Array of new values.
        """
        val = self.get_value_ref(var_name)
        val[:] = src

    def set_value_at_indices(self, var_name, src, indices):
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
        val = self.get_value_ref(var_name)
        val.flat[indices] = src

    def get_component_name(self):
        """Name of the component."""
        return self._name

    def get_input_var_names(self):
        """Get names of input variables."""
        return self._input_var_names

    def get_output_var_names(self):
        """Get names of output variables."""
        return self._output_var_names

    def get_grid_shape(self, grid_id):
        """Number of rows and columns of uniform rectilinear grid."""
        var_name = self._grids[grid_id][0]
        return self.get_value_ref(var_name).shape

    def get_grid_spacing(self, grid_id):
        """Spacing of rows and columns of uniform rectilinear grid."""
        return self._model.spacing

    def get_grid_origin(self, grid_id):
        """Origin of uniform rectilinear grid."""
        return self._model.origin

    def get_grid_type(self, grid_id):
        """Type of grid."""
        return self._grid_type[grid_id]

    def get_start_time(self):
        """Start time of model."""
        return 0.0

    def get_end_time(self):
        """End time of model."""
        return np.finfo("d").max

    def get_current_time(self):
        """Current time of model."""
        return self._model.time

    def get_time_step(self):
        """Time step of model."""
        return self._model.time_step
