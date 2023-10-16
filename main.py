import json

from AdminRestApi import CloudShellAdminApi
from sample_inputs import domain_details, license_pool_details, user_details, edit_user_details

if __name__ == '__main__':
    with open('quali_config.json') as f:
        config = json.load(f)
    api = CloudShellAdminApi(config)
    api.login()
    #
    # domains = api.get_all_domains()
    # print('Domains:')
    # pprint([d.get('Name') for d in domains.get('Domains')])
    #
    # global_domain_id = api.get_domain_id('Global')
    #
    # print('Global Domain from Id:')
    # pprint(api.get_domain_by_id(global_domain_id))
    #
    # print('Global Domain blueprints:')
    # pprint([b.get('Name') for b in api.get_domain_blueprints(global_domain_id).get('Blueprints')])
    #
    # print('Groups in Global Domain')
    # pprint([g.get('Name') for g in api.get_domain_groups(global_domain_id).get('Groups')])
    #
    # groups = api.get_all_groups()
    # print('Groups:')
    # pprint([g.get('Name') for g in groups.get('Groups')])
    #
    # sys_admin_group_id = api.get_group_id('System Administrators')
    #
    # print('Sys admin group users:')
    # pprint([u.get('Username') for u in api.get_groups_users(sys_admin_group_id).get('Users')])
    #
    # users = api.get_all_users()
    # print('Users:')
    # pprint([u.get('Username') for u in users.get('Users')])
    #
    # license_pools = api.get_all_license_pools()
    # print('License Pools:')
    # pprint(license_pools)
    # pprint([lp.get('Username') for lp in license_pools.get('LicensePools')])
    #
    # license_pool1_id = api.get_license_pool_id('Pool_1')
    #
    # print('License Pool Pool_1:')
    # pprint(api.get_license_pool_by_id(license_pool1_id))

    # # Create and delete domain
    # print('Creating new domain:')
    # new_domain = api.create_domain(domain_details)
    # print(f'New domain: {new_domain}')
    #
    # new_domain_id = api.get_domain_id('API Created Domain')
    # print('Editing new domain:')
    # print(api.edit_domain(new_domain_id, domain_details))
    #
    # print('Deleting new domain:')
    # print(api.delete_domain(new_domain_id))
    #
    # # Create and delete license pool
    # print('Creating new license pool:')
    # new_license_pool = api.create_license_pool(license_pool_details)
    # print(f'New License Pool: {new_license_pool}')
    #
    # new_license_pool_id = api.get_license_pool_id('My License Pool')
    # print('Editing new license pool:')
    # print(api.edit_license_pool(new_license_pool_id, license_pool_details))
    #
    # print('Deleting new license pool:')
    # print(api.delete_license_pool(new_license_pool_id))

    # Create and delete Users
    print('Creating new user:')
    new_user = api.create_user(user_details)
    print(f'New User: {new_user}')

    new_user_id = api.get_user_id('NewUser')
    print('Editing new user:')
    print(api.edit_user(new_user_id, edit_user_details))

    print('Deleting new user:')
    print(api.delete_user(new_user_id))
