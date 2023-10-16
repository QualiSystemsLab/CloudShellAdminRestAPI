# cloudshell_admin_rest_api 
Python wrapper for CloudShell Administration REST API 

###  Usage:
```
import json

from AdminRestApi import CloudShellAdminApi
from sample_inputs import domain_details, license_pool_details, user_details, edit_user_details

with open('quali_config.json') as f:
    config = json.load(f)
api = CloudShellAdminApi(config)
api.login()

domains = api.get_all_domains()
print('Domains:')
pprint([d.get('Name') for d in domains.get('Domains')])
```
