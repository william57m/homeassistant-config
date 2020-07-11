'''
Send snapshot via telegram for the given camera

python3 send_camera_snapshot.py CAMERA_NAME
'''

import sys
from helpers.foscam_utility import download_snapshot as download_snapshot_foscam
from helpers.hikvision_utility import download_snapshot as download_snapshot_hikvision
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

# Camera informations
camera_type = secrets[f'camera_{camera_name}_type']
camera_username = secrets[f'camera_{camera_name}_user']
camera_password = secrets[f'camera_{camera_name}_password']
camera_ip = secrets[f'camera_{camera_name}_ip']
camera_port = secrets[f'camera_{camera_name}_port']

# Download photo
snapshot_path = f'{SNAPSHOTS_PATH}/snapshot.jpg'

if camera_type == 'foscam':
    download_snapshot_foscam(camera_ip, camera_port, camera_username, camera_password, snapshot_path)
elif camera_type == 'hikvision':
    download_snapshot_hikvision(camera_ip, camera_port, camera_username, camera_password, snapshot_path)

# Send photo
send_photo(api_key, chat_id, snapshot_path)
