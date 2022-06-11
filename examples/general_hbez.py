from jnpr.healthbot import PINClient
from pprint import pprint
from jnpr.healthbot import DeviceGroupSchema

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'

with PINClient(ip, gui_username, gui_password, port=8080) as pin:

    print(pin.version)
    pprint(pin.device.get_ids())
    pprint(pin.device_group.get())

    # Handling devices
    pprint(pin.device.get_ids())
    pprint(pin.device.add("test", "1.1.1.1", "admin", "Admin@123"))
    pprint(pin.device.add("teakwood", "1.1.1.1", "admin", "Admin@123"))
    pin.commit()
    pprint(pin.device.get_ids())
    pprint(pin.device.delete("test"))
    pin.commit()
    pprint(pin.device.get_ids())
    pprint(pin.device.get('test'))

    schemaObj = pin.device.get('test')
    schemaObj.description = 'changed description'
    pin.device.update(schemaObj)
    pprint(pin.device.get('test'))
    pprint(pin.device.get_facts())
    pprint(pin.device.health('test'))
    pprint(pin.device.health('svl1r'))

    # Handling device-groups
    pprint(pin.device_group.get())
    dgs = DeviceGroupSchema(device_group_name="edge",
                            description="All devices on the edge",
                            devices=['test'])
    pin.device_group.add(dgs)
    pin.commit()
    pprint(pin.device_group.get("edge"))
    pin.device_group.delete("egde")
    pin.commit()
    pprint(pin.device_group.get("edge"))

    dgs = pin.device_group.get('edge')
    dgs.devices.append("teakwood")
    pin.device_group.update(dgs)
    pin.commit()
    print(pin.device_group.get('edge'))

    dgs = pin.device_group.get('edge')
    dgs.devices.remove("teakwood")
    pin.device_group.update(dgs)
    pin.commit()
    print(pin.device_group.get('edge'))

    # Handling playbooks
    pprint(pin.playbook.get())
    pprint(pin.playbook.get('linecard-kpis-playbook'))

    pprint(pin.rule.get('linecard.ospf', 'check-ddos-statistics'))







