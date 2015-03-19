#! /usr/bin/env python


class BmiInfo(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    def get_component_name(self):
        """Returns the name of the component.

        Returns
        -------
        str
          The name of the component.

        """
        pass

    def get_input_var_names(self):
        """Lists the model's input variables.

        Input variable names must be CSDMS Standard Names, also known
        as *long variable names*.

        Returns
        -------
        list of str
          The input variables for the model.

        Notes
        -----
        Standard Names enable the CSDMS framework to determine whether
        an input variable in one model is equivalent to, or compatible
        with, an output variable in another model. This allows the
        framework to automatically connect components.

        Standard Names do not have to be used within the model.

        """
        pass

    def get_output_var_names(self):
        """Lists the model's output variables.

        Output variable names must be CSDMS Standard Names, also known
        as *long variable names*.

        Returns
        -------
        list of str
          The output variables for the model.

        See Also
        --------
        get_input_var_names

        """
        pass

