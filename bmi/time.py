#! /usr/bin/env python


class BmiTime(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    def get_start_time(self):
        """Returns the start time of the model.

        Model times should be of type float. The default model start
        time is 0.

        Returns
        -------
        float
          The model start time.

        """
        pass

    def get_current_time(self):
        """Returns the model's current time.

        Returns
        -------
        float
          The current model time.

        See Also
        --------
        get_start_time

        """
        pass

    def get_end_time(self):
        """Returns the maximum time of the model.

        Returns
        -------
        float
          The maximum model time.

        See Also
        --------
        get_start_time

        """
        pass

    def get_time_step(self):
        """Returns the model's current time step.

        The model time step should be of type float. The default time
        step is 1.0.

        Returns
        -------
        float
          The time step used in model.

        """
        pass

    def get_time_units(self):
        """Returns the model's time units.

        Returns
        -------
        float
          The model time unit; e.g., 'days' or 's'.

        See Also
        --------
        get_var_units

        """
        pass


