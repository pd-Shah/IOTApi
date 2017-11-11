import json

from api import Api
from mqtt import MQTT
from permission import Permission
from person import Person
from project import Project
from uplink import Uplink

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

    pd=Person("pd", "123456")
    pd.api.login()
    print(pd.api.headers)
    print(pd.api.access_token)
    print(pd.api.host)

    connection=pd.api

    #make new project
    #pd.make_new_project("new", "new")

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

    # pd.projects[0].make_new_thing(thing_name="thing", description="desc", api=connection)
    pd.projects[0].get_things(page_number=1, page_size=10, api=connection)
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

    pd.projects[0].things[0].get_lora(api=connection)
    print(pd.projects[0].things[0]._get_lora)

    pd.projects[0].things[0].get_lorawan_abp(api=connection)
    print(pd.projects[0].things[0]._get_lorawan_abp)

    # pd.projects[0].things[0].set_lora(is_enable=True, is_otaa=True, dev_EUI='dev_EUI', appSKey='appSKey', nwkSKey='nwkSKey', dev_addr='dev_addr', app_key='12', app_EUI='4', description='description', api=connection)
    # print(pd.projects[0].things[0]._set_lora)

    # pd.projects[0].things[0].set_info(api=connection, name="name", description="des")
    # print(pd.projects[0].things[0]._set_info)
    #
    # pd.projects[0].things[0].get_location(api=connection)
    # print(pd.projects[0].things[0]._get_location)

    # pd.projects[0].things[0].set_location(latitude=12, longitude=20, api=connection)
    # print(pd.projects[0].things[0]._set_location)
    #
    # pd.projects[0].things[0].get_program(api=connection)
    # print(pd.projects[0].things[0]._get_program)
    #
    # pd.projects[0].things[0].set_program(program_id="000000000000000000000000", api=connection)
    # print(pd.projects[0].things[0]._set_program)

    # pd.projects[0].make_new_script(name='name', description='description', script='script', api=connection)
    # print(pd.projects[0]._make_new_script)

    # pd.projects[0].script_validation(param="param", code='code', api=connection)
    # print(pd.projects[0]._script_validation)

    # pd.projects[0].captcha_generate_deletation(api=connection)
    # print(pd.projects[0]._captcha_generate_deletation)

    # pd.projects[0].captcha_generate_modification(api=connection)
    # print(pd.projects[0]._captcha_generate_modification)

    # print(pd.projects[0].things[0].sensors[0].sensor_obj)

    # print(pd.projects[0].things[0].sensors)
    # print(pd.projects[0].things[0].sensors)
    # print(pd.projects[0].things[0].sensors[0].sensor_obj)

    # pd.projects[0].get_permission(connection)
    # print(pd.projects[0].permission)

    # pd.projects[0].delete_project(connection)
    # print(pd.projects[0]._delete)

    # pd.projects[0].things[0].delete_thing(connection)
    # print(pd.projects[0].things[0].delete_thing_state)
