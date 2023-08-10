# Copyright (c) 2023, Chandru and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
from frappe import _
import frappe
import datetime
from datetime import date, timedelta
import json

def execute(filters=None):
    return get_columns(),get_data(filters)

def get_columns():
    return[
        {
                "fieldname": "asset_no",
                "label": _("Asset No"),
                "fieldtype": "Data",
                "width": 300
            },
            {
                "fieldname": "tpi",
                "label": _("TPI"),
                "fieldtype": "Select",
                "width": 100
            },
            {
                "fieldname": "tpi_certificate_no",
                "label": _("TPI Certificate No"),
                "fieldtype": "Data",
                "width": 100
            },
            {
                "fieldname": "tpi_expiry",
                "label": _("TPI Expiry"),
                "fieldtype": "Date",
                "width": 100
            },
            {
                "fieldname": "calibration",
                "label": _("CALIBRATION"),
                "fieldtype": "Select",
                "width": 100
            },
            {
                "fieldname": "calibration_certificate_no",
                "label": _("CALIBRATION Certification No"),
                "fieldtype": "Data",
                "width": 100
            },
            {
                "fieldname": "expiry_date",
                "label": _("CALIBRATION Expiry"),
                "fieldtype": "Date",
                "width": 100
            },
            {
                "fieldname": "mpi_report",
                "label": _("MPI Report"),
                "fieldtype": "Data",
                "width": 100
            },
            {
                "fieldname": "mpi_certificate_no",
                "label": _("MPI Certificate No"),
                "fieldtype": "Data",
                "width": 100
            }
          ]

def get_data(filters):
    conditions = "1"
    print(conditions)
    if(filters.get('asset_no')):conditions =conditions+ f" AND asset_no ='{filters.get('asset_no')}'"
    data = frappe.db.get_all('Tools Inspection and Certificate',fields=['asset_no','tpi','tpi_certificate_no','tpi_expiry','calibration','calibration_certificate_no','expiry_date','mpi_report','mpi_certificate_no'])
    return data
