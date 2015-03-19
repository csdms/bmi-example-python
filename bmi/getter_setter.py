#! /usr/bin/env python


class BmiGetter(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """


    def get_value(self, long_var_name):
        """Returns the value of the given variable.

        This is a getter for the model, used to access the model's
        current state. It returns a copy of a model variable, with
        the return type, size and rank dependent on the variable.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        object
          The value of a model variable.

        """
        pass

    def get_value_ref(self, long_var_name):
        """Returns a given variable.

        This is a getter for the model, used to access the model's
        current state. It returns a reference to a model variable,
        with the return type, size and rank dependent on the variable.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        object
          A model variable.

        """
        pass

    def get_value_at_indices(self, long_var_name, inds):
        """Returns the value of the given variable at a location in the model
        grid.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.
        inds : array_like
          The indices into the variable array.

        """
        pass


class BmiSetter(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    def set_value(self, long_var_name, src):
        """Specifies a new value for a model variable.

        This is the setter for the model, used to change the model's
        current state. It accepts, through `src`, a new value for a
        model variable, with the type, size and rank of `src`
        dependent on the variable.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.
        src : array_like
          The new value for the specified variable.

        """
        pass

    def set_value_at_indices(self, long_var_name, inds, src):
        """Specifies a new value for a model variable at a location in the
        model grid.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.
        inds : array_like
          The indices into the variable array.
        src : array_like
          The new value for the specified variable.

        """
        pass
