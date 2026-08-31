"""The 2D heat model."""

from __future__ import annotations

from io import TextIOBase

import numpy as np
import yaml
from numpy.typing import NDArray
from scipy import ndimage


def solve_2d(
    temp: NDArray[np.float64],
    spacing: tuple[float, ...],
    out: NDArray[np.float64] | None = None,
    alpha: float = 1.0,
    time_step: float = 1.0,
) -> NDArray[np.float64]:
    """Solve the 2D Heat Equation on a uniform mesh.

    Parameters
    ----------
    temp : ndarray
        Temperature.
    spacing : array_like
        Grid spacing in the row and column directions.
    out : ndarray (optional)
        Output array.
    alpha : float (optional)
        Thermal diffusivity.
    time_step : float (optional)
        Time step.

    Returns
    -------
    result : ndarray
        The temperatures after time *time_step*.

    Examples
    --------
    >>> from heat import solve_2d
    >>> z0 = np.zeros((3, 3))
    >>> z0[1:-1, 1:-1] = 1.
    >>> solve_2d(z0, (1., 1.), alpha=.25)
    array([[0. , 0. , 0. ],
           [0. , 0.5, 0. ],
           [0. , 0. , 0. ]])
    """
    dy2, dx2 = spacing[0] ** 2, spacing[1] ** 2
    stencil = (
        np.array([[0.0, dy2, 0.0], [dx2, -2.0 * (dx2 + dy2), dx2], [0.0, dy2, 0.0]])
        * alpha
        * time_step
        / (2.0 * (dx2 * dy2))
    )

    if out is None:
        out = np.empty_like(temp)

    ndimage.convolve(temp, stencil, output=out)
    out[(0, -1), :] = 0.0
    out[:, (0, -1)] = 0.0
    return np.add(temp, out, out=out)


class Heat:
    """Solve the Heat equation on a grid.

    Examples
    --------
    >>> heat = Heat()
    >>> heat.time
    0.0
    >>> heat.time_step
    0.25
    >>> heat.advance_in_time()
    >>> heat.time
    0.25

    >>> heat = Heat(shape=(5, 5))
    >>> heat.temperature = np.zeros_like(heat.temperature)
    >>> heat.temperature[2, 2] = 1.
    >>> heat.advance_in_time()

    >>> heat = Heat(alpha=.5)
    >>> heat.time_step
    0.5
    >>> heat = Heat(alpha=.5, spacing=(2., 3.))
    >>> heat.time_step
    2.0
    """

    def __init__(
        self,
        shape: tuple[int, int] = (10, 20),
        spacing: tuple[float, float] = (1.0, 1.0),
        origin: tuple[float, float] = (0.0, 0.0),
        alpha: float = 1.0,
    ) -> None:
        """Create a new heat model.

        Parameters
        ---------
        shape : array_like, optional
            The shape of the solution grid as (*rows*, *columns*).
        spacing : array_like, optional
            Spacing of grid rows and columns.
        origin : array_like, optional
            Coordinates of lower left corner of grid.
        alpha : float
            Alpha parameter in the heat equation.
        """
        self._shape = shape
        self._spacing = spacing
        self._origin = origin
        self._time = 0.0
        self._alpha = alpha
        self._time_step = min(spacing) ** 2 / (4.0 * self._alpha)

        self._temperature = np.random.random(self._shape)
        self._next_temperature = np.empty_like(self._temperature)

    @property
    def time(self) -> float:
        """Current model time."""
        return self._time

    @property
    def temperature(self) -> NDArray[np.float64]:
        """Temperature of the plate."""
        return self._temperature

    @temperature.setter
    def temperature(self, new_temp: float) -> None:
        """Set the temperature of the plate.

        Parameters
        ----------
        new_temp : array_like
            The new temperatures.
        """
        self._temperature[:] = new_temp

    @property
    def time_step(self) -> float:
        """Model time step."""
        return self._time_step

    @time_step.setter
    def time_step(self, time_step: float) -> None:
        """Set model time step."""
        self._time_step = time_step

    @property
    def shape(self) -> tuple[int, int]:
        """Shape of the model grid."""
        return self._shape

    @property
    def spacing(self) -> tuple[float, float]:
        """Spacing between nodes of the model grid."""
        return self._spacing

    @property
    def origin(self) -> tuple[float, float]:
        """Origin coordinates of the model grid."""
        return self._origin

    @classmethod
    def from_file_like(cls: type[Heat], file_like: TextIOBase) -> Heat:
        """Create a Heat object from a file-like object.

        Parameters
        ----------
        file_like : file_like
            Input parameter file.

        Returns
        -------
        Heat
            A new instance of a Heat object.
        """
        config = yaml.safe_load(file_like)
        return cls(**config)

    def advance_in_time(self) -> None:
        """Calculate new temperatures for the next time step."""
        solve_2d(
            self._temperature,
            self._spacing,
            out=self._next_temperature,
            alpha=self._alpha,
            time_step=self._time_step,
        )
        np.copyto(self._temperature, self._next_temperature)

        self._time += self._time_step
