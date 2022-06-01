def delete_notification_for_device_type(device_type):
    logging.info('Start delete_notification')

    try:
        playbook_instance = PlayBookInstanceBuilder(healthbot_client,
                                                    get_playbook_name(device_type),
                                                    get_playbook_instance_name(device_type),
                                                    get_device_group_name(device_type))
        playbook_instance.delete()
        playbook_instance.apply()
        logging.info(f'delete playbook_instance  {playbook_instance.instance_id}')

    except Exception as exe:
        logging.error('Error', exe)

    try:
        device_group_schema = get_configured_device_group_schema_for_device_type(device_type)
        healthbot_client.device_group.delete(device_group_schema.device_group_name)
        logging.info(f'delete device_group name: {device_group_schema.device_group_name}')
    except Exception as exe:
        logging.error('Error', exe)

    try:
        playbook_schema = get_playbook_schema_for_device_type(device_type)
        healthbot_client.playbook.delete(playbook_schema.playbook_name)
        logging.info(f'delete playbook name: {playbook_schema.playbook_name}')
    except Exception as exe:
        logging.error('Error', exe)

    try:
        device_schema_collection = get_configured_device_schemas_per_device_type().get(device_type)
        for device_schema in device_schema_collection:
            healthbot_client.device.delete(device_schema.device_id)
            logging.info(f'delete device: {device_schema.device_id}')
    except Exception as exe:
        logging.error('Error', exe)

    try:
        rule_schema_collection = get_configured_rule_schemas_per_device_type().get(device_type)
        for rule_schema in rule_schema_collection:
            healthbot_client.rule.delete(get_topic_name(device_type), rule_schema.rule_name)
            logging.info(f'delete rule name: {rule_schema.rule_name}')
    except Exception as exe:
        logging.error('Error', exe)

    healthbot_client.commit()
    logging.info('End delete_notification')


def update_rule(device_type):
    logging.info(f'Start update_rule device_type: {device_type}')

    rule_schema_collection = get_configured_rule_schemas_per_device_type().get(device_type)
    for rule_schema in rule_schema_collection:
        healthbot_client.rule.update(get_topic_name(device_type), schema=rule_schema)
        logging.info(f'update rule name: {rule_schema.rule_name}')
    healthbot_client.commit()
    logging.info('End update_rule')