#!/usr/bin/python
# -*- coding: utf-8 -*-

#This python script will check to see what the current system's hostname is and set it
#The hostname will be set in the /ITS_tools/its-awx-server-build/awx-instance-deployment.yml 

import os
import subprocess

Short_Hostname_var = str(subprocess.getoutput("hostname -s"))

#Output of short_Hostname_var in all lowercase 
Short_Hostname_Lowercase_var = Short_Hostname_var.lower()

k_output([f"sed -i 's/ITS-SYSVAR/{Short_Hostname_Lowercase_var}/g' /ITS_tools/awx-operator/awx-operator/awx-deploy/awx-instance-deployment.yml"], shell=True, universal_newlines=True)

#Replace the Default Hostname in the base/awx.yaml file 
subprocess.check_output([f"sed -i 's/ITS-SYSVAR/{Short_Hostname_Lowercase_var}/g' /ITS_tools/awx-operator/awx-deploy/awx.yaml"], shell=True, universal_newlines=True)




