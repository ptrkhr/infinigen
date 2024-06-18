# Copyright (c) Princeton University.
# This source code is licensed under the BSD 3-Clause license found in the LICENSE file in the root directory of this source tree.

# Authors: Hongyu Wen

from infinigen.infinigen_gpl.surfaces import *

from . import *
from .metal import brushed_metal, galvanized_metal, grained_and_polished_metal, hammered_metal, metal_basic
from .metal.brushed_metal import shader_brushed_metal
from .metal.galvanized_metal import shader_galvanized_metal
from .metal.grained_and_polished_metal import shader_grained_metal
from .metal.hammered_metal import shader_hammered_metal
from .metal.metal_basic import shader_metal

metal_shader_list = [
    shader_brushed_metal,
    shader_galvanized_metal,
    shader_grained_metal,
    shader_hammered_metal,
    shader_metal,
]

from .plastic import shader_rough_plastic, shader_translucent_plastic

plastic_shader_list = [shader_rough_plastic, shader_translucent_plastic]

from .woods.wood import shader_wood

wood_shader_list = [shader_wood]

from .glass import shader_glass

glass_shader_list = [shader_glass]

from .art import Art, ArtFabric, ArtRug, DarkArt
from .leather_and_fabrics import (
    coarse_knit_fabric,
    fine_knit_fabric,
    general_fabric,
    leather,
    lined_fabric,
    sofa_fabric,
    velvet,
)
from .stone_and_concrete import concrete
from .woods import (
    composite_wood_tile,
    crossed_wood_tile,
    hexagon_wood_tile,
    non_wood_tile,
    square_wood_tile,
    staggered_wood_tile,
    tiled_wood,
    wood,
    wood_old,
    wood_tile,
)
