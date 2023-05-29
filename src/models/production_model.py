#!/usr/bin/env python3
# production_model.py

class Material:
    """
    Represents the raw material in the production process.
    """

    def __init__(self, name, input_quantity, output_quantity, previous_stock):
        """
        Initializes a Material object.

        Args:
            name (str): The name of the raw material.
            input_quantity (float): The quantity of the raw material as input.
            output_quantity (float): The quantity of the raw material as output.
            previous_stock (float): The stock of the raw material from the previous cycle.
        """
        self.name = name
        self.input_quantity = input_quantity
        self.output_quantity = output_quantity
        self.previous_stock = previous_stock # the previous stock is the stock before the input
        self.stock = previous_stock + input_quantity - output_quantity


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
