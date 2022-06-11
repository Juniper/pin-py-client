# Settings --> Deployment --> Loadbalancer
# Equivalant to GUI: https://<IP>:8080/deployment-management/deploy

from jnpr.healthbot import PINClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'

with PINClient(ip, gui_username, gui_password, port=8080) as pin:
    # Adding a loadbalancer IP
    pin.settings.deployment.add(ip="1.1.1.1")
    pin.commit()

    # Updating the loadbalancer IP
    pin.settings.deployment.update(ip="1.1.1.2")
    pin.commit()

    # Getting the configured loadbalancer IP
    print(pin.settings.deployment.get())

    # Deleting the configured IP
    pin.settings.deployment.delete()
    pin.commit()
