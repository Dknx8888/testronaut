UNITS = ["ml", "oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001


class Volume(object):  # creating class volume
    def __init__(self, magnitude=0, unit='ml'):  # defining the initialize function
        """
            This function has magnitude and unit and checks for
            if the unit is a valid unit from list UNITS and magnitude
            is greater than zero or not.
            Parameter: self, magnitude, unit
            returns: Nothing
            Displays: Nothing
            """
        self.magnitude = float(magnitude)
        self.unit = unit
        if magnitude < 0 and unit in UNITS:  # checking if magnitude is greater than zero or not
            self.magnitude = 0
            self.unit = None
        if magnitude > 0 and unit not in UNITS:  # checking if unit is in units list or not
            self.magnitude = None
            self.unit = None

    def __str__(self):
        """This function prints out an error message if the unit
            is not defined, else gives out the result as specified
            in the documentation provided for the project 11.
            Parameter: self
            Returns: Error message/required result
            Displays: Nothing
            """
        if self.unit is None:  # if unit is none then outputs not a volume
            error_message = "Not a Volume"
            return error_message
        else:
            result = "{:.3f} {}".format(self.magnitude, self.unit)  # outputs the magnitude unto three decimal places
            return result

    def __repr__(self):
        """
        The function is kind of similar as the str function but
        the only difference is that this function focuses on printing
        out the required to be output unto six decimal places.
        Parameter: self
        Returns: Error message/Required result
        Displays: Nothing
        """
        if self.unit is None:  # if unit is none then outputs not a volume
            error_message = "Not a Volume"
            return error_message

        else:
            result = "{:.6f} {}".format(self.magnitude, self.unit)  # outputs the magnitude upto three decimal places
            return result

    def is_valid(self):
        """The function checks if the unit and magnitude provided
            are valid or not. And, the conditions are unit should
            be in the list UNITS and the magnitude should be greater
            than zero.

            Parameter: self
            Returns: Boolean
            Displays: Nothing"""
        if self.unit not in UNITS or self.magnitude < 0:  # checking if unit is in units and magnitude is greater
            # than zero
            return False
        else:
            return True  # returns bool respectively

    def get_units(self):
        """
        This function checks if the units are valid or not and
        if they are valid then the function gets the unit of
        the input provided and returns them.

        Parameter: self
        Returns: unit,none
        Displays: Nothing
        """
        if self.unit in UNITS and self.magnitude > 0:  # if input is valid then gets the unit and returns it.
            return self.unit
        else:
            return None

    def get_magnitude(self):
        """"
        This function checks if the magnitude are valid or not and
        if they are valid then the function gets the magnitude of
        the input provided and returns it.

        Parameter: self
        Returns: magnitude,none
        Displays: Nothing
        """
        if not (self.is_valid()):  # if input is valid then gets the magnitude and returns it.
            return self.magnitude
        if self.unit in UNITS:
            return self.magnitude
        else:
            return None

    def metric(self):
        """
        This function checks if the unit is in milliliters or not,
        if not then it converts it into milliliters and returns the
        desired output.

        parameters: self
        return: self, result
        Displays: Nothing
        """
        if self.unit == 'ml':  # checking if unit is in list units or not
            return self
        else:
            z = ''
            x = self.magnitude
            y = x * MLperOZ  # converting ounces to milliliters
            z = UNITS[0]
            result = Volume(y, z)

            return result

    def customary(self):
        """
        This function checks if the unit is in ounces or not,
        if not then it converts it into ounces and returns the
        desired output.

        parameters: self
        return: self, result
        Displays: Nothing
        """
        if self.unit == 'oz':  # checking if unit is in list units or not
            return self
        else:
            z = ''
            x = self.magnitude
            y = x / MLperOZ  # converting ounces to ounces
            z = UNITS[1]
            result = Volume(y, z)

            return result

    def __eq__(self, other):
        """This function checks if the inputs given by the user are
            equal or not but checking their difference. Their difference
            should be less than already defined variable called DELTA.

            Parameter: self, other
            returns: Boolean
            Displays: Nothing"""
        if self.is_valid() and other.is_valid():  # checking if the input is valid
            if self.unit == other.unit:
                if abs(self.magnitude - other.magnitude) < DELTA:  # checking if difference is less than delta
                    return True
            else:
                return False
        else:
            return False  # returning true and false respectively

    def add(self, other):
        """
        The function first checks if the self and other methods are
        strings or not, if not then checks them if they are valid or not
        if they are then adds them and returns the output if not possible then
        returns an invalid output.
        parameter: self, other
        returns: self, add
        displays: nothing
        """

        if type(other) == float or type(other) == int:  # checking if other is float or int
            addition = self.magnitude + other  # if so, just adding the input
            add = Volume(addition, self.unit)
            return add
        if (self.unit in UNITS and other.unit in UNITS) and (self.magnitude > 0):  # checking if input is valid
            if self.unit == UNITS[0] and other.unit == UNITS[1]:  # checking if units are equivalent
                conversion = other.magnitude * MLperOZ
                addition = conversion + self.magnitude  # adding
                add = Volume(addition, self.unit)
                return add
            elif self.unit == UNITS[1] and other.unit == UNITS[0]:  # checking if units are equivalent
                conversion = other.magnitude / MLperOZ
                addition = conversion + self.magnitude
                add = Volume(addition, self.unit)
                return add
            else:
                self.magnitude += other.magnitude  # adding
        if not (self.is_valid()):  # checking if input is valid or not
            return self
        return self

    def sub(self, other):
        """
        The function first checks if the self and other methods are
        strings or not, if not then checks them if they are valid or not
        if they are then subtracts them and returns the output if not possible then
        returns an invalid output.
        parameter: self, other
        returns: self, sub
        displays: nothing
        """

        if type(other) == float or type(other) == int:  # checking if other is float or not
            subtraction = self.magnitude - other
            sub = Volume(subtraction, self.unit)  # if so then just subtracting the input
            return sub
        if (self.unit in UNITS and other.unit in UNITS) and (self.magnitude > 0):
            if self.unit == UNITS[0] and other.unit == UNITS[1]:  # checking for equivalent units
                conversion = other.magnitude * MLperOZ  # converting if not equal
                subtraction = self.magnitude - conversion  # subtracting
                sub = Volume(subtraction, self.unit)
                return sub
            elif self.unit == UNITS[1] and other.unit == UNITS[0]:  # checking if units are equal
                conversion = other.magnitude / MLperOZ  # conversion
                subtraction = self.magnitude - conversion  # subtraction
                sub = Volume(subtraction, self.unit)
                return sub
            else:
                self.magnitude -= other.magnitude  # subtracting by calling the respective methods
        if not (self.is_valid()):  # checking if input is valid or not
            return self
        return self
