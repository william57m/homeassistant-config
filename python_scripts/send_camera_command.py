'''
Process Foscam commands
  - getMotionStatus
  - getMotionSensor
  - setMotionSensor

python3 send_camera_command.py CAMERA_NAME COMMAND [OPTIONS]
'''

import sys
from helpers.foscam_utility import process_command as process_command_foscam
from helpers.hikvision_utility import process_command as process_command_hikvision
from helpers.utilities import get_secrets


# Get secrets
secrets = get_secrets()

# Get arguments
camera_name = sys.argv[1]
command = sys.argv[2]
options = sys.argv[3:]

# Camera informations
camera_type = secrets[f'camera_{camera_name}_type']
camera_username = secrets[f'camera_{camera_name}_user']
camera_password = secrets[f'camera_{camera_name}_password']
camera_ip = secrets[f'camera_{camera_name}_ip']
camera_port = secrets[f'camera_{camera_name}_port']

# Process command
if camera_type == 'foscam':
  process_command_foscam(command, camera_ip, camera_port, camera_username, camera_password, options)
elif camera_type == 'hikvision':
  process_command_hikvision(command, camera_ip, camera_port, camera_username, camera_password, options)
