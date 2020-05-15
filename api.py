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
		
		server_list = frappe.get_all("server_list", fields=["server_name","ip_addr"])
		for server in server_list:
			resp = requests.get(str(server.ipa), verify=False, timeout=1)
			new_doc = frappe.new_doc("server_result")
			new_doc.rname = server.sname
			new_doc.rcode = resp.status_code
			new_doc.rdata = now()
			new_doc.submit()
			frappe.db.commit()

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
""".format(server.sname, resp.status_code, frappe.utils.get_datetime(now()).strftime('%m/%d/%Y %H:%M:%S'))

				frappe.sendmail(recipients=recipients, subject=subject, message=msg, now=True)
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