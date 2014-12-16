import numpy as np
from scipy import ndimage, random
import yaml


def solve_2d(temp, spacing, out=None, alpha=1., dt=1.):
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
    dt : float (optional)
        Time step.

    Returns
    -------
    result : ndarray
        The temperatures after time *dt*.

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
                        [0., dy2, 0.]]) * alpha * dt / (dx2 * dy2)

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
    >>> heat.dt
    0.25
    >>> heat.advance_in_time()
    >>> heat.time
    0.25

    >>> heat = Heat(shape=(5, 5))
    >>> heat.z = np.zeros_like(heat.z)
    >>> heat.z[2, 2] = 1.
    >>> heat.advance_in_time()

    >>> heat = Heat(alpha=.5)
    >>> heat.dt
    0.5
    >>> heat = Heat(alpha=.5, spacing=(2., 3.))
    >>> heat.dt
    2.0
    """
    def __init__(self, shape=(10, 20), spacing=(1., 1.), origin=(0., 0.),
                 alpha=1.):
        self._shape = shape
        self._spacing = spacing
        self._origin = origin
        self._time = 0.
        self._alpha = alpha
        self._dt = min(spacing) ** 2 / (4. * self._alpha)

        self._z = random.random(self._shape)
        self._z_temp = np.empty_like(self._z)

    @property
    def time(self):
        return self._time

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, new_z):
        self._z[:] = new_z

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, dt):
        self._dt = dt

    @property
    def spacing(self):
        return self._spacing

    @property
    def origin(self):
        return self._origin

    @classmethod
    def from_file_like(clazz, file_like):
        config = yaml.load(file_like)
        return clazz(**config)

    def advance_in_time(self):
        solve_2d(self._z, self._spacing, out=self._z_temp, alpha=self._alpha,
                 dt=self._dt)
        np.copyto(self._z, self._z_temp)

        self._time += self._dt
