# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

from jnpr.healthbot import PINClient

# Paragon Automationn GUI credentials
ip = ""
user = ""
pwd = ""
port = '443'


with PINClient(ip=ip, user=user, pwd=pwd, port=port) as pin:
    # Adding managed device to Paragon Automation
    print(pin.device.add(managed=True, host="x.x.x.x", username="device_user", password="device_pwd"))

    # Adding unmanaged device to Paragon Automation
    print(pin.device.add(managed=False, device_id="device_id", host="x.x.x.x", username="device_user", password="device_pwd"))