import wmi

ip = 'ec2-65-0-102-50.ap-south-1.compute.amazonaws.com'

username = 'Administrator'

password = 'password'

from socket import *

try:

    print("Establishing connection to %s" %ip)

    connection = wmi.WMI(ip, user=username, password=password)

    print("Connection established")

except wmi.x_wmi:

    print("Your Username and Password of "+getfqdn(ip)+" are wrong.")


import wmi

import os

import subprocess

import re

import socket, sys

 

def main():

 

     host="remotemachine"

     username="adminaam"

     password="passpass!"

     server =connects(host, username, password)

     s = socket.socket()

     s.settimeout(5)

     print server.run_remote('hostname')

 

class connects:

 

    def __init__(self, host, username, password, s = socket.socket()):

        self.host=host

        self.username=username

        self.password=password

        self.s=s

 

        try:

            self.connection= wmi.WMI(self.host, user=self.username, password=self.password)

            self.s.connect(('10.10.10.3', 25))

            print "Connection established"

        except:

            print "Could not connect to machine"

def run_remote(self, cmd, async=False, minimized=True):

       call=subprocess.check_output(cmd, shell=True,stderr=subprocess.STDOUT )

       print call

 

main()

import paramiko

 

hostname = "ec2-65-0-102-50.ap-south-1.compute.amazonaws.com"

username = "Administrator"

password = "X$H6cKd$LRr3xSgA8242G=G2iqwaoCZ2"

cmd = 'your-command'

 

try:

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname,username=username,password=password)

    print("Connected to %s" % hostname)

except paramiko.AuthenticationException:

    print("Failed to connect to %s due to wrong username/password" %hostname)

    exit(1)

except Exception as e:

    print(e.message)    

    exit(2)

 