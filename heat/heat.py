"""The 2D heat model."""

import numpy as np
from scipy import ndimage, random
import yaml


def solve_2d(temp, spacing, out=None, alpha=1., time_step=1.):
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
    array([[ 0. ,  0. ,  0. ],
           [ 0. ,  0.5,  0. ],
           [ 0. ,  0. ,  0. ]])
    """
    dy2, dx2 = spacing[0] ** 2, spacing[1] ** 2
    stencil = np.array([[0., dy2, 0.],
                        [dx2, -2. * (dx2 + dy2), dx2],
                        [0., dy2, 0.]]) * alpha * time_step / (dx2 * dy2)

    if out is None:
        out = np.empty_like(temp)

    ndimage.convolve(temp, stencil, output=out)
    out[(0, -1), :] = 0.
    out[:, (0, -1)] = 0.
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

    def __init__(self, shape=(10, 20), spacing=(1., 1.), origin=(0., 0.),
                 alpha=1.):
        self._shape = shape
        self._spacing = spacing
        self._origin = origin
        self._time = 0.
        self._alpha = alpha
        self._time_step = min(spacing) ** 2 / (4. * self._alpha)

        self._temperature = random.random(self._shape)
        self._z_temp = np.empty_like(self._temperature)

    @property
    def time(self):
        return self._time

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temp):
        self._temperature[:] = new_temp

    @property
    def time_step(self):
        return self._time_step

    @time_step.setter
    def time_step(self, time_step):
        self._time_step = time_step

    @property
    def spacing(self):
        return self._spacing

    @property
    def origin(self):
        return self._origin

    @classmethod
    def from_file_like(cls, file_like):
        config = yaml.load(file_like)
        return cls(**config)

    def advance_in_time(self):
        solve_2d(self._temperature, self._spacing, out=self._z_temp,
                 alpha=self._alpha, time_step=self._time_step)
        np.copyto(self._temperature, self._z_temp)

        self._time += self._time_step
