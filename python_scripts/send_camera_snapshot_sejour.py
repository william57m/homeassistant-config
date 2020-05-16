import os
from helpers.foscam_utility import download_snapshot
from helpers.telegram_utility import send_photo
from helpers.utilities import get_secrets
from helpers.config import SNAPSHOTS_PATH


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

# Download photo
snapshot_path = f'{SNAPSHOTS_PATH}/snapshot.jpg'
download_snapshot(foscam_ip, foscam_port, foscam_username, foscam_password, snapshot_path)

# Send photo
send_photo(api_key, chat_id, snapshot_path)
