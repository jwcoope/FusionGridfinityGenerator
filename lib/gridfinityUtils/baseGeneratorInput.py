import adsk.core, adsk.fusion, traceback

from .const import DIMENSION_MAGNET_CUTOUT_DEPTH, DIMENSION_MAGNET_CUTOUT_DIAMETER, DIMENSION_SCREW_HOLE_DIAMETER

class BaseGeneratorInput():
    def __init__(self):
        self.hasMagnetCutouts = False
        self.hasScrewHoles = False
        self.screwHolesDiameter = DIMENSION_SCREW_HOLE_DIAMETER
        self.magnetCutoutsDiameter = DIMENSION_MAGNET_CUTOUT_DIAMETER
        self.magnetCutoutsDepth = DIMENSION_MAGNET_CUTOUT_DEPTH

    @property
    def baseWidth(self) -> float:
        return self._baseWidth

    @baseWidth.setter
    def baseWidth(self, value: float):
        self._baseWidth = value

    @property
    def xyTolerance(self) -> float:
        return self._xyTolerance

    @xyTolerance.setter
    def xyTolerance(self, value: float):
        self._xyTolerance = value

    @property
    def hasScrewHoles(self) -> bool:
        return self._hasScrewHoles

    @hasScrewHoles.setter
    def hasScrewHoles(self, value: bool):
        self._hasScrewHoles = value

    @property
    def screwHolesDiameter(self) -> float:
        return self._screwHolesDiameter

    @screwHolesDiameter.setter
    def screwHolesDiameter(self, value: float):
        self._screwHolesDiameter = value

    @property
    def hasMagnetCutouts(self) -> bool:
        return self._hasMagnetCutouts

    @hasMagnetCutouts.setter
    def hasMagnetCutouts(self, value: bool):
        self._hasMagnetCutouts = value

    @property
    def magnetCutoutsDiameter(self) -> float:
        return self._magnetCutoutsDiameter

    @magnetCutoutsDiameter.setter
    def magnetCutoutsDiameter(self, value: float):
        self._magnetCutoutsDiameter = value

    @property
    def magnetCutoutsDepth(self) -> float:
        return self._magnetCutoutsDepth

    @magnetCutoutsDepth.setter
    def magnetCutoutsDepth(self, value: float):
        self._magnetCutoutsDepth = value