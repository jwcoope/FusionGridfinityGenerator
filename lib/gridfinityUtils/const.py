import adsk.core, adsk.fusion, traceback

BIN_XY_TOLERANCE = 0.01
BIN_CORNER_FILLET_RADIUS = 0.4 - BIN_XY_TOLERANCE
BIN_WALL_THICKNESS = 0.24
BIN_LIP_CHAMFER = 0.12
BIN_CONNECTION_RECESS_DEPTH = 0.4
BIN_BODY_BOTTOM_THICKNESS = 0.1
BIN_BODY_CUTOUT_BOTTOM_FILLET_RADIUS = 0.2

BASE_TOTAL_HEIGHT = 0.5

DIMENSION_DEFAULT_WIDTH_UNIT = 4.2
DIMENSION_DEFAULT_HEIGHT_UNIT = 0.7
DIMENSION_SCREW_HOLES_DISTANCE = 2.6
DIMENSION_SCREW_HOLE_DIAMETER = 0.3
DIMENSION_MAGNET_CUTOUT_DIAMETER = 0.65
DIMENSION_MAGNET_CUTOUT_DEPTH = 0.24
DIMENSION_PRINT_HELPER_GROOVE_DEPTH = 0.03

DEFAULT_FILTER_TOLERANCE = 0.00001