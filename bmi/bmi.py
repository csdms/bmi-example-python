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
        initializing the model state. Model inputs are read from a
        text-based configuration file, specified by `filename`.

        Parameters
        ----------
        filename : str, optional
          The path to the model configuration file.

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

        Update() performs all tasks that take place within one pass
        through the model's time loop. This typically includes
        incrementing all of the model's state variables. If the
        model's state variables don't change in time, then they can be
        computed by the ***initialize()*** method and this method can
        return with no action.

        """
        pass

    def update_until(self, time):
        """Advances model state until the given time.

        Parameters
        ----------
        time : double
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
        time_frac : double
          A fraction of a model time step value.

        See Also
        --------
        update

        """
        pass

    def finalize(self):
        """Performs tear-down tasks for the model.

        Finalize() performs all tasks that take place after exiting
        the model's time loop. This typically includes deallocating
        memory, closing files and printing reports.

        """
        pass

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

    def get_var_rank(self, long_var_name):
        """Returns the number of dimensions of the given variable.

        Scalars have a rank of 0, vectors a rank of 1, planar grids
        and meshes a rank of 2, and 3D grids and meshes a rank of 3.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        int
          The variable rank.

        """
        pass

    def get_var_size(self, long_var_name):
        """Returns the number of elements in the given variable.

        Parameters
        ----------
        long_var_name : str
          An input or output variable name, a CSDMS Standard Name.

        Returns
        -------
        int
          The count of elements in the variable.

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
