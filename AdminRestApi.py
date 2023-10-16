import json

import requests


class CloudShellAdminApi:
    def __init__(self, configuration: dict) -> None:
        self.server = configuration.get('server_name')
        self.port = configuration.get('server_port')
        self.username = configuration.get('username')
        self.password = configuration.get('password')
        self.domain = configuration.get('domain')
        self.server_address = f'http://{self.server}:{self.port}'
        self.headers = {'Content-Type': 'application/json'}
        self.auth_code = None

    def _request_and_parse(self, request_type: str, url_str: str, json_dict: dict = None, data_dict: dict = None):
        """

        :param request_type:
        :param url_str:
        :param json_dict:
        :param data_dict:
        :return:
        """

        response = ''
        if request_type.lower() == 'put':
            response = requests.put(url_str, json=json_dict, headers=self.headers)

        elif request_type.lower() == 'get':
            response = requests.get(url_str, json=json_dict, headers=self.headers)

        elif request_type.lower() == 'post':
            if data_dict:
                response = requests.post(url_str, json=json_dict, headers=self.headers, data=json.dumps(data_dict))
            else:
                response = requests.post(url_str, json=json_dict, headers=self.headers)
        elif request_type.lower() == 'delete':
            response = requests.delete(url_str, headers=self.headers)

        if not response.ok:
            raise Exception(
                f'Error code: {response.status_code}\n'
                f'Error text: {json.loads(response.text)["message"]}\n'
                f'{url_str} '
                f'failed, exiting')
        return response

    def login(self):
        """Login and set some internal variables
        """
        url_str = f'{self.server_address}/Api/Auth/Login'
        json_dict = {'username': self.username, 'password': self.password, 'domain': self.domain}
        response = self._request_and_parse('put', url_str, json_dict)
        self.auth_code = f'Basic {response.content[1:-1].decode()}'
        self.headers = {"Authorization": self.auth_code, "Content-Type": "application/json"}

    def get_all_domains(self):
        url = f'{self.server_address}/api/v1/domains'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print('Failed to get all domains')
        return json.loads(response.content)

    def get_domain_id(self, domain_name):
        all_domains = self.get_all_domains()
        domain_id = [d.get('Id') for d in all_domains.get('Domains') if d.get('Name') == domain_name][0]
        return domain_id

    def get_domain_by_id(self, domain_id):
        url = f'{self.server_address}/api/v1/domains/{domain_id}'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print(f'Failed to get domain details for {domain_id}')
        return json.loads(response.content)

    def create_domain(self, domain_details):
        url = f'{self.server_address}/api/v1/domains'
        response = self._request_and_parse('post', url, json_dict=domain_details)
        if not response.ok:
            print('Failed to get all domains')
        return json.loads(response.content)

    def edit_domain(self, domain_id, domain_details):
        url = f'{self.server_address}/api/v1/domains/{domain_id}'
        response = self._request_and_parse('put', url, json_dict=domain_details)
        if not response.ok:
            print(f'Failed to get edit domain for {domain_id}')
            return False
        return response.ok

    def delete_domain(self, domain_id):
        url = f'{self.server_address}/api/v1/domains/{domain_id}'
        response = self._request_and_parse('delete', url)
        if not response.ok:
            print(f'Failed to get domain details for {domain_id}')
            return False
        return response.ok

    def get_domain_blueprints(self, domain_id):
        url = f'{self.server_address}/api/v1/domains/{domain_id}/blueprints'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print(f'Failed to get blueprints for {domain_id}')
        return json.loads(response.content)

    def get_domain_groups(self, domain_id):
        url = f'{self.server_address}/api/v1/domains/{domain_id}/groups'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print(f'Failed to get domain groups for {domain_id}')
        return json.loads(response.content)

    def get_all_groups(self):
        url = f'{self.server_address}/api/v1/groups'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print('Failed to get all groups')
        return json.loads(response.content)

    def get_group_id(self, group_name):
        all_groups = self.get_all_groups()
        group_id = [g.get('Id') for g in all_groups.get('Groups') if g.get('Name') == group_name][0]
        return group_id

    def get_groups_users(self, group_id):
        url = f'{self.server_address}/api/v1/groups/{group_id}/Users'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print('Failed to get all groups')
        return json.loads(response.content)

    def get_all_users(self):
        url = f'{self.server_address}/api/v1/users'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print('Failed to get all users')
        return json.loads(response.content)

    def get_user_id(self, username):
        all_users = self.get_all_users()
        user_id = [u.get('Id') for u in all_users.get('Users') if u.get('Username') == username][0]
        return user_id

    def create_user(self, user_details):
        url = f'{self.server_address}/api/v1/users'
        response = self._request_and_parse('post', url, user_details)
        if not response.ok:
            print('Failed to create new user')
        return json.loads(response.content)

    def edit_user(self, user_id, user_details):
        url = f'{self.server_address}/api/v1/users/{user_id}'
        response = self._request_and_parse('put', url, user_details)
        if not response.ok:
            print(f'Failed to edit edit user {user_details.get("Username")}')
        return response.ok

    def delete_user(self, user_id):
        url = f'{self.server_address}/api/v1/users/{user_id}'
        response = self._request_and_parse('delete', url)
        if not response.ok:
            print(f'Failed to get delete user {user_id}')
        return response.ok

    def get_all_license_pools(self):
        url = f'{self.server_address}/api/v1/licensepools'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print('Failed to get all license pools')
        return json.loads(response.content)

    def get_license_pool_id(self, pool_name):
        license_pools = self.get_all_license_pools()
        license_pool_id = [lp.get('Id') for lp in license_pools.get('LicensePools') if lp.get('Name') == pool_name][0]
        return license_pool_id

    def get_license_pool_by_id(self, pool_id):
        url = f'{self.server_address}/api/v1/licensepools/{pool_id}'
        response = self._request_and_parse('get', url)
        if not response.ok:
            print(f'Failed to get all license pool for {pool_id}')
        return json.loads(response.content)

    def create_license_pool(self, pool_details):
        url = f'{self.server_address}/api/v1/licensepools'
        response = self._request_and_parse('post', url, pool_details)
        if not response.ok:
            print(f'Failed to get create license pool {pool_details.get("Name")}')
        return json.loads(response.content)

    def edit_license_pool(self, license_pool_id, pool_details):
        url = f'{self.server_address}/api/v1/licensepools/{license_pool_id}'
        response = self._request_and_parse('put', url, pool_details)
        if not response.ok:
            print(f'Failed to get edit license pool {pool_details.get("Name")}')
        return response.ok

    def delete_license_pool(self, license_pool_id):
        url = f'{self.server_address}/api/v1/licensepools/{license_pool_id}'
        response = self._request_and_parse('delete', url)
        if not response.ok:
            print(f'Failed to get delete license pool {license_pool_id}')
        return response.ok
