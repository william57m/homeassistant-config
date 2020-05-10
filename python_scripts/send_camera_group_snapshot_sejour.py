import json
import os
import requests
import threading
import urllib
import yaml
from helpers import download_snapshot

# Params
nb_snapshot = 4
time_between_snapshot = 1

# Open secrets
secret_file = open('/home/homeassistant/.homeassistant/secrets.yaml', 'r')
secrets = yaml.load(secret_file, Loader=yaml.FullLoader)

# Bot informations
api_key = secrets['telegram_api_key']
chat_id = secrets['telegram_chat_id']

# Foscam informations
foscam_username = secrets['foscam_user']
foscam_password = secrets['foscam_password']
foscam_ip = '192.168.2.118'
foscam_port = '88'
foscam_snapshot_url = f'http://{foscam_ip}:{foscam_port}/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr={foscam_username}&pwd={foscam_password}'

# Get snapshot and build params
event = threading.Event()
params = {
  'media': [],
  'files': {}
}
for i in range(nb_snapshot):
  snapshot_name = f'snapshot_{i}'
  snapshot_path = f'/home/homeassistant/.homeassistant/tmp/{snapshot_name}.jpg'
  download_snapshot(foscam_snapshot_url, snapshot_path)
  params['media'].append({'type': 'photo', 'media': f'attach://{snapshot_name}'})
  params['files'][snapshot_name] = open(snapshot_path, 'rb')
  event.wait(time_between_snapshot)

# Prepare request
encoded_media = urllib.parse.quote(json.dumps(params['media']))
url = f'https://api.telegram.org/bot{api_key}/sendMediaGroup?chat_id={chat_id}&media={encoded_media}'

# Send photos
requests.post(url, files=params['files'])
