#! /usr/bin/env python


class BmiVars(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    def get_var_type(self, long_var_name):
        """Returns the type of the given variable.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        str
          The Python variable type; e.g., `str`, `int`, `float`.

        """
        pass

    def get_var_units(self, long_var_name):
        """Returns the units of the given variable.

        Standard unit names, in lower case, should be used, such as
        "meters" or "seconds". Standard abbreviations, like "m" for
        meters, are also supported. For variables with compound units,
        each unit name is separated by a single space, with exponents
        other than 1 placed immediately after the name, as in "m s-1"
        for velocity, "W m-2" for an energy flux, or "km2" for an
        area.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        str
          The variable units.

        Notes
        -----
        CSDMS uses the UDUNITS standard from Unidata.

        """
        pass

    def get_var_nbytes(self, long_var_name):
        """Returns the size, in bytes, of the given variable.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        int
          The size of the variable, counted in bytes.

        """
        pass

    def get_var_grid(self, long_var_name):
        """Returns the identifier of the grid associated with a given
        variable.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        int
          The grid identifier.

        """
        pass

