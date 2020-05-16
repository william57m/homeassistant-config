'''
Send sleep command to MBP
'''

import os

os.system("ssh mbpwill 'pmset sleepnow'")
