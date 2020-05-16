'''
Process Foscam commands
  - getMotionStatus
  - getMotionSensor
  - setMotionSensor

python3 foscam_command.py CAMERA_NAME COMMAND [OPTIONS]
'''

import sys
from helpers.foscam_utility import process_command
from helpers.utilities import get_secrets


# Get secrets
secrets = get_secrets()

# Get arguments
camera_name = sys.argv[1]
command = sys.argv[2]
options = sys.argv[3:]

# Foscam informations
foscam_username = secrets['foscam_user']
foscam_password = secrets['foscam_password']
foscam_ip = secrets[f'foscam_{camera_name}_ip']
foscam_port = secrets[f'foscam_{camera_name}_port']

# Process command
process_command(command, foscam_ip, foscam_port, foscam_username, foscam_password, options)
