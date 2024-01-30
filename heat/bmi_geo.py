from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import numpy as np
from numpy.typing import NDArray


class BmiGeo(ABC):

    @abstractmethod
    def initialize(self, filename: str=None) -> None:
        ...

    @abstractmethod
    def get_grid_coordinate_names(self, grid: int) -> tuple[str, ...]:
        ...

    @abstractmethod
    def get_grid_coordinate_units(self, grid: int) -> tuple[str, ...]:
        ...
    
    @abstractmethod
    def get_grid_coordinate(self, grid: int, coordinate: str, values: NDArray[np.float64]) -> None:
        ...

    @abstractmethod
    def get_grid_crs(self, grid: int) -> str:
        ...
