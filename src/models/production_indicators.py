#!/usr/bin/env python3
# production_indicators.py

def calculate_production_rate(output_quantity, running_time):
    """
    Calculates the production rate.

    Args:
        output_quantity (float): The quantity of the output produced.
        running_time (float): The running time of the machine.

    Returns:
        float: The production rate.
    """
    production_rate = output_quantity / running_time
    return production_rate


def calculate_efficiency(actual_production_rate, maximum_production_rate):
    """
    Calculates the efficiency.

    Args:
        actual_production_rate (float): The actual production rate.
        maximum_production_rate (float): The maximum achievable production rate.

    Returns:
        float: The efficiency.
    """
    efficiency = (actual_production_rate / maximum_production_rate) * 100
    return efficiency


def calculate_yield(output_quantity, input_quantity):
    """
    Calculates the yield.

    Args:
        output_quantity (float): The quantity of the output produced.
        input_quantity (float): The quantity of the input used.

    Returns:
        float: The yield.
    """
    yield_value = (output_quantity / input_quantity) * 100
    return yield_value


# Additional indicator calculation functions can be added here...


def calculate_indicators(output_quantity, running_time, maximum_production_rate, input_quantity):
    """
    Calculates the key production indicators.

    Args:
        output_quantity (float): The quantity of the output produced.
        running_time (float): The running time of the machine.
        maximum_production_rate (float): The maximum achievable production rate.
        input_quantity (float): The quantity of the input used.

    Returns:
        dict: A dictionary containing the calculated production indicators.
    """
    indicators = {}

    indicators['Production Rate'] = calculate_production_rate(output_quantity, running_time)
    indicators['Efficiency'] = calculate_efficiency(indicators['Production Rate'], maximum_production_rate)
    indicators['Yield'] = calculate_yield(output_quantity, input_quantity)

    # Additional indicators can be calculated and added to the dictionary here...

    return indicators
