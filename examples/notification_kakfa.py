{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
from jnpr.healthbot import PINClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'


with PINClient(ip, gui_username, gui_password, port=8080) as pin:
    pin.settings.notification.add(notification_name="sample", description=None, emails=None, microsoft_teams=None,
                                 slack=None, http_post=None, kafka_publish={'bootstrap-servers': ['hbkafka:9094'],
                                                                                  'use-hash-partitioner': False})
    pin.device_group.add(device_group_name="edge", description="All devices on the edge", devices=['demo'],
                        notification={'major': ["sample"], 'minor': ["sample"], 'normal': ["sample"]})

    pin.commit()
    print(pin.settings.notification.get(notification_name="sample"))
    print(pin.device_group.get(device_group_name="edge"))
