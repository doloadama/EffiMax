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


def calculate_quality_rate(acceptable_quantity, total_quantity):
    """
    Calculates the quality rate.

    Args:
        acceptable_quantity (float): The quantity of acceptable output.
        total_quantity (float): The total quantity of output produced.

    Returns:
        float: The quality rate.
    """
    quality_rate = (acceptable_quantity / total_quantity) * 100
    return quality_rate


def calculate_availability_rate(working_time, total_time):
    """
    Calculates the availability rate.

    Args:
        working_time (float): The working time of the machine.
        total_time (float): The total time including working and non-working time.

    Returns:
        float: The availability rate.
    """
    availability_rate = (working_time / total_time) * 100
    return availability_rate
#!/usr/bin/env python3 

def calculate_indicators(output_quantity, running_time, acceptable_quantity, total_quantity, working_time, total_time):
    """
    Calculates the key production indicators.

    Args:
        output_quantity (float): The quantity of the output produced.
        running_time (float): The running time of the machine.
        acceptable_quantity (float): The quantity of acceptable output.
        total_quantity (float): The total quantity of output produced.
        working_time (float): The working time of the machine.
        total_time (float): The total time including working and non-working time.

    Returns:
        dict: A dictionary containing the calculated production indicators.
    """
    indicators = {}

    indicators['Production Rate'] = calculate_production_rate(output_quantity, running_time)
    indicators['Quality Rate'] = calculate_quality_rate(acceptable_quantity, total_quantity)
    indicators['Availability Rate'] = calculate_availability_rate(working_time, total_time)

    return indicators
