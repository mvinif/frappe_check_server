# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "check_server"
app_title = "check_server"
app_publisher = "Marcos Vinicius Fernandes Machado"
app_description = "Server monitoring module"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = ""
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/devjupiter/css/devjupiter.css"
# app_include_js = "/assets/devjupiter/js/devjupiter.js"

# include js, css files in header of web template
# web_include_css = "/assets/devjupiter/css/devjupiter.css"
# web_include_js = "/assets/devjupiter/js/devjupiter.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "devjupiter.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "devjupiter.install.before_install"
# after_install = "devjupiter.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "devjupiter.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

scheduler_events = {
	"cron":{
		"*/2 * * * *":[
			"devjupiter.api.check_server"
		]
	}
}

