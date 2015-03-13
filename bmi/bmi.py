#! /usr/bin/env python

class BmiGridType(object):
    UNKNOWN = 0
    UNIFORM = 1
    RECTILINEAR = 2
    STRUCTURED = 3
    UNSTRUCTURED = 4


class Bmi(object):
    """Defines an interface for converting a standalone model into an
    integrated modeling framework component.
    """

    def initialize(self, filename):
        """Performs startup tasks for the model.

        Initialize() performs all tasks that take place before
        entering the model's time loop, including opening files and
        initializing the model state. Models should be refactored, if
        necessary, to read their inputs from a text-based
        configuration file, specified by `filename`. CSDMS does not
        impose any constraint on how configuration files are formatted
        (although YAML is recommended). A "template" of a model's
        configuration file with placeholder values is used by the BMI.

        Parameters
        ----------
        filename : str, optional
          The path to the model configuration file.

        Returns
        -------
        int
          Non-zero value indicates error code, or zero on success.

        """
        pass

    def update(self):
        """Advances model state by one time step.

        Update() performs all tasks that take place within one pass
        through the model's time loop. This typically includes
        incrementing all of the model's state variables. If the
        model's state variables don't change in time, then they can be
        computed by the ***initialize()*** method and this method can
        return with no action.

        Returns
        -------
        int
          Non-zero value indicates error code, or zero on success.

        """
        pass

    def update_until(self, time):
        """Advances model state until the given time step.
        """
        pass

    def update_frac(self, time_frac):
        """Advances model state by a fraction of a time step.
        """
        pass

    def finalize(self):
        """Performs tear-down tasks for the model.

        Finalize() performs all tasks that take place after exiting
        the model's time loop. This typically includes deallocating
        memory, closing files and printing reports.

        Returns
        -------
        int
          Non-zero value indicates error code, or zero on success.

        """
        pass

    def get_component_name(self):
        """Returns the name of the component.
        """
        pass

    def get_input_var_names(self):
        """Lists the model's input variables.
        """
        pass

    def get_output_var_names(self):
        """Lists the model's output variables.
        """
        pass

    def get_var_type(self, long_var_name):
        """Returns the type of the given variable.
        """
        pass

    def get_var_units(self, long_var_name):
        """Returns the units of the given variable.
        """
        pass

    def get_var_rank(self, long_var_name):
        """Returns the number of dimensions of the given variable.
        """
        pass

    def get_var_size(self, long_var_name):
        """Returns the number of elements in the given variable.
        """
        pass

    def get_var_nbytes(self, long_var_name):
        """Returns the size, in bytes, of the given variable.
        """
        pass

    def get_start_time(self):
        """Returns the start time of the model.
        """
        pass

    def get_current_time(self):
        """Returns the model's current time.
        """
        pass

    def get_end_time(self):
        """Returns the end time of the model.
        """
        pass

    def get_time_step(self):
        """Returns the model's current time step.
        """
        pass

    def get_time_units(self):
        """Returns the model's time units.
        """
        pass

    def get_value(self, long_var_name):
        """Returns the value of the given variable.
        """
        pass

    def get_value_at_indices(self, long_var_name, inds):
        """Returns the value of the given variable at a location in the model
        grid.
        """
        pass

    def set_value(self, long_var_name, src):
        """Specifies a new value for a model variable.
        """
        pass

    def set_value_at_indices(self, long_var_name, inds, src):
        """Specifies a new value for a model variable at a location in the
        model grid.
        """
        pass


class BmiRaster(Bmi):
    """Defines an interface for a uniform rectilinear grid.
    """

    def get_grid_shape(self, long_var_name):
        """Returns the dimensions of the computational grid.
        """
        pass

    def get_grid_spacing(self, long_var_name):
        """Returns the spacing between nodes of the computational grid.
        """
        pass

    def get_grid_origin(self, long_var_name):
        """Returns coordinates for the origin of the computational grid.
        """
        pass


class BmiRectilinear(Bmi):
    """Defines an interface for a rectilinear grid with nonuniform
    spacing.
    """

    def get_grid_shape(self, long_var_name):
        """Returns the dimensions of the computational grid.
        """
        pass

    def get_grid_x(self, long_var_name):
        """Returns the grid nodes in the streamwise direction.
        """
        pass

    def get_grid_y(self, long_var_name):
        """Returns the grid nodes in the transverse direction.
        """
        pass

    def get_grid_z(self, long_var_name):
        """Returns the grid nodes in the normal direction.
        """
        pass


class BmiStructured (Bmi):
    """Defines an interface for a grid with nonuniform position and
    spacing of nodes.
    """

    def get_grid_shape(self, long_var_name):
        """Returns the dimensions of the computational grid.
        """
        pass

    def get_grid_x(self, long_var_name):
        """Returns the grid nodes in the streamwise direction.
        """
        pass

    def get_grid_y(self, long_var_name):
        """Returns the grid nodes in the transverse direction.
        """
        pass

    def get_grid_z(self, long_var_name):
        """Returns the grid nodes in the normal direction.
        """
        pass


class BmiUnstructured(Bmi):
    """Defines an interface for an unstructured mesh of nodes.
    """

    def get_grid_x(self, long_var_name):
        """Returns the grid nodes in the streamwise direction.
        """
        pass

    def get_grid_y(self, long_var_name):
        """Returns the grid nodes in the transverse direction.
        """
        pass

    def get_grid_z(self, long_var_name):
        """Returns the grid nodes in the normal direction.
        """
        pass

    def get_grid_connectivity(self, long_var_name):
        """Returns connectivity array of the grid.
        """
        pass

    def get_grid_offset(self, long_var_name):
        """Returns the grid offset values.
        """
        pass
