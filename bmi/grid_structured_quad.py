#! /usr/bin/env python


class BmiGridStructuredQuad(object):
    """Methods that describe a structured grid of quadrilaterals.

    .. figure:: _static/grid_structured_quad.png
        :scale: 10%
        :align: center
        :alt: An example of a structured quad grid.
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
