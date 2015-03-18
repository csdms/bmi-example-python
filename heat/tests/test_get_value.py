#!/usr/bin/env python
from nose.tools import assert_equal, assert_true, assert_is, assert_is_not
from numpy.testing import assert_array_less, assert_array_almost_equal
import numpy as np

from heat import BmiHeat


def test_get_initial_value():
    model = BmiHeat()
    model.initialize()

    z0 = model.get_value_ref('plate_surface__temperature')
    assert_array_less(z0, 1.)
    assert_array_less(0., z0)


def test_get_value_copy():
    model = BmiHeat()
    model.initialize()

    z0 = model.get_value('plate_surface__temperature')
    z1 = model.get_value('plate_surface__temperature')

    assert_is_not(z0, z1)
    assert_array_almost_equal(z0, z1)


def test_get_value_reference():
    model = BmiHeat()
    model.initialize()

    z0 = model.get_value_ref('plate_surface__temperature')
    z1 = model.get_value('plate_surface__temperature')

    assert_is_not(z0, z1)
    assert_array_almost_equal(z0, z1)

    for _ in xrange(10):
        model.update()

    assert_is(z0, model.get_value_ref('plate_surface__temperature'))


def test_get_value_at_indices():
    model = BmiHeat()
    model.initialize()

    z0 = model.get_value_ref('plate_surface__temperature')
    z1 = model.get_value_at_indices('plate_surface__temperature', [0, 2, 4])

    assert_array_almost_equal(z0.take((0, 2, 4)), z1)


def test_value_size():
    model = BmiHeat()
    model.initialize()

    z = model.get_value_ref('plate_surface__temperature')
    assert_equal(model.get_grid_size(0), z.size)


def test_value_nbytes():
    model = BmiHeat()
    model.initialize()

    z = model.get_value_ref('plate_surface__temperature')
    assert_equal(model.get_var_nbytes('plate_surface__temperature'), z.nbytes)
