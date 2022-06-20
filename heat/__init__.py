"""Model the diffusion of heat over a 2D plate."""
from ._version import __version__
from .bmi_heat import BmiHeat
from .heat import solve_2d

__all__ = ["__version__", "BmiHeat", "solve_2d"]
