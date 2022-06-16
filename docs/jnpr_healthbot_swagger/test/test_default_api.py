{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_backup_helper_files(self):
        """Test case for backup_helper_files

        Download the tar file containing all helper files.  # noqa: E501
        """
        pass

    def test_create_files_certificates_by_file_name(self):
        """Test case for create_files_certificates_by_file_name

        Upload a certificate file.  # noqa: E501
        """
        pass

    def test_create_files_helper_files_by_file_name(self):
        """Test case for create_files_helper_files_by_file_name

        Upload a helper-file.  # noqa: E501
        """
        pass

    def test_create_healthbot_ingest_settings_byoi_custom_plugin_by_id(self):
        """Test case for create_healthbot_ingest_settings_byoi_custom_plugin_by_id

        Create custom-plugin by ID  # noqa: E501
        """
        pass

    def test_create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(self):
        """Test case for create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id

        Create tlive-kafka-oc by ID  # noqa: E501
        """
        pass

    def test_create_healthbot_ingest_settings_byoi_ingest_mapping_by_id(self):
        """Test case for create_healthbot_ingest_settings_byoi_ingest_mapping_by_id

        Create ingest-mapping by ID  # noqa: E501
        """
        pass

    def test_create_healthbot_ingest_settings_frequency_profile_by_id(self):
        """Test case for create_healthbot_ingest_settings_frequency_profile_by_id

        Create frequency-profile by ID  # noqa: E501
        """
        pass

    def test_create_healthbot_system_time_series_database_time_series_database_by_id(self):
        """Test case for create_healthbot_system_time_series_database_time_series_database_by_id

        Create time-series-database by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_ingest_settings(self):
        """Test case for create_iceberg_ingest_settings

        Create ingest-settings by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_ingest_settings_flow(self):
        """Test case for create_iceberg_ingest_settings_flow

        Create flow by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_ingest_settings_flow_template_by_id(self):
        """Test case for create_iceberg_ingest_settings_flow_template_by_id

        Create template by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_ingest_settings_syslog(self):
        """Test case for create_iceberg_ingest_settings_syslog

        Create syslog by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_ingest_settings_syslog_pattern_by_id(self):
        """Test case for create_iceberg_ingest_settings_syslog_pattern_by_id

        Create pattern by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_ingest_settings_syslog_pattern_set_by_id(self):
        """Test case for create_iceberg_ingest_settings_syslog_pattern_set_by_id

        Create pattern-set by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_profile_data_summarization_raw_by_id(self):
        """Test case for create_iceberg_profile_data_summarization_raw_by_id

        Create raw-data-summarization by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_profile_security_ca_profile_by_id(self):
        """Test case for create_iceberg_profile_security_ca_profile_by_id

        Create ca-profile by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_profile_security_local_certificate_by_id(self):
        """Test case for create_iceberg_profile_security_local_certificate_by_id

        Create local-certificate by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_profile_security_ssh_key_profile_by_id(self):
        """Test case for create_iceberg_profile_security_ssh_key_profile_by_id

        Create ssh-key-profile by ID  # noqa: E501
        """
        pass

    def test_create_iceberg_profiles(self):
        """Test case for create_iceberg_profiles

        Create profile by ID  # noqa: E501
        """
        pass

    def test_delete_files_certificates_by_file_name(self):
        """Test case for delete_files_certificates_by_file_name

        Delete a certificate-file.  # noqa: E501
        """
        pass

    def test_delete_files_helper_files_by_file_name(self):
        """Test case for delete_files_helper_files_by_file_name

        Delete a helper-file.  # noqa: E501
        """
        pass

    def test_delete_healthbot_ingest_settings_byoi_custom_plugin_by_id(self):
        """Test case for delete_healthbot_ingest_settings_byoi_custom_plugin_by_id

        Delete custom-plugin by ID  # noqa: E501
        """
        pass

    def test_delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(self):
        """Test case for delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id

        Delete tlive-kafka-oc by ID  # noqa: E501
        """
        pass

    def test_delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id(self):
        """Test case for delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id

        Delete ingest-mapping by ID  # noqa: E501
        """
        pass

    def test_delete_healthbot_ingest_settings_frequency_profile_by_id(self):
        """Test case for delete_healthbot_ingest_settings_frequency_profile_by_id

        Delete frequency-profile by ID  # noqa: E501
        """
        pass

    def test_delete_healthbot_system_time_series_database_time_series_database_by_id(self):
        """Test case for delete_healthbot_system_time_series_database_time_series_database_by_id

        Delete time-series-database  # noqa: E501
        """
        pass

    def test_delete_iceberg_ingest_settings(self):
        """Test case for delete_iceberg_ingest_settings

        Delete ingest-settings by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_ingest_settings_flow(self):
        """Test case for delete_iceberg_ingest_settings_flow

        Delete flow by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_ingest_settings_flow_template_by_id(self):
        """Test case for delete_iceberg_ingest_settings_flow_template_by_id

        Delete template by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_ingest_settings_syslog(self):
        """Test case for delete_iceberg_ingest_settings_syslog

        Delete syslog by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_ingest_settings_syslog_pattern_by_id(self):
        """Test case for delete_iceberg_ingest_settings_syslog_pattern_by_id

        Delete pattern by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_ingest_settings_syslog_pattern_set_by_id(self):
        """Test case for delete_iceberg_ingest_settings_syslog_pattern_set_by_id

        Delete pattern-set by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_profile_data_summarization_raw_by_id(self):
        """Test case for delete_iceberg_profile_data_summarization_raw_by_id

        Delete raw-data-summarization by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_profile_security_ca_profile_by_id(self):
        """Test case for delete_iceberg_profile_security_ca_profile_by_id

        Delete ca-profile by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_profile_security_local_certificate_by_id(self):
        """Test case for delete_iceberg_profile_security_local_certificate_by_id

        Delete local-certificate by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_profile_security_ssh_key_profile_by_id(self):
        """Test case for delete_iceberg_profile_security_ssh_key_profile_by_id

        Delete ssh-key-profile by ID  # noqa: E501
        """
        pass

    def test_delete_iceberg_profiles(self):
        """Test case for delete_iceberg_profiles

        Delete profile by ID  # noqa: E501
        """
        pass

    def test_inspect_command_rpc_table_on_device(self):
        """Test case for inspect_command_rpc_table_on_device

        Inspect the given iAgent table.  # noqa: E501
        """
        pass

    def test_restore_helper_files(self):
        """Test case for restore_helper_files

        Upload a helper-file.  # noqa: E501
        """
        pass

    def test_retrieve_configuration_jobs(self):
        """Test case for retrieve_configuration_jobs

        """
        pass

    def test_retrieve_data_database_table(self):
        """Test case for retrieve_data_database_table

        Get information about tables for a device of a device-group.  # noqa: E501
        """
        pass

    def test_retrieve_data_database_table_column_by_table_name(self):
        """Test case for retrieve_data_database_table_column_by_table_name

        Get information about columns in a table.  # noqa: E501
        """
        pass

    def test_retrieve_data_database_tags_by_table_name(self):
        """Test case for retrieve_data_database_tags_by_table_name

        Get information about tags keys and values in a table.  # noqa: E501
        """
        pass

    def test_retrieve_debug_jobs(self):
        """Test case for retrieve_debug_jobs

        """
        pass

    def test_retrieve_event(self):
        """Test case for retrieve_event

        Get all events for a device.  # noqa: E501
        """
        pass

    def test_retrieve_event_by_event_name(self):
        """Test case for retrieve_event_by_event_name

        Get instances of a device event.  # noqa: E501
        """
        pass

    def test_retrieve_event_by_event_name_device_group(self):
        """Test case for retrieve_event_by_event_name_device_group

        Get instances of a device-group event.  # noqa: E501
        """
        pass

    def test_retrieve_event_by_event_name_network_group(self):
        """Test case for retrieve_event_by_event_name_network_group

        Get instances of a network-group event.  # noqa: E501
        """
        pass

    def test_retrieve_event_device_group(self):
        """Test case for retrieve_event_device_group

        Get all events for a device-group.  # noqa: E501
        """
        pass

    def test_retrieve_event_network_group(self):
        """Test case for retrieve_event_network_group

        Get all events for a network-group.  # noqa: E501
        """
        pass

    def test_retrieve_events(self):
        """Test case for retrieve_events

        Get all events.  # noqa: E501
        """
        pass

    def test_retrieve_files_certificates_by_file_name(self):
        """Test case for retrieve_files_certificates_by_file_name

        Download a certificate-file.  # noqa: E501
        """
        pass

    def test_retrieve_files_helper_files(self):
        """Test case for retrieve_files_helper_files

        Get all helper-file names.  # noqa: E501
        """
        pass

    def test_retrieve_files_helper_files_by_file_name(self):
        """Test case for retrieve_files_helper_files_by_file_name

        Download a helper-file.  # noqa: E501
        """
        pass

    def test_retrieve_health_all(self):
        """Test case for retrieve_health_all

        Return a dict with health of devices in device groups and network groups  # noqa: E501
        """
        pass

    def test_retrieve_health_tree_by_device_group(self):
        """Test case for retrieve_health_tree_by_device_group

        Get device-group health-tree.  # noqa: E501
        """
        pass

    def test_retrieve_health_tree_by_id(self):
        """Test case for retrieve_health_tree_by_id

        Return a device's health-tree.  # noqa: E501
        """
        pass

    def test_retrieve_health_tree_by_network_group(self):
        """Test case for retrieve_health_tree_by_network_group

        Get network-group health-tree.  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id(self):
        """Test case for retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id

        Retrieve custom-plugin by ID  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_byoi_custom_plugins(self):
        """Test case for retrieve_healthbot_ingest_settings_byoi_custom_plugins

        Retrieve custom-plugin by ID  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(self):
        """Test case for retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id

        Retrieve tlive-kafka-oc by ID  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas(self):
        """Test case for retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas

        Retrieve tlive-kafka-oc  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id(self):
        """Test case for retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id

        Retrieve ingest-mapping by ID  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_byoi_ingest_mappings(self):
        """Test case for retrieve_healthbot_ingest_settings_byoi_ingest_mappings

        Retrieve ingest-mapping  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_frequency_profile(self):
        """Test case for retrieve_healthbot_ingest_settings_frequency_profile

        Retrieve frequency-profile  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_ingest_settings_frequency_profile_by_id(self):
        """Test case for retrieve_healthbot_ingest_settings_frequency_profile_by_id

        Retrieve frequency-profile by ID  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_system_time_series_database_time_series_database(self):
        """Test case for retrieve_healthbot_system_time_series_database_time_series_database

        Retrieve time-series-database  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings(self):
        """Test case for retrieve_iceberg_ingest_settings

        Retrieve ingest-settings  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_flow(self):
        """Test case for retrieve_iceberg_ingest_settings_flow

        Retrieve flow  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_flow_template_by_id(self):
        """Test case for retrieve_iceberg_ingest_settings_flow_template_by_id

        Retrieve template by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_flow_template_ids(self):
        """Test case for retrieve_iceberg_ingest_settings_flow_template_ids

        Retrieve template  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_syslog(self):
        """Test case for retrieve_iceberg_ingest_settings_syslog

        Retrieve syslog  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_syslog_pattern_by_id(self):
        """Test case for retrieve_iceberg_ingest_settings_syslog_pattern_by_id

        Retrieve pattern by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_syslog_pattern_ids(self):
        """Test case for retrieve_iceberg_ingest_settings_syslog_pattern_ids

        Retrieve pattern  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id(self):
        """Test case for retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id

        Retrieve pattern-set by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_syslog_pattern_set_ids(self):
        """Test case for retrieve_iceberg_ingest_settings_syslog_pattern_set_ids

        Retrieve pattern-set  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_syslog_pattern_sets(self):
        """Test case for retrieve_iceberg_ingest_settings_syslog_pattern_sets

        Retrieve pattern-set by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_ingest_settings_syslog_patterns(self):
        """Test case for retrieve_iceberg_ingest_settings_syslog_patterns

        Retrieve pattern by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_data_summarization_raw_by_id(self):
        """Test case for retrieve_iceberg_profile_data_summarization_raw_by_id

        Retrieve raw-data-summarization by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_data_summarizations_raw(self):
        """Test case for retrieve_iceberg_profile_data_summarizations_raw

        Retrieve raw-data-summarization  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_security_ca_profile_by_id(self):
        """Test case for retrieve_iceberg_profile_security_ca_profile_by_id

        Retrieve ca-profile by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_security_ca_profiles(self):
        """Test case for retrieve_iceberg_profile_security_ca_profiles

        Retrieve ca-profile  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_security_local_certificate_by_id(self):
        """Test case for retrieve_iceberg_profile_security_local_certificate_by_id

        Retrieve local-certificate by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_security_local_certificates(self):
        """Test case for retrieve_iceberg_profile_security_local_certificates

        Retrieve local-certificate  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_security_ssh_key_profile_by_id(self):
        """Test case for retrieve_iceberg_profile_security_ssh_key_profile_by_id

        Retrieve ssh-key-profile by ID  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profile_security_ssh_key_profiles(self):
        """Test case for retrieve_iceberg_profile_security_ssh_key_profiles

        Retrieve ssh-key-profile  # noqa: E501
        """
        pass

    def test_retrieve_iceberg_profiles(self):
        """Test case for retrieve_iceberg_profiles

        Retrieve profile  # noqa: E501
        """
        pass

    def test_retrieve_sensors(self):
        """Test case for retrieve_sensors

        List all OpenConfig sensors.  # noqa: E501
        """
        pass

    def test_update_healthbot_ingest_settings_byoi_custom_plugin_by_id(self):
        """Test case for update_healthbot_ingest_settings_byoi_custom_plugin_by_id

        Update custom-plugin by ID  # noqa: E501
        """
        pass

    def test_update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(self):
        """Test case for update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id

        Update tlive-kafka-oc by ID  # noqa: E501
        """
        pass

    def test_update_healthbot_ingest_settings_byoi_ingest_mapping_by_id(self):
        """Test case for update_healthbot_ingest_settings_byoi_ingest_mapping_by_id

        Update ingest-mapping by ID  # noqa: E501
        """
        pass

    def test_update_healthbot_ingest_settings_frequency_profile_by_id(self):
        """Test case for update_healthbot_ingest_settings_frequency_profile_by_id

        Update frequency-profile by ID  # noqa: E501
        """
        pass

    def test_update_healthbot_system_time_series_database_time_series_database_by_id(self):
        """Test case for update_healthbot_system_time_series_database_time_series_database_by_id

        Update time-series-database by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_ingest_settings(self):
        """Test case for update_iceberg_ingest_settings

        Update ingest-settings by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_ingest_settings_flow(self):
        """Test case for update_iceberg_ingest_settings_flow

        Update flow by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_ingest_settings_flow_template_by_id(self):
        """Test case for update_iceberg_ingest_settings_flow_template_by_id

        Update template by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_ingest_settings_syslog(self):
        """Test case for update_iceberg_ingest_settings_syslog

        Update syslog by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_ingest_settings_syslog_pattern_by_id(self):
        """Test case for update_iceberg_ingest_settings_syslog_pattern_by_id

        Update pattern by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_ingest_settings_syslog_pattern_set_by_id(self):
        """Test case for update_iceberg_ingest_settings_syslog_pattern_set_by_id

        Update pattern-set by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_profile_data_summarization_raw_by_id(self):
        """Test case for update_iceberg_profile_data_summarization_raw_by_id

        Update raw-data-summarization by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_profile_security_ca_profile_by_id(self):
        """Test case for update_iceberg_profile_security_ca_profile_by_id

        Update ca-profile by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_profile_security_local_certificate_by_id(self):
        """Test case for update_iceberg_profile_security_local_certificate_by_id

        Update local-certificate by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_profile_security_ssh_key_profile_by_id(self):
        """Test case for update_iceberg_profile_security_ssh_key_profile_by_id

        Update ssh-key-profile by ID  # noqa: E501
        """
        pass

    def test_update_iceberg_profiles(self):
        """Test case for update_iceberg_profiles

        Update profile by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
