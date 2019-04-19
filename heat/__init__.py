"""Model the diffusion of heat over a 2D plate."""

from ._version import get_versions
from .bmi_heat import BmiHeat
from .heat import solve_2d

__all__ = ["BmiHeat", "solve_2d"]

__version__ = get_versions()["version"]
del get_versions

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
