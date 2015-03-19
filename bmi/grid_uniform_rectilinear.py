#! /usr/bin/env python


class BmiGridUniformRectilinear(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
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
