.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://github.com/csdms/bmi-example-python/workflows/Build/Test%20CI/badge.svg
    :target: https://github.com/csdms/bmi-example-python/actions?query=workflow%3A%22Build%2FTest+CI%22

.. image:: https://coveralls.io/repos/csdms/bmi-example-python/badge.png?branch=master
    :target: https://coveralls.io/r/csdms/bmi-example-python?branch=master

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/csdms/bmi

bmi-example-python
==================

An example of implementing the `Python bindings`_
for the CSDMS `Basic Model Interface`_ (BMI).

Overview
--------

This is an example of implementing a BMI for a simple model
that solves the diffusion equation
on a uniform rectangular plate
with Dirichlet boundary conditions.
The model and its BMI are written in Python 3.
Tests of the BMI are provided.

This repository is organized with the following directories:

*heat*
  Source code for the model and its BMI

*examples*
  Jupyter Notebooks that demonstrate how to run the model through its BMI

*tests*
  Tests that cover the BMI of the model

Build/Install
-------------

This example can be built and installed on Linux, macOS, and Windows.

**Prerequisites:**

* Python 3
* The Python BMI bindings. Follow the build and install directions
  given in the `README`_ in that repository. You can choose to install
  them from source, or through `pip` or `conda`.

To build/install this example from source,
using the current Python BMI version, run

.. code-block:: bash

  $ pip install -e .

To run the tests,

.. code-block:: bash

  $ pip install -r requirements-testing.txt
  $ make test


.. _Python bindings: https://github.com/csdms/bmi-python
.. _Basic Model Interface: https://bmi-spec.readthedocs.io
.. _README: https://github.com/csdms/bmi-python/blob/master/README.rst
