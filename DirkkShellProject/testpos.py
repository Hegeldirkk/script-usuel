#!/usr/bin/python3
"""test env method"""

import os

os.environ["TYPE_STORAGE"]='dbm'
type_storage = os.getenv("TYPE_STORAGE")

if type_storage == "db":
    print(type_storage)
else:
    print("env ne fonctionne pas")
    with open(".env.example") as env:
        for line in env.readlines():
            try:
                pair = line.split('=')
                key = pair[0]
                value = pair[1]
                os.environ['{}'.format(key)] = value[0:-1]
                type_storag = os.getenv('{}'.format(key))
                print(type_storag)
            except ValueError:
                # syntax error
                pass

