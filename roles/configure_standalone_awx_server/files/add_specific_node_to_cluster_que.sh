#!/bin/bash

/usr/bin/awx-manage provision_instance --hostname $HOSTNAME --node_type control

/usr/bin/awx-manage register_queue --queuename cluster_name --hostname $HOSTNAME