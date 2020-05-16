import sys
from helpers.foscam_utility import download_snapshot
from helpers.telegram_utility import send_photo
from helpers.utilities import get_secrets
from helpers.config import CAMERAS, SNAPSHOTS_PATH


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

# Download photo
snapshot_path = f'{SNAPSHOTS_PATH}/snapshot.jpg'
download_snapshot(foscam_ip, foscam_port, foscam_username, foscam_password, snapshot_path)

# Send photo
send_photo(api_key, chat_id, snapshot_path)
