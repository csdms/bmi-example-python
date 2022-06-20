"""Model the diffusion of heat over a 2D plate."""
import pkg_resources

from .bmi_heat import BmiHeat
from .heat import Heat, solve_2d

__all__ = ["BmiHeat", "solve_2d", "Heat"]
__version__ = pkg_resources.get_distribution("bmi-heat").version
