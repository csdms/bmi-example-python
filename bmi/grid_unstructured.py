#! /usr/bin/env python


class BmiGridUnstructured(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

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

    def get_grid_connectivity(self, grid_id):
        """Returns the connectivity array of the grid.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like of float
          The graph of connections between the grid nodes.

        """
        pass

    def get_grid_offset(self, grid_id):
        """Returns the offsets for the grid nodes.

        Parameters
        ----------
        grid_id : int
          A grid identifier.

        Returns
        -------
        array_like of int
          The offsets for the grid nodes.

        """
        pass
