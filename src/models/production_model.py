#!/usr/bin/env python3
# production_model.py

class RawMaterialInventory:
    """
    Represents the inventory of raw materials in the production process.
    """

    def __init__(self, name, stock, input_date, output_date):
        """
        Initializes a RawMaterialInventory object.

        Args:
            name (str): The name of the raw material.
            stock (float): The stock of the raw material.
            input_date (str): The date of input.
            output_date (str): The date of output.
        """
        self.name = name
        self.stock = stock
        self.input_date = input_date
        self.output_date = output_date


class FinalProduct:
    """
    Represents the final product in the production process.
    """

    def __init__(self, name, input_stock, output_stock, input_date, output_date, non_quality_quantity):
        """
        Initializes a FinalProduct object.

        Args:
            name (str): The name of the final product.
            input_stock (float): The stock of the final product as input.
            output_stock (float): The stock of the final product as output.
            input_date (str): The date of input.
            output_date (str): The date of output.
            non_quality_quantity (float): The quantity of non-quality final product.
        """
        self.name = name
        self.input_stock = input_stock
        self.output_stock = output_stock
        self.input_date = input_date
        self.output_date = output_date
        self.non_quality_quantity = non_quality_quantity


class Machine:
    """
    Represents a machine in the production process.
    """

    def __init__(self, name, working_time, non_working_time, failures_time, surprise_me):
        """
        Initializes a Machine object.

        Args:
            name (str): The name of the machine.
            working_time (float): The working time of the machine.
            non_working_time (float): The non-working time of the machine.
            failures_time (float): The time due to machine failures.
            surprise_me: Any additional parameter you would like to include.
        """
        self.name = name
        self.working_time = working_time
        self.non_working_time = non_working_time
        self.failures_time = failures_time
        self.surprise_me = surprise_me


class ProductionModel:
    """
    Represents the production model.
    """

    def __init__(self, unit_of_measurement):
        """
        Initializes a ProductionModel object.

        Args:
            unit_of_measurement (str): The unit of measurement for weight, such as kilogram, pound, etc.
        """
        self.unit_of_measurement = unit_of_measurement
