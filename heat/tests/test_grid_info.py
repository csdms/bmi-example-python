#!/usr/bin/env python
from nose.tools import assert_equal, assert_list_equal
import numpy as np

from heat import BmiHeat


def test_grid_var_names():
    model = BmiHeat()
    model.initialize()

    names = model.get_input_var_names()
    assert_list_equal(names, ['plate_surface__temperature'])

    names = model.get_output_var_names()
    assert_list_equal(names, ['plate_surface__temperature'])


def test_grid_var_units():
    model = BmiHeat()
    model.initialize()
    assert_equal(model.get_var_units('plate_surface__temperature'), 'K')


def test_grid_var_rank():
    model = BmiHeat()
    model.initialize()
    assert_equal(model.get_var_rank('plate_surface__temperature'), 2)


def test_grid_var_shape():
    model = BmiHeat()
    model.initialize()
    assert_equal(model.get_grid_shape('plate_surface__temperature'), (10, 20))


def test_grid_var_spacing():
    model = BmiHeat()
    model.initialize()
    assert_equal(model.get_grid_spacing('plate_surface__temperature'), (1., 1.))


def test_grid_var_origin():
    model = BmiHeat()
    model.initialize()
    assert_equal(model.get_grid_origin('plate_surface__temperature'), (0., 0.))


def test_grid_var_type():
    model = BmiHeat()
    model.initialize()
    assert_equal(model.get_var_type('plate_surface__temperature'), 'float64')


def test_grid_type():
    from bmi import BmiGridType

    model = BmiHeat()
    model.initialize()
    assert_equal(model.get_grid_type('plate_surface__temperature'),
                 BmiGridType.UNIFORM)
    assert_equal(model.get_grid_type('invalid-name'), BmiGridType.UNKNOWN)
