#!/bin/bash

/usr/bin/awx-manage createsuperuser --username backup_username --no-input --email iam@uconn.edu && /usr/bin/awx-manage update_password --username=backup_username --password=backup_password && exit
