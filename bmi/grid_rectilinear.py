#! /usr/bin/env python


class BmiGridRectilinear(object):
    """Methods that describe a rectilinear grid.

    In a 2D rectilinear grid, every grid cell (or element) is a rectangle but
    different cells can have different dimensions. All cells in the same row
    have the same grid spacing in the y direction and all cells in the same
    column have the same grid spacing in the x direction. Grid spacings can
    be computed as the difference of successive x or y values.

    .. figure:: _static/grid_rectilinear.png
        :scale: 10%
        :align: center
        :alt: An example of a rectilinear grid
    """

    def get_grid_shape(self, grid_id):
        """The dimensions of the computational grid.

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

    def get_grid_x(self, grid_id):
        """Returns the grid nodes in the streamwise direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of float or array_like of float
          The positions of the grid nodes.

        """
        pass

    def get_grid_y(self, grid_id):
        """Returns the grid nodes in the transverse direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of float or array_like of float
          The positions of the grid nodes.

        """
        pass

    def get_grid_z(self, grid_id):
        """Returns the grid nodes in the normal direction.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of float or array_like of float
          The positions of the grid nodes.

        """
        pass
