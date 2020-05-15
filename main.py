from __future__ import unicode_literals
import frappe
import frappe.defaults
from frappe.utils import nowdate, cstr, flt, cint, now ,getdate
from frappe import throw, _
from frappe.utils import formatdate, get_number_format_info
import requests
import json
import datetime

@frappe.whitelist()
def check_server():
	try:
		# read server_list doc, which have a list of values (server name and ip address)
		server_list = frappe.get_all("server_list", fields=["server_name","ip_address"])

		for server in server_list:

			# verify response for each server in list
			resp = requests.get(str(server.ip_address), verify=False, timeout=1)

			# create new doc named server_result, which keep the verification data
			new_doc = frappe.new_doc("server_result")
			new_doc.resp_server_name = server.server_name
			new_doc.resp_code = resp.status_code
			new_doc.resp_data = now()

			# save server_result and commit in database
			new_doc.submit()
			frappe.db.commit()

			# if server is unavailibre, notify the email team
			if resp.status_code >= 400:
				recipients = "company@email.com"
				subject = "[Alert] Server monitoring"
				msg ="""
<h2>Server unavailable</h2>
<h3>Status:</h3>
<br>
<strong>Server:</strong> {}<br>
<strong>Return code:</strong> {}<br>
<strong>Date:</strong> {}<br>
""".format(server.server_name, resp.status_code, frappe.utils.get_datetime(now()).strftime('%m/%d/%Y %H:%M:%S'))

				frappe.sendmail(recipients=recipients, subject=subject, message=msg, now=True)

			# if method enter in a exception, notify the team to analyze
	except Exception as e:
		recipients = "company@email.com"
		subject = "[Exception Report] Exception in server monitoring process"
		msg = """
<h2>Exception report:</h2>
<strong>Method check_server return a exception</strong>
<p>Return data:</p>
<pre> {} </pre>
""".format(e)
		frappe.sendmail(recipients=recipients, subject=subject, message=msg, now=True)
		pass