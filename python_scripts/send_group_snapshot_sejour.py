import os
import requests
import threading
import yaml
import urllib
import json

# Open secrets
secret_file = open('/home/homeassistant/.homeassistant/secrets.yaml', 'r')
secrets = yaml.load(secret_file, Loader=yaml.FullLoader)

# Bot informations
apiKey = secrets['telegram_api_key']
chat_id = secrets['telegram_chat_id']

# Foscam informations
foscamUsername = secrets['foscam_user']
foscamPassword = secrets['foscam_password']
foscamIp = '192.168.2.118'
foscamPort = '88'
foscamSnapshotUrl = f'http://{foscamIp}:{foscamPort}/cgi-bin/CGIProxy.fcgi\\?cmd\\=snapPicture2\\&usr\\={foscamUsername}\\&pwd\\={foscamPassword}'

event = threading.Event()

# Get snapshot
for i in range(3):
  os.system(f'curl {foscamSnapshotUrl} -o /home/homeassistant/.homeassistant/tmp/snapshot_{i+1}.jpg')
  event.wait(1)

# Send photo
url = f'https://api.telegram.org/bot{apiKey}/sendMediaGroup'
data = {
  'media': [
    {'type': 'photo', 'media': "attach://photo_1"},
    {'type': 'photo', 'media': "attach://photo_2"},
    {'type': 'photo', 'media': "attach://photo_3"}
  ]
}

dataj = json.dumps(data['media'])
params = urllib.parse.quote(dataj)
url = f'{url}?chat_id={chat_id}&media={params}'

data_files = {
  'photo_1': open('/home/homeassistant/.homeassistant/tmp/snapshot_1.jpg', 'rb'),
  'photo_2': open('/home/homeassistant/.homeassistant/tmp/snapshot_2.jpg', 'rb'),
  'photo_3': open('/home/homeassistant/.homeassistant/tmp/snapshot_3.jpg', 'rb')
}

requests.post(url, files=data_files)
