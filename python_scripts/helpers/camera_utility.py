import requests

def download_snapshot(ip, port, endpoint, to_path):
  '''
  Download snapshot for the given path
  '''
  r = requests.get(f'http://{ip}:{port}{endpoint}')
  with open(to_path, 'wb') as f:
    f.write(r.content)
