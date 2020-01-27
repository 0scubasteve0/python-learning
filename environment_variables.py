#!/usr/bin/env python3.8

import os
from math import pi

digits = int(os.environ["DIGITS"])

if digits >= 0:
    print("%.*f" % (digits, pi))
else:
    print("%.*f" % (10, pi))

