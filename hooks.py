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

scheduler_events = {
	"cron":{
		"*/15 * * * *":[
			"monitoring.main.check_server"
		]
	}
}

