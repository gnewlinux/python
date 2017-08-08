#!/usr/bin/python
import sys
from datetime import datetime,timedelta,date

print "Hoje: %s"%datetime.now()
# daqui a 7 dias
print datetime.now() + timedelta(7)

# so a data
print date.today()

sys.exit()
