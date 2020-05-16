from threading import Event
from helpers.foscam_utility import download_snapshot
from helpers.telegram_utility import send_photos
from helpers.utilities import get_secrets
from helpers.config import SNAPSHOTS_PATH


# Params
nb_snapshot = 4
time_between_snapshot = 1

# Open secrets
secrets = get_secrets()

# Bot informations
api_key = secrets['telegram_api_key']
chat_id = secrets['telegram_chat_id']

# Foscam informations
foscam_username = secrets['foscam_user']
foscam_password = secrets['foscam_password']
foscam_ip = '192.168.2.118'
foscam_port = '88'

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