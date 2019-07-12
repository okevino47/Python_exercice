#!/usr/bin/env python3

import sys
import socket
import subprocess

out, err = subprocess.Popen(["ls"] + sys.argv[1:], stdout=subprocess.PIPE).communicate()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4242))
s.send(out)
s.close()
