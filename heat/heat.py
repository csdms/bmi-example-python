"""The 2D heat model."""

import numpy as np
import yaml
from scipy import ndimage, random


def solve_2d(temp, spacing, out=None, alpha=1.0, time_step=1.0):
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
    >>> solve_2d(z0, (1., 1.), alpha=.125)
    array([[0. , 0. , 0. ],
           [0. , 0.5, 0. ],
           [0. , 0. , 0. ]])
    """
    dy2, dx2 = spacing[0] ** 2, spacing[1] ** 2
    stencil = (
        np.array([[0.0, dy2, 0.0], [dx2, -2.0 * (dx2 + dy2), dx2], [0.0, dy2, 0.0]])
        * alpha
        * time_step
        / (dx2 * dy2)
    )

    if out is None:
        out = np.empty_like(temp)

    ndimage.convolve(temp, stencil, output=out)
    out[(0, -1), :] = 0.0
    out[:, (0, -1)] = 0.0
    return np.add(temp, out, out=out)


class Heat(object):

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
        self, shape=(10, 20), spacing=(1.0, 1.0), origin=(0.0, 0.0), alpha=1.0
    ):
        """Create a new heat model.

        Paramters
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

        self._temperature = random.random(self._shape)
        self._next_temperature = np.empty_like(self._temperature)

    @property
    def time(self):
        """Current model time."""
        return self._time

    @property
    def temperature(self):
        """Temperature of the plate."""
        return self._temperature

    @temperature.setter
    def temperature(self, new_temp):
        """Set the temperature of the plate.

        Parameters
        ----------
        new_temp : array_like
            The new temperatures.
        """
        self._temperature[:] = new_temp

    @property
    def time_step(self):
        """Model time step."""
        return self._time_step

    @time_step.setter
    def time_step(self, time_step):
        """Set model time step."""
        self._time_step = time_step

    @property
    def spacing(self):
        """Shape of the model grid."""
        return self._spacing

    @property
    def origin(self):
        """Origin coordinates of the model grid."""
        return self._origin

    @classmethod
    def from_file_like(cls, file_like):
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
        config = yaml.load(file_like)
        return cls(**config)

    def advance_in_time(self):
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
