#! /usr/bin/env python


class BmiGridUniformRectilinear(object):
    """Methods that describe a uniform rectilinear grid.

    In a 2D uniform grid, every grid cell (or element) is a rectangle and all
    cells have the same dimensions. If the dimensions are equal, then the
    grid is a tiling of squares.

    Each of these functions returns information about each dimension of a
    grid. The dimensions are ordered with "ij" indexing (as opposed to "xy").
    For example, the :func:`get_grid_shape` function for the example grid would
    return the array ``[4, 5]``. If there were a third dimension, the length of
    the z dimension would be listed first. This same convention is used in
    NumPy. Note that the grid shape is the number of nodes in the coordinate
    directions and not the number of cells or elements. It is possible for
    grid values to be associated with the nodes or with the cells.

    .. figure:: _static/grid_uniform_rectilinear.png
        :scale: 10%
        :align: center
        :alt: An example of a uniform rectilinear grid
    """

    def get_grid_shape(self, grid_id):
        """Returns the dimensions of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of int
          The dimensions of the grid.

        """
        pass

    def get_grid_spacing(self, grid_id):
        """Returns the distance between nodes of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of float
          The grid spacing.

        """
        pass

    def get_grid_origin(self, grid_id):
        """Returns coordinates for the origin of the computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of float
          The coordinates of the lower left corner of the grid.

        """
        pass
