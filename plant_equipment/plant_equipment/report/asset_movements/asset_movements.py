# Copyright (c) 2023, Chandru and contributors
# For license information, please see license.txt

# import frappe

from __future__ import unicode_literals
from frappe import _
import frappe
import datetime
from frappe.utils import today
from datetime import date, timedelta
import json

def execute(filters=None):
	return get_columns(),get_data(filters)

def get_columns():
    return[
             {
		"fieldname": "name",
		"label": _("Name"),
		"fieldtype": "Data",
		"width": 200
	     },
             {  
		"fieldname": "contract",
		"label": _("Contract"),
		"fieldtype": "Link",
		"options":"Contract",
		"width": 200
	     },
	     {
		"fieldname": "purpose",
		"label": _("Purpose"),
		"fieldtype": "Select",
		"options":['Issue','Receipt','Transfer'],
		"width": 200
	     },
	     {
		"fieldname": "transaction_date",
		"label": _("Transaction Date"),
		"fieldtype": "Date",
		"width": 200
	     },
             {
		"fieldname": "asset_return_date",
		"label": _("Asset Return Date"),
		"fieldtype": "Date",
		"width": 200
	     },

	     {
		"fieldname": "permanent_transfer",
		"label": _("Permanent Transfer"),
		"fieldtype": "Check",
		"width": 200
	     },
	     {
		"fieldname": "temporarily_transfer",
		"label": _("Temporarily Transfer"),
		"fieldtype": "Check",
		"width": 200
	     },

             {
		"fieldname": "asset",
		"label": _("Asset"),
		"fieldtype": "Data",
		"width": 200
	     },
             {
		"fieldname": "source_location",
		"label": _("Source Location"),
		"fieldtype": "Link",
		"options":"Location",
		"width": 200
	    },
            {
		"fieldname": "from_employee",
		"label": _("From Employee"),
		"fieldtype": "Link",
		"options":"Employee",
		"width": 200
	    },

	    {  
		"fieldname": "target_location",
		"label": _("Target Location"),
		"fieldtype": "Link",
		"options":"Location",
		"width": 200
	    },
            {
		"fieldname": "to_employee",
		"label": _("To Employee"),
		"fieldtype": "Link",
		"options":"Employee",
		"width": 200
	    },
        ]

def get_data(filters):
    result = frappe.db.sql(f"SELECT am.name,am.contract,am.purpose,am.transaction_Date,am.asset_return_date,am.permanent_transfer,am.temporarily_tranfer,aet.asset,aet.source_location,aet.from_employee,aet.target_location,aet.to_employee,aet.asset_name,alt.asset,alt.source_location,alt.from_employee,alt.target_location,alt.to_employee,alt.asset_name,att.asset,att.source_location,att.from_employee,att.target_location,att.to_employee,att.asset_name,act.asset,act.source_location,act.from_employee,act.target_location,act.to_employee,act.asset_name from `tabAsset movement Mashhor` as am left join `tabAsset Movement Equipment Table` as aet on am.name=aet.parent left join `tabAsset Movement Light Vehicle Table` as alt  on am.name=alt.parent left join `tabAsset Movement Tools Table` as att on am.name=att.parent left join `tabAsset Movement Consumables Table` as act on am.name=act.parent WHERE am.asset_return_date != '' and am.purpose = 'Transfer' and am.asset_return_date <now() and am.asset_return_date != now() ")
    return result

