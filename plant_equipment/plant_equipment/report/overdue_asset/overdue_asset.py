# Copyright (c) 2023, Chandru and contributors
# For license information, please see license.txt

# import frappe


from __future__ import unicode_literals
from frappe import _
import frappe
import datetime

def execute(filters=None):
    return get_columns(),get_data(filters)

def get_data(filters):
    conditions = "1"
    print(conditions)
    if(filters.get('asset_no')):conditions =conditions+ f" AND asset_no ='{filters.get('asset_no')}'"
    data = frappe.db.sql(f"SELECT asset_no,cert_no,tpi,tpi_expiry,calibration,expiry_date,mpi_report,expiry_date1 from `tabLCMS Tools Inspection and Certificate` ",as_dict=1)


def get_columns():
    return[
            {
                "fieldname": "asset_no",
                "label": _("Asset No"),
                "fieldtype": "Data",
                "width": 300
            },
            {
                "fieldname": "cert_no",
                "label": _("Certificate No."),
                "fieldtype": "Data",
                "width": 300
            },
            {
                "fieldname": "TPI",
                "label": _("tpi"),
                "fieldtype": "Select",
                "width": 100
            },
            {
                "fieldname": "TPI Expiry",
                "label": _("tpi_expiry"),
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
                "fieldname": "expiry_date",
                "label": _("CALIBRATION Expiry"),
                "fieldtype": "Date",
                "width": 100
            },
            {
                "fieldname": "mpi_report",
                "label": _("MPI Report"),
                "fieldtype": "Select",
                "width": 100
            },
            {
                "fieldname": "expiry_date1",
                "label": _("MPI Report Expiry"),
                "fieldtype": "Date",
                "width": 100
            }
          ]
