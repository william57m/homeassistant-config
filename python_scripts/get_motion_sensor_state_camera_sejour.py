import sys
from helpers.foscam_utility import get_motion_sensor_state
from helpers.utilities import get_secrets


# Open secrets
secrets = get_secrets()

# Foscam informations
foscam_username = secrets['foscam_user']
foscam_password = secrets['foscam_password']
foscam_ip = '192.168.2.118'
foscam_port = '88'

# Get snapshot and build params
get_motion_sensor_state(foscam_ip, foscam_port, foscam_username, foscam_password)
