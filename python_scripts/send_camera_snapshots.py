import sys
from threading import Event
from helpers.foscam_utility import download_snapshot
from helpers.telegram_utility import send_photos
from helpers.utilities import get_secrets
from helpers.config import CAMERAS, SNAPSHOTS_PATH


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

# Foscam informations
foscam_username = secrets['foscam_user']
foscam_password = secrets['foscam_password']
foscam_ip = CAMERAS[camera_name]['ip']
foscam_port = CAMERAS[camera_name]['port']

# Get snapshot and build params
event = Event()
photos = []
for i in range(nb_snapshot):
  snapshot_path = f'{SNAPSHOTS_PATH}/snapshot_{i}.jpg'
  download_snapshot(foscam_ip, foscam_port, foscam_username, foscam_password, snapshot_path)
  photos.append(snapshot_path)
  event.wait(time_between_snapshot)

# Send photos
send_photos(api_key, chat_id, photos)