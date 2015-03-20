#! /usr/bin/env python


class BmiGridStructuredQuad(object):
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

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

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

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

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

        See Also
        --------
        bmi.vars.BmiVars.get_var_grid : Obtain a `grid_id`.

        """
        pass
