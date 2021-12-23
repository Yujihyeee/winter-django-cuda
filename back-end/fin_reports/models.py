from dataclasses import dataclass, field
from random import random
import numpy as np
import pandas as pd
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class FinReports(models.Model):
    year = models.IntegerField()
    category = models.TextField()
    price = models.BigIntegerField([MinValueValidator(1), MaxValueValidator(100)])

    class Meta:
        db_table = 'fin_reports'

    def __str__(self):
        return f'[{self.pk}] {self.id}' \
               f'연도: {self.year}' \
               f'항목명: {self.category}' \
               f'금액: {self.price}'


# @dataclass
# class Chart:
#     def __init__(self):
#         pass
#
#     def get_options(self):
#         """
#         the default options that all charts will use
#         """
#         return {}
#
#     def generate_chart_id(self):
#         """
#         returns a randomly generated 8 character ascii string
#         """
#         return ''.join(random.choice(str.ascii_letters) for i in range(8))
#
#     def get_random_colors(num, colors=[]):
#         """
#         function to generate a random hex color list
#         ``num`` the number of colors required
#         ``colors`` the existing color list - additional
#         colors will be added if colors exist
#         """
#         while len(colors) < num:
#             color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
#             if color not in colors:
#                 colors.append(color)
#         return colors
#
#     def get_colors(self):
#         """
#         Get colors from palette.colors or randomly generate a list
#         of colors.  This works great with the palettable module
#         but this is not required and will call get_random_colors
#         if palette.color is not set
#         """
#         try:
#             return palette.hex_colors
#         except:
#             return self.get_random_colors(6)
#
#     """
#     A class for using chart.js charts.
#     ``datasets`` the data itself.  this contains the data and some
#     of the options for the data.  For example, in a stacked bar chart
#     the stack labels.
#     ``labels`` the labels for the data
#     ``chart_id`` is unique chart ID.  A random id will be generated
#     if none s provided.  This needs to be a valid javascript variable
#     name.  Do not use '-'
#     ``palette`` is a list of colors.  The will generate if none
#     are listed
#     """
#     chart_type: str
#     datasets: list = field(default_factory=list)
#     labels: list = field(default_factory=list)
#     chart_id: str = field(default_factory=generate_chart_id)
#     palette: list = field(default_factory=get_colors)
#     options: dict = field(default_factory=get_options)
#
#     def from_lists(self, values, labels, stacks):
#         """
#         function to build a chart from lists
#         ``values`` is a list of datasets. If the chart is not stacked
#         or grouped it will be a list containing one list of the values.
#         For a stack it will be each stack as a different list in the values
#         list.
#         ``labels`` labels are the labels for the individual values
#         ``stacks`` stacks are the labels for each datset in the values
#         list.  This will only contain one value if there are not stacks
#         or groups of data.
#         """
#         self.datasets = []
#
#         # make sure we have the right number of colors
#         if len(self.palette) < len(values):
#             self.get_random_colors(num=len(values), colors=self.palette)
#
#         # build the datasets
#         for i in range(len(stacks)):
#             self.datasets.append(
#                 {
#                     'label': stacks[i],
#                     'backgroundColor': self.palette[i],
#                     'data': values[i],
#                 }
#             )
#
#         if len(values) == 1:
#             self.datasets[0]['backgroundColor'] = self.palette
#
#         self.labels = labels
#
#     def from_df(self, df, values, labels, stacks=None, aggfunc=np.sum, round_values=0, fill_value=0):
#         """
#         function to build a chart from a dataframe
#         ``df`` is the datframe to use
#         ``values`` is the name of the values column
#         ``stacks`` is the name of the stacks column
#         ``labels`` is the name of the labels column
#         ``aggfunc`` is the aggregate function to use to
#          aggregate the values.  Defaults to np.sum
#         ``round_values`` the decimal place to round values to
#         ``fill_value`` is what to use for empty values
#         """
#         pivot = pd.pivot_table(
#             df,
#             values=values,
#             index=stacks,
#             columns=labels,
#             aggfunc=aggfunc,
#             fill_value=0
#         )
#
#         pivot = pivot.round(round_values)
#         values = pivot.values.tolist()
#         labels = pivot.columns.tolist()
#         stacks = pivot.index.tolist()
#         self.from_lists(values, labels, stacks)
#
#     def get_elements(self):
#         """
#         function to record all the chart elements by chart type
#         this is the function to edit to add a new chart type
#         """
#         elements = {
#             'data': {
#                 'labels': self.labels,
#                 'datasets': self.datasets
#             },
#             'options': self.options
#         }
#
#         if self.chart_type == 'stackedBar':
#             elements['type'] = 'bar'
#             self.options['scales'] = {
#                 'xAxes': [
#                     {'stacked': 'true'}
#                 ],
#                 'yAxes': [
#                     {'stacked': 'true'}
#                 ]
#             }
#
#         if self.chart_type == 'bar':
#             elements['type'] = 'bar'
#             self.options['scales'] = {
#                 'xAxes': [
#                     {
#                         'ticks': {
#                             'beginAtZero': 'true'
#                         }
#                     }
#                 ],
#                 'yAxes': [
#                     {
#                         'ticks': {
#                             'beginAtZero': 'true'
#                         }
#                     }
#                 ]
#             }
#
#         if self.chart_type == 'groupedBar':
#             elements['type'] = 'bar'
#             self.options['scales'] = {
#                 'xAxes': [
#                     {
#                         'ticks': {
#                             'beginAtZero': 'true'
#                         }
#                     }
#                 ],
#                 'yAxes': [
#                     {
#                         'ticks': {
#                             'beginAtZero': 'true'
#                         }
#                     }
#                 ]
#             }
#
#         if self.chart_type == 'horizontalBar':
#             elements['type'] = 'horizontalBar'
#             self.options['scales'] = {
#                 'xAxes': [
#                     {
#                         'ticks': {
#                             'beginAtZero': 'true'
#                         }
#                     }
#                 ],
#                 'yAxes': [
#                     {
#                         'ticks': {
#                             'beginAtZero': 'true'
#                         }
#                     }
#                 ]
#             }
#
#         if self.chart_type == 'stackedHorizontalBar':
#             elements['type'] = 'horizontalBar'
#             self.options['scales'] = {
#                 'xAxes': [
#                     {'stacked': 'true'}
#                 ],
#                 'yAxes': [
#                     {'stacked': 'true'}
#                 ]
#             }
#
#         if self.chart_type == 'doughnut':
#             elements['type'] = 'doughnut'
#
#         if self.chart_type == 'polarArea':
#             elements['type'] = 'polarArea'
#
#         if self.chart_type == 'radar':
#             elements['type'] = 'radar'
#
#         return elements
#
#     def get_html(self):
#         code = f'<canvas id="{self.chart_id}"></canvas>'
#         return code
#
#     def get_js(self):
#         code = f"""
#             var chartElement = document.getElementById('{self.chart_id}').getContext('2d');
#             var {self.chart_id}Chart = new Chart(chartElement, {self.get_elements()})
#         """
#         return code
#
#     def get_presentation(self):
#         code = {
#             'html': self.get_html(),
#             'js': self.get_js(),
#         }
#         return code
