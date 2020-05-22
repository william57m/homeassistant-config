import requests
import xmltodict


def set_motion_sensor(ip, port, user, password, state=1):
  '''
  Enable/Disable motion sensor
  Docs: https://www.camarasip.es/descarga/IP_Camera_CGI_(SDK).pdf
    :param state: 0 disabled, 1 enabled
  '''

  # Params
  linkage = 8
  schedule = 'schedule0=281474976710655&schedule1=281474976710655&schedule2=281474976710655&schedule3=281474976710655&schedule4=281474976710655&schedule5=281474976710655&schedule6=281474976710655'
  area = 'area0=1023&area1=1023&area2=1023&area3=1023&area4=1023&area5=1023&area6=1023&area7=1023&area8=1023&area9=1023'

  # Call
  requests.get(f'http://{ip}:{port}/cgi-bin/CGIProxy.fcgi?cmd=setMotionDetectConfig&isEnable={state}&usr={user}&pwd={password}&linkage={linkage}&schedule={schedule}&area={area}')


def get_motion_sensor_state(ip, port, user, password):
  '''
  Get motion sensor state
    :return: 0 disabled, 1 enabled
  '''
  response = requests.get(f'http://{ip}:{port}/cgi-bin/CGIProxy.fcgi?cmd=getMotionDetectConfig&usr={user}&pwd={password}')
  doc = xmltodict.parse(response.content)
  result = doc['CGI_Result']['isEnable'][0]
  print(result)


def get_motion_alert(ip, port, user, password):
  '''
  Get motion status
    :return: 0 Disabled, 1 No Alarm, 2 Detect Alarm
  '''
  response = requests.get(f'http://{ip}:{port}/cgi-bin/CGIProxy.fcgi?cmd=getDevState&usr={user}&pwd={password}')
  doc = xmltodict.parse(response.content)
  result = doc['CGI_Result']['motionDetectAlarm'][0]
  print(result)


def download_snapshot(ip, port, user, password, to_path):
  '''
  Download snapshot for the given path
  '''
  url = f'http://{ip}:{port}/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr={user}&pwd={password}'
  r = requests.get(url)
  with open(to_path, 'wb') as f:
    f.write(r.content)


def process_command(cmd, ip, port, user, password, options):
  '''
  Process command
  '''
  if cmd == 'getMotionAlert':
    get_motion_alert(ip, port, user, password)
  elif cmd == 'getMotionSensor':
    get_motion_sensor_state(ip, port, user, password)
  elif cmd == 'setMotionSensor':
    state = options[0]
    set_motion_sensor(ip, port, user, password, state)
  else:
    print('Commant not recognized')
