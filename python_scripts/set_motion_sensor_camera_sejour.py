import sys
from helpers.foscam_utility import set_motion_sensor
from helpers.utilities import get_secrets


# Open secrets
secrets = get_secrets()

# Foscam informations
foscam_username = secrets['foscam_user']
foscam_password = secrets['foscam_password']
foscam_ip = '192.168.2.118'
foscam_port = '88'

# Get state from args
state = sys.argv[1]

# Get snapshot and build params
set_motion_sensor(foscam_ip, foscam_port, foscam_username, foscam_password, state)
