#! /usr/bin/env python


class BmiBase(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    def initialize(self, filename):
        """Performs startup tasks for the model.

        **Initialize()** performs all tasks that take place before
        entering the model's time loop, including opening files and
        initializing the model state. Model inputs are read from a
        text-based configuration file, specified by `filename`.

        Parameters
        ----------
        filename : str, optional
          The path to the model configuration file.

        Bindings
        --------
        C : int initialize(void *self, char * filename);

        Notes
        -----
        Models should be refactored, if necessary, to use a
        configuration file. CSDMS does not impose any constraint on
        how configuration files are formatted, although YAML is
        recommended. A template of a model's configuration file
        with placeholder values is used by the BMI.

        """
        pass

    def update(self):
        """Advances model state by one time step.

        **Update()** performs all tasks that take place within one pass
        through the model's time loop. This typically includes
        incrementing all of the model's state variables. If the
        model's state variables don't change in time, then they can be
        computed by **initialize()** and this method can
        return with no action.

        """
        pass

    def update_until(self, time):
        """Advances model state until the given time.

        Parameters
        ----------
        time : float
          A model time value.

        See Also
        --------
        update

        """
        pass

    def update_frac(self, time_frac):
        """Advances model state by a fraction of a time step.

        Parameters
        ----------
        time_frac : float
          A fraction of a model time step value.

        See Also
        --------
        update

        """
        pass

    def finalize(self):
        """Performs tear-down tasks for the model.

        **Finalize()** performs all tasks that take place after exiting
        the model's time loop. This typically includes deallocating
        memory, closing files and printing reports.

        """
        pass


