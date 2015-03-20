#! /usr/bin/env python
"""The complete Basic Model Interface."""


from .base import BmiBase
from .info import BmiInfo
from .time import BmiTime
from .vars import BmiVars
from .getter_setter import BmiGetter, BmiSetter
from .grid_rectilinear import BmiGridRectilinear
from .grid_uniform_rectilinear import BmiGridUniformRectilinear
from .grid_structured_quad import BmiGridStructuredQuad
from .grid_unstructured import BmiGridUnstructured


class Bmi(BmiBase, BmiInfo, BmiTime, BmiVars, BmiGetter, BmiSetter,
          BmiGridRectilinear, BmiGridUniformRectilinear, BmiGridStructuredQuad,
          BmiGridUnstructured):

    """The complete Basic Model Interface.

    Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    pass
