'''
Send snapshots via telegram for the given camera

python3 send_camera_snapshots.py CAMERA_NAME
'''

import sys
from threading import Event
from helpers.foscam_utility import download_snapshot as download_snapshot_foscam
from helpers.hikvision_utility import download_snapshot as download_snapshot_hikvision
from helpers.telegram_utility import send_photos
from helpers.utilities import get_secrets
from helpers.config import SNAPSHOTS_PATH


# Params
nb_snapshot = 4
time_between_snapshot = 1

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

# Get snapshot and build params
event = Event()
photos = []
for i in range(nb_snapshot):
  snapshot_path = f'{SNAPSHOTS_PATH}/snapshot_{i}.jpg'
  if camera_type == 'foscam':
    download_snapshot_foscam(camera_ip, camera_port, camera_username, camera_password, snapshot_path)
  elif camera_type == 'hikvision':
    download_snapshot_hikvision(camera_ip, camera_port, camera_username, camera_password, snapshot_path)
    
  photos.append(snapshot_path)
  event.wait(time_between_snapshot)

# Send photos
send_photos(api_key, chat_id, photos)