from copy import copy

import bpy

import numpy as np
from numpy.random import uniform, normal

from assets.creatures.geometry.lofting import Skin
from util.math import lerp, randomspacing
from assets.creatures.geometry import lofting 

def extend_cap(skin: Skin, r=1, margin=0):
    res = copy(skin)
    res.ts = np.concatenate([np.array([margin]), skin.ts, np.array([1-margin])], axis=0)
    res.profiles = np.concatenate([skin.profiles[[0]] * r, skin.profiles, skin.profiles[[-1]] * r])
    
    if res.surface_params is not None:
        res.surface_params = np.concatenate([
            skin.surface_params[[0]], skin.surface_params, skin.surface_params[[-1]]])

    return res

def square_cap(s: Skin):
    s = extend_cap(s, r=1, margin=0.01)
    s = extend_cap(s, r=0)
    return s

def bevel_cap(s: Skin, n: int, d: float, profile='SPHERE'):

    ts = np.linspace(1, 0, n) # pct of distance from end

    if profile == 'SPHERE':
        rads = np.sqrt(1 - ts * ts)
    elif profile == 'CHAMFER':
        rads = ts
    else:
        raise ValueError(f'Unrecognized {profile=}')        

    for t, r in zip(ts, rads):
        s = extend_cap(s, r=r, margin=d*t)

    return s

def symmetrize(s: Skin, fac):
    
    #if s.angles is not None:
    #    raise NotImplementedError(f'symmetrize(s: Skin) only supports s.angles = None')
    
    res = copy(s)
    res.profiles = lerp(s.profiles, (s.profiles + s.profiles[:, ::-1])/2, fac)
    
    if s.surface_params is not None:
        res.surface_params = lerp(s.surface_params, (s.surface_params + s.surface_params[:, ::-1]) / 2, fac)
    return res



    s = Skin(ts=ts, profiles=profiles)
    return s

def random_skin(rad, n, m, n_params=1):

    ts = randomspacing(0.03, 0.97, n, margin=0.1)
    angles = None # cutil.randomspacing(-np.pi, 1.5 * np.pi, m, margin=0.4)

    sine_fac = np.sin(ts * np.pi)[:, None]
    sine_fac = sine_fac ** 0.2
    radius_func = lerp(rad * 0.1, rad, sine_fac)

    sigmas = np.array([0.07, 0.4, 0.25])
    o_n, o_m, o_ind = np.clip(normal(sigmas, sigmas/4, 3), 0, 1)
    profiles = radius_func * (
        normal(1, o_n, (n, 1)) *
        normal(1, o_m, (1, m)) *
        normal(1, o_ind, (n, m))
    )
    profiles = np.clip(profiles, 0, 2 * rad)

    sym = 1

    if n_params == 2:
        ring_creases = np.power(uniform(0, 1, (n, 1)), 3) 
        row_creases = np.power(uniform(0, 1, (1, m)), 3) 

        params = np.stack([ring_creases * np.ones((1, m)), row_creases * np.ones((n, 1))], axis=-1)
    else:
        params = uniform(0.1, 10, (n, m, 1))
    
    s = Skin(ts=ts, profiles=profiles, surface_params=params, angles=angles)
    s = extend_cap(s, r=0.5)
    s = extend_cap(s, r=0)

    s = symmetrize(s, fac=sym)
