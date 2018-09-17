# My Email Package
Python 3.6 Installable SMTP Email Package

Sends Email to address using SMTP server.

Install:
```
System:
$ bash install-system.sh

Conda:
$ conda activate Py3EnvName
$ python setup.py install
```

Usage:
```
import myEmail

bool = myEmail.sendEmail(fromAddr, toAddr, subject, msg, serverAddr, password, username=None, inPort=25, outPort=587)
```
Returns True if complete, prints exception and returns False if not.

Uses fromAddr as default username unless passing username parameter

Default SMTP port in/out = 25/587