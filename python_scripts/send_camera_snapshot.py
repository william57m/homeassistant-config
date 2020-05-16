'''
Send snapshot via telegram for the given camera

python3 send_camera_snapshot.py CAMERA_NAME
'''

import sys
from helpers.foscam_utility import download_snapshot
from helpers.telegram_utility import send_photo
from helpers.utilities import get_secrets
from helpers.config import SNAPSHOTS_PATH


# Get secrets
secrets = get_secrets()

# Get state from args
camera_name = sys.argv[1]

# Bot informations
api_key = secrets['telegram_api_key']
chat_id = secrets['telegram_chat_id']

# Foscam informations
foscam_username = secrets['foscam_user']
foscam_password = secrets['foscam_password']
foscam_ip = secrets[f'foscam_{camera_name}_ip']
foscam_port = secrets[f'foscam_{camera_name}_port']

# Download photo
snapshot_path = f'{SNAPSHOTS_PATH}/snapshot.jpg'
download_snapshot(foscam_ip, foscam_port, foscam_username, foscam_password, snapshot_path)

# Send photo
send_photo(api_key, chat_id, snapshot_path)
