#! /usr/bin/env python


class BmiTime(object):
    """Methods that get time information from a model.
    """

    def get_start_time(self):
        """The start time of the model.

        Model times should be of type float. The default model start
        time is 0.

        Returns
        -------
        float
          The model start time.

        Notes
        -----
        .. code-block:: c
        
            /* C */
            int get_start_time(void * self, double * time);
        """
        pass

    def get_current_time(self):
        """The model's current time.

        Returns
        -------
        float
          The current model time.

        See Also
        --------
        get_start_time

        Notes
        -----
        .. code-block:: c
        
            /* C */
            int get_current_time(void * self, double * time);
        """
        pass

    def get_end_time(self):
        """The maximum time of the model.

        Returns
        -------
        float
          The maximum model time.

        See Also
        --------
        get_start_time

        Notes
        -----
        .. code-block:: c
        
            /* C */
            int get_end_time(void * self, double * time);
        """
        pass

    def get_time_step(self):
        """The model's current time step.

        The model time step should be of type float. The default time
        step is 1.0.

        Returns
        -------
        float
          The time step used in model.

        Notes
        -----
        .. code-block:: c
        
            /* C */
            int get_time_step(void * self, double * dt);
        """
        pass

    def get_time_units(self):
        """The model's time units.

        Returns
        -------
        float
          The model time unit; e.g., 'days' or 's'.

        See Also
        --------
        get_var_units

        Notes
        -----
        .. code-block:: c
        
            /* C */
            int get_time_units(void * self, char * units);
        """
        pass
