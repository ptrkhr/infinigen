# Copyright (c) Princeton University.
# This source code is licensed under the BSD 3-Clause license found in the LICENSE file in the root directory
# of this source tree.

# Authors: Alexander Raistrick

import logging
import typing
from dataclasses import dataclass

import bpy
import numpy as np
import trimesh
from mathutils import Matrix, Vector

from infinigen.core.constraints.example_solver import state_def
from infinigen.core.constraints.example_solver.geometry import parse_scene
from infinigen.core.util import blender as butil

logger = logging.getLogger(__name__)


@dataclass
class Move:
    names: typing.List[str]

    def __post_init__(self):
        assert isinstance(self.names, list)

    def apply(self, state: state_def.State):
        raise NotImplementedError

    def revert(self, state: state_def.State):
        raise NotImplementedError

    def accept(self, state: state_def.State):
        pass
