import requests
import sys

from helpers.config import SNAPSHOTS_PATH
from helpers.telegram_utility import send_photo
from helpers.utilities import get_secrets

def download_snapshot(url, to_path):
  '''
  Download snapshot for the given path
  '''
  r = requests.get(url)
  with open(to_path, 'wb') as f:
    f.write(r.content)

# Get secrets
secrets = get_secrets()

# Get state from args
camera_name = sys.argv[1]

# Bot informations
api_key = secrets['telegram_api_key']
chat_id = secrets['telegram_chat_id']

# Download photo
url = f'http://192.168.2.111:5000/camera_{camera_name}/person/best.jpg'
snapshot_path = f'{SNAPSHOTS_PATH}/snapshot_frigate_{camera_name}.jpg'
download_snapshot(url, snapshot_path)

# Send photo
send_photo(api_key, chat_id, snapshot_path)
