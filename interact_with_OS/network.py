#!/usr/bin/env python3

import requests
import socket

def check_localhost:
        """ checks whether the local host is correctly configured """
        localhost = socket.gethostbyname('localhost')
        return localhost == "123.0.0.1"

def check_connectivity:
        """ checks whether the computer can make successful calls to the intern$
        request = requests.get("http://www.google.com")
        return request == 200
