#!/usr/bin/python
# -*- coding: utf-8 -*-

#This script will get the ipv4 Address for the system
#An then add the entry to the /etc/hosts
import subprocess

# We will use the subprocess  command to output the current RHEL Version into a variable
Current_IP_Address_Var = subprocess.check_output(["hostname -I | awk ' {print $1}'"], shell=True, universal_newlines=True)

#Here we will remove the extra space from the Current_IP_Address_Var variable and store its contents in a new variable
Current_IP_Address_Final_var = Current_IP_Address_Var.strip()

#print(Current_IP_Address_Final_var)

#We now need to get the short hostname of the system

Short_Hostname_var = str(subprocess.getoutput("hostname -s"))


#We will create a string that will be appended to our /etc/hosts file
Host_string_var = (f"{Current_IP_Address_Final_var}" + " " f"{Short_Hostname_var}" + " " + f"{Short_Hostname_var}.grove.ad.uconn.edu")


#This command will append the string to our /etc/hosts file
subprocess.check_output([f'echo "{Host_string_var}" >> /etc/hosts'], shell=True, universal_newlines=True)

