from src.api import Api
from src.permission import Permission
from src.person import Person
from src.project import Project
from src.uplink import Uplink

if __name__=="__main__":

    #singup
    user=Api(username="myuser", password="mypassword")
    user.signup()
    print(user._signup)

    #login
    user.login()
    print(user.access_token)
    print(user.headers)

    #update accessToken
    user.renew()
    print(user._renew)

    #login
    pd=Person("pd", "123456")
    pd.api.login()
    print(pd.api.headers)
    print(pd.api.access_token)
    print(pd.api.host)

    connection=pd.api
    print(connection)

    #make new project
    pd.make_new_project(project_name='new', project_description='new')

    #get all user projects
    pd.get_projects(page_size=10, page_number=1)

    #all projects Objs
    print(pd.projects)
    print(pd.projects[0])
    print(pd.projects[0].project_obj)
    print(pd.projects[0].get_info(api=connection))
    print(pd.projects[0]._get_info)

    pd.projects[0].update_info("new name", "new description", connection)
    print(pd.projects[0]._update_info)

    print(pd.projects[0].things)
    print(pd.projects[0].project_obj)
    print(pd.projects[0].project_obj["id"])

    pd.projects[0].new_rule(is_enabled=True, interval=10, trigger=True, script="dsa", api=connection)
    pd.projects[0].get_rule(api=connection)
    print(pd.projects[0]._get_rule)

    pd.projects[0].set_rule_enable(value=True, api=connection)
    print(pd.projects[0]._set_rule_enable)

    pd.projects[0].set_rule_script(value=True, api=connection)
    print(pd.projects[0]._set_rule_script)

    pd.projects[0].set_rule_trigger(value=False, api=connection)
    print(pd.projects[0]._set_rule_trigger)

    pd.projects[0].set_rule_interval(value=False, api=connection)
    print(pd.projects[0]._set_rule_interval)

    pd.projects[0].get_programs(page_number=0, page_size=10, api=connection)
    print(pd.projects[0]._get_programs)

    pd.projects[0].make_new_thing(thing_name="thing", description="desc", api=connection)
    pd.projects[0].get_things(page_number=0, page_size=10, api=connection)
    print(pd.projects[0].things)
    print(pd.projects[0].things[0])
    print(pd.projects[0].things[0].thing_obj)
    print(pd.projects[0].things[0].thing_obj['id'])

    pd.projects[0].things[0].get_info(api=connection)
    print(pd.projects[0].things[0]._get_info)

    pd.projects[0].things[0].set_info(name='name', description='description', api=connection)
    print(pd.projects[0].things[0]._set_info)

    pd.projects[0].things[0].get_location(api=connection)
    print(pd.projects[0].things[0]._get_location)

    pd.projects[0].things[0].set_location(latitude=10, longitude=20, api=connection)
    print(pd.projects[0].things[0]._set_location)

    pd.projects[0].things[0].get_program(api=connection)
    print(pd.projects[0].things[0]._get_program)

    pd.projects[0].things[0].set_program(program_id='000000000000000000000000', api=connection)
    print(pd.projects[0].things[0]._set_program)

    pd.projects[0].things[0].get_sensors(connection)
    print(pd.projects[0].things[0].sensors)

    pd.projects[0].things[0].jwt(api=connection)
    print(pd.projects[0].things[0]._jwt)

    pd.projects[0].things[0].get_jwt_enable(api= connection)
    print(pd.projects[0].things[0]._get_jwt_enable)

    pd.projects[0].things[0].set_jwt_enable(enable=False, api=connection)
    print(pd.projects[0].things[0]._set_jwt_enable)

    pd.projects[0].things[0].get_jwt_settings(api=connection)
    print(pd.projects[0].things[0]._get_jwt_settings)

    # pd.projects[0].things[0].set_jwt_settings(key='123', audience='audience', issuer='issuer', description='description', api=connection)
    # print(pd.projects[0].things[0]._set_jwt_settings)

    # pd.projects[0].things[0].get_jwt_generate(seconds=259200, api=connection)
    # print(pd.projects[0].things[0]._get_jwt_generate)

    pd.projects[0].things[0].get_lorawan(api=connection)
    print(pd.projects[0].things[0]._get_lorawan)

    pd.projects[0].things[0].get_lorawan_abp(api=connection)
    print(pd.projects[0].things[0]._get_lorawan_abp)

    pd.projects[0].things[0].get_lorawan_enable(api=connection)
    print(pd.projects[0].things[0]._get_lorawan_enable)

    pd.projects[0].things[0].set_lorawan_enable(enable=True, api=connection)
    print(pd.projects[0].things[0]._set_lorawan_enable)

    pd.projects[0].things[0].get_lorawan_otaa(api=connection)
    print(pd.projects[0].things[0]._get_lorawan_otaa)

    pd.projects[0].things[0].set_lorawan_otaa(app_key='app_key', app_EUI='app_EUI', api=connection)
    print(pd.projects[0].things[0]._set_lorawan_otaa)

    pd.projects[0].things[0].get_lorawan_abp(api=connection)
    print(pd.projects[0].things[0]._get_lorawan_abp)

    pd.projects[0].things[0].set_lora_abp(app_skey='app_skey', nwk_skey='nwk_skey', dev_addr='dev_addr', api=connection)
    print(pd.projects[0].things[0]._set_lora_abp)

    pd.projects[0].things[0].get_lorawan_deveui(api=connection)
    print(pd.projects[0].things[0]._get_lorawan_deveui)

    pd.projects[0].things[0].set_lorawan_deveui(dev_EUI='dev_EUI', api=connection)
    print(pd.projects[0].things[0]._set_lorawan_deveui)

    pd.projects[0].things[0].get_lorawan_mode(api=connection)
    print(pd.projects[0].things[0]._get_lorawan_mode)

    pd.projects[0].things[0].set_lorawan_mode(mode='mode', api=connection)
    print(pd.projects[0].things[0]._set_lorawan_mode)

    pd.projects[0].things[0].set_lorawan(is_enable=True, is_otaa=True, dev_EUI='0', appSKey='0', nwkSKey='0', dev_addr='0', app_key='0', app_EUI='0', description='description', api=connection)
    print(pd.projects[0].things[0]._set_lorawan)

    pd.projects[0].things[0].get_commands(api=connection)
    print(pd.projects[0].things[0]._get_commands)

    pd.projects[0].things[0].execute_command(api=connection, command_id='479ecf5e-2ed5-4bab-9480-6a6148bc5cad')
    print(pd.projects[0].things[0]._execute_command)

    pd.projects[0].things[0].get_sensor(api=connection, type=3)
    print(pd.projects[0].things[0]._get_sensor)

    pd.projects[0].things[0].set_jwt_settings(key='123', audience='audience', issuer='issuer', description='description', api=connection)
    print(pd.projects[0].things[0]._set_jwt_settings)

    pd.projects[0].things[0].get_jwt_generate(seconds='10000', api=connection)
    print(pd.projects[0].things[0]._get_jwt_generate)
