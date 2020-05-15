
# Server verification in Frappe/ERPNext

This method send a simple request to a server ip, with response code this method keep monitoring the servers list and mailing the teams in any exception or server unavaible

## Usage
To ideal usage of this method, firstly we need to create:

 - Frappe doc **server_list**, containing:
   - server_name
   - ip_address
 - Frappe doc **server_result**, containing:
   - resp_server_name
   - resp_code
   - resp_date
 - Setup a default outgoing email account in Frappe configuration
 - Setup hook.py file
 
 ## Functionality
 Each server registered in **server_list**, is monitored every X times *(defined in __hook.py__ cron),* each result is saved in **server_result**, if any server is unavaible or method enter in a exception, the method send a e-mail notification to responsible team
