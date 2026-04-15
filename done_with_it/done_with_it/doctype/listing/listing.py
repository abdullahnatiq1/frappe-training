# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class listing(WebsiteGenerator):
	pass

@frappe.whitelist()
def getSum(price, fullName):

	print(f"\n\n\n{price}\n\n\n")
	print(f"\n\n\n{fullName}\n\n\n")

	return price
