// Copyright (c) 2023, Chandru and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Certification Pending"] = {
	"filters": [
		{
                "fieldname": "asset_no",
                "label": __("Asset No"),
                "fieldtype": "Data",
                "width": 300
            },
            {
                "fieldname": "cert_no",
                "label": __("Certificate No."),
                "fieldtype": "Data",
                "width": 300
            },		

	]
};
