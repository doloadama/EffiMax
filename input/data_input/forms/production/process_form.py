#!/usr/bin/env python3

"""
process_form.py
Module for generating the process form.
"""

from django import forms
from .production_form import ProductionForm

class ProcessForm(forms.Form):
    """
    ProcessForm class for generating the process form.
    """

    machine_id = forms.CharField(max_length=50)
    process_date = forms.DateTimeField()
    worker_name = forms.CharField(max_length=100)
    process_description = forms.CharField(widget=forms.Textarea)

    def clean(self):
        """
        Clean method to perform additional validation or cleaning logic.
        """
        cleaned_data = super().clean()

        # Perform additional validation or cleaning logic if needed

        # Fetch production quantity from ProductionForm
        production_form = ProductionForm(self.data)
        if production_form.is_valid():
            produced_quantity = production_form.cleaned_data['produced_quantity']
        else:
            produced_quantity = 0

        # Calculate productivity rate
        productivity_rate = calculate_productivity_rate(produced_quantity, cleaned_data['process_date'])
        cleaned_data['productivity_rate'] = productivity_rate

        # Calculate availability rate
        availability_rate = calculate_availability_rate(cleaned_data['process_date'])
        cleaned_data['availability_rate'] = availability_rate

        # Calculate quality rate
        quality_rate = calculate_quality_rate(produced_quantity)
        cleaned_data['quality_rate'] = quality_rate

        # Calculate synthetic rate of return
        synthetic_rate_of_return = calculate_synthetic_rate_of_return(productivity_rate, availability_rate, quality_rate)
        cleaned_data['synthetic_rate_of_return'] = synthetic_rate_of_return

        return cleaned_data

def calculate_productivity_rate(produced_quantity, process_date):
    """
    Calculate the productivity rate based on the produced quantity and process date.
    Add your calculation logic here.
    """
    # Placeholder calculation
    productivity_rate = produced_quantity / process_date.hour  # Example value
    return productivity_rate

def calculate_availability_rate(process_date):
    """
    Calculate the availability rate based on the process date.
    Add your calculation logic here.
    """
    # Placeholder calculation
    availability_rate = 0.95  # Example value
    return availability_rate

def calculate_quality_rate(produced_quantity):
    """
    Calculate the quality rate based on the produced quantity.
    Add your calculation logic here.
    """
    # Placeholder calculation
    quality_rate = 0.98  # Example value
    return quality_rate

def calculate_synthetic_rate_of_return(productivity_rate, availability_rate, quality_rate):
    """
    Calculate the synthetic rate of return based on the productivity, availability, and quality rates.
    Add your calculation logic here.
    """
    # Placeholder calculation
    synthetic_rate_of_return = productivity_rate * availability_rate * quality_rate  # Example value
    return synthetic_rate_of_return
