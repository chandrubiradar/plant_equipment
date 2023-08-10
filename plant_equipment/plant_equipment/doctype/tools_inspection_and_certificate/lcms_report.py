import frappe
import datetime

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

def get_data():
    result = frappe.db.get_list('LCMS Tools Inspection and Certificate',['asset_no','cert_no','tpi','calibration','mpi_report','tpi_expiry','expiry_date','expiry_date1'])


