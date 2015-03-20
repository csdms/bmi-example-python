#! /usr/bin/env python


class BmiGridUniformRectilinear(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    def get_grid_shape(self, grid_id):
        """Returns the dimensions of a computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of int
          The dimensions of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_spacing(self, grid_id):
        """Returns the distance between nodes of a computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of float
          The grid spacing.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass

    def get_grid_origin(self, grid_id):
        """Returns coordinates for the origin of a computational grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        tuple of float
          The coordinates of the lower left corner of the grid.

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass
