#!/usr/bin/python

import boto3

CONFIG_FILEPATH = '/usr/local/etc/opensips/opensips.cfg'

DB_HOST_PLACEHOLDER = "DB_HOST"
DB_NAME_PLACEHOLDER = "DB_NAME"
DB_USERNAME_PLACEHOLDER = "DB_USERNAME"
DB_PASSWORD_PLACEHOLDER = "DB_PASSWORD"

ssm = boto3.client('ssm', 'ca-central-1')
db_host = ssm.get_parameter(Name='opensips-registrar-db-host')
db_name = ssm.get_parameter(Name='opensips-registrar-db-name')
db_username = ssm.get_parameter(Name='opensips-registrar-db-username')
db_password = ssm.get_parameter(Name='opensips-registrar-db-password',
        WithDecryption=True)

config_file = open(CONFIG_FILEPATH, "rt")
config_file_text = config_file.read()
config_file_text_new = config_file_text.replace(DB_HOST_PLACEHOLDER,
        db_host['Parameter']['Value'])  \
    .replace(DB_NAME_PLACEHOLDER, db_name['Parameter']['Value']) \
    .replace(DB_USERNAME_PLACEHOLDER, db_username['Parameter']['Value']) \
    .replace(DB_PASSWORD_PLACEHOLDER, db_password['Parameter']['Value'])
config_file.close()

config_file = open(CONFIG_FILEPATH, "wt")
config_file.write(config_file_text_new)
config_file.close()
