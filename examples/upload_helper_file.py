# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

from jnpr.healthbot import PINClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'


with PINClient(ip, gui_username, gui_password, port=8080) as pin:
    # We can upload rules/playbooks/udf python files (any kind of helper file) 
    file = "/<path>/myrule.rule"
    pin.rule.upload_rule_file(file)
    pin.commit()
