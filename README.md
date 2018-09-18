# My Email Package
Python Installable SMTP Email Package

Sends Email to address using SMTP server.

Install Python 3:
```
System:
$ cd py3
$ bash install-system.sh

Conda:
$ cd py3
$ conda activate Py3EnvName
$ python setup.py install
```

Install Python 2: ***NOT WORKING ATM***
```
System:
$ cd py2
$ bash install-system.sh

Conda:
$ cd py2
$ conda activate Py2EnvName
$ python setup.py install
```

Usage:
```
import myEmail

bool = myEmail.sendEmail(fromAddr, toAddr, subject, msg, password, serverAddr=None, username=None, port=587):
```
Returns True if complete, prints exception and returns False if not.

Uses fromAddr as default username unless passing username parameter

Default SMTP port=587
