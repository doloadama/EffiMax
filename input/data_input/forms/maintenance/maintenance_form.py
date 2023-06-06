#!/usr/bin/env python3

"""
maintenance_form.py
Module for generating the maintenance form.
"""

from django import forms

class MaintenanceForm(forms.Form):
    """
    MaintenanceForm class for generating the maintenance form.
    """

    machine_id = forms.CharField(max_length=50)
    maintenance_date = forms.DateField()
    maintenance_type = forms.ChoiceField(choices=[('scheduled', 'Scheduled'), ('unscheduled', 'Unscheduled')])
    duration_hours = forms.DecimalField(min_value=0, max_digits=5, decimal_places=2)
    worker_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

    def clean(self):
        """
        Clean method to perform additional validation or cleaning logic.
        """
        cleaned_data = super().clean()

        # Calculate MTBF
        mtbf = calculate_mtbf(cleaned_data['machine_id'])
        cleaned_data['mtbf'] = mtbf

        # Calculate MTTR
        mttr = cleaned_data['duration_hours']
        cleaned_data['mttr'] = mttr

        # Calculate reliability
        reliability = calculate_reliability(mtbf)
        cleaned_data['reliability'] = reliability

        # Calculate availability
        availability = calculate_availability(mtbf, mttr)
        cleaned_data['availability'] = availability

        # Calculate default rate
        default_rate = calculate_default_rate(reliability)
        cleaned_data['default_rate'] = default_rate

        return cleaned_data

def calculate_mtbf(machine_id):
    """
    Calculate the Mean Time Between Failures (MTBF) for a given machine.
    Add your calculation logic here.
    """
    # Placeholder calculation
    mtbf = 1000  # Example value
    return mtbf

def calculate_reliability(mtbf):
    """
    Calculate the reliability for a given MTBF value.
    Add your calculation logic here.
    """
    # Placeholder calculation
    reliability = 0.95  # Example value
    return reliability

def calculate_availability(mtbf, mttr):
    """
    Calculate the availability based on MTBF and MTTR.
    Add your calculation logic here.
    """
    # Placeholder calculation
    availability = mtbf / (mtbf + mttr)  # Example value
    return availability

def calculate_default_rate(reliability):
    """
    Calculate the default rate based on reliability.
    Add your calculation logic here.
    """
    # Placeholder calculation
    default_rate = 1 - reliability  # Example value
    return default_rate
