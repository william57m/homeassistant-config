import requests
import xmltodict


def set_motion_sensor(ip, port, user, password, state=1):
  '''
  Enable/Disable motion sensor
    :param state: 0 to disable, 1 to enable
  '''
  requests.get(f'http://{ip}:{port}/cgi-bin/CGIProxy.fcgi?cmd=setMotionDetectConfig&isEnable={state}&usr={user}&pwd={password}')


def get_motion_sensor_state(ip, port, user, password):
  '''
  Get motion sensor state
    :return: 0 when disabled, 1 when enabled
  '''
  response = requests.get(f'http://{ip}:{port}/cgi-bin/CGIProxy.fcgi?cmd=getMotionDetectConfig&usr={user}&pwd={password}')
  doc = xmltodict.parse(response.content)
  result = doc['CGI_Result']['isEnable'][0]
  print(result)


def download_snapshot(ip, port, user, password, to_path):
  '''
  Download snapshot for the given path
  '''
  url = f'http://{ip}:{port}/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr={user}&pwd={password}'
  r = requests.get(url)
  with open(to_path, 'wb') as f:
    f.write(r.content)
