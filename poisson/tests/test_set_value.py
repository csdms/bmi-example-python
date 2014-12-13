#!/usr/bin/env python
from nose.tools import assert_is, assert_is_not
from numpy.testing import assert_array_almost_equal
import numpy as np

from poisson import BmiPoisson


def test_set_value():
    model = BmiPoisson()
    model.initialize()

    z0 = model.get_value_ptr('land_surface__elevation')
    z1 = np.zeros_like(z0) - 1

    model.set_value('land_surface__elevation', z1)

    new_z = model.get_value_ptr('land_surface__elevation')

    assert_is(new_z, z0)
    assert_is_not(new_z, z1)
    assert_array_almost_equal(new_z, z1)


def test_set_value_at_indices():
    model = BmiPoisson()
    model.initialize()

    z0 = model.get_value_ptr('land_surface__elevation')

    model.set_value_at_indices('land_surface__elevation', [-1, -1, -1],
                               [0, 2, 4])

    new_z = model.get_value_ptr('land_surface__elevation')
    assert_array_almost_equal(new_z.take((0, 2, 4)), -1.)
