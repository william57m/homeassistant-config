'''
Set alarm speaker

python3 set_alarm_speaker.py [STATE]
'''

import sys

# Get arguments
state = sys.argv[1]

# Set speaker
if state == 'on':
  print('Turn on speaker')
else:
  print('Turn off speaker')
