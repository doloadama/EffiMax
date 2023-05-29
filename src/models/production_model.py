#!/usr/bin/env python3
# production_model.py

class Component:
    """
    Represents a component of the production process.
    """

    def __init__(self, name, quantity):
        """
        Initializes a Component object.

        Args:
            name (str): The name of the component.
            quantity (int): The quantity of the component.
        """
        self.name = name
        self.quantity = quantity


class Parameter:
    """
    Represents a parameter that influences the production process.
    """

    def __init__(self, name, value):
        """
        Initializes a Parameter object.

        Args:
            name (str): The name of the parameter.
            value: The current value of the parameter.
        """
        self.name = name
        self.value = value


class Constraint:
    """
    Represents a constraint that must be satisfied during the optimization process.
    """

    def __init__(self, name, condition):
        """
        Initializes a Constraint object.

        Args:
            name (str): The name of the constraint.
            condition: The condition that the constraint should meet.
        """
        self.name = name
        self.condition = condition
