from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from heat.bmi_geo import BmiGeo
from heat.bmi_heat import BmiHeat


class BmiHeatGeo(BmiGeo):
    def __init__(self, bmi_heat: BmiHeat):
        self._bmi_heat = bmi_heat

    def initialize(self, filename: str = None) -> None:
        pass

    def get_grid_coordinate_names(self, grid: int) -> tuple[str, ...]:
        return ("y", "x")

    def get_grid_coordinate_units(self, grid: int) -> tuple[str, ...]:
        return ("m", "m")

    def get_grid_coordinate(
        self, grid: int, coordinate: str, values: NDArray[np.float64]
    ) -> None:
        coords = np.meshgrid(
            range(self._bmi_heat._model.shape[0]),
            range(self._bmi_heat._model.shape[1]),
            indexing="ij"
        )
        if coordinate == "y":
            dim = 0
        elif coordinate == "x":
            dim = 1
        else:
            raise RuntimeError(f"{coordinate}: unknown coordinate")

        values[:] = coords[dim].reshape(-1) * self._bmi_heat._model.spacing[dim] + self._bmi_heat._model.origin[dim]

    def get_grid_crs(self, grid: int) -> str:
        return "none"
