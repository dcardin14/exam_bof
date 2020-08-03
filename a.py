#!/usr/bin/env python2
import socket

ServiceManagerIP = "10.0.2.7"
ServiceManagerPort = 42424

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ServiceManagerIP, ServiceManagerPort))
msg = raw_input('Welcome to the Foo Phones Customer Manager.\r\n\r\nPlease Enter A Customer ID: ') + "\r\n"

s.send(msg)
data = s.recv(len(msg))
s.recv(1024)
s.close()
print data
