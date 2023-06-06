#!/usr/bin/env python3

"""
final_product_form.py
Module for generating the final product form.
"""

from django import forms

class FinalProductForm(forms.Form):
    """
    FinalProductForm class for generating the final product form.
    """

    product_name = forms.CharField(max_length=100)
    product_id = forms.CharField(max_length=50)
    production_date = forms.DateField()
    designation = forms.CharField(max_length=100)
    quantity_in_stock_before = forms.IntegerField(min_value=0)
    quantity_input = forms.IntegerField(min_value=0)
    quantity_output = forms.IntegerField(min_value=0)

    def clean(self):
        """
        Clean method to perform additional validation and calculations.
        """

        cleaned_data = super().clean()
        quantity_in_stock_before = cleaned_data.get('quantity_in_stock_before', 0)
        quantity_input = cleaned_data.get('quantity_input', 0)
        quantity_output = cleaned_data.get('quantity_output', 0)

        remaining_stock = quantity_in_stock_before + quantity_input - quantity_output
        cleaned_data['remaining_stock'] = remaining_stock

        return cleaned_data
