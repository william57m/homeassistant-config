import json
import os
import requests
import urllib


def send_photo(api_key, chat_id, photo_path):
  os.system(f'curl -s -X POST "https://api.telegram.org/bot{api_key}/sendPhoto" -F chat_id={chat_id} -F photo="@{photo_path}" ')


def send_photos(api_key, chat_id, photo_paths):
  params = {
    'media': [],
    'files': {}
  }
  for path in photo_paths:
    name = path.split('/')[-1]
    params['media'].append({'type': 'photo', 'media': f'attach://{name}'})
    params['files'][name] = open(path, 'rb')

  encoded_media = urllib.parse.quote(json.dumps(params['media']))
  url = f'https://api.telegram.org/bot{api_key}/sendMediaGroup?chat_id={chat_id}&media={encoded_media}'

  # Send photos
  requests.post(url, files=params['files'])
