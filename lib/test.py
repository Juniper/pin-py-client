{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
from jnpr.healthbot import PINClient
from pprint import pprint

# DV
ip = "10.49.104.25"
pwd = "Embe1mpls!"
port = '443'

# # HB
# ip = "10.93.20.153"
# pwd = 'Admin@123'
# port = '8080'


with PINClient(ip, 'admin', pwd, port=port) as pin:
    pprint(pin.device.add("test", "1.1.1.1", "admin", "Admin@123"))
    pprint(pin.device.add("teakwood", "1.1.1.1", "admin", "Admin@123"))
    pin.commit()
    pprint(pin.device.get_ids())
