import requests
import xmltodict

def get_xml(enabled):
  enabled_bool = str(bool(int(enabled))).lower()

  return f'''
    <?xml version="1.0" sencoding="UTF-8"?>
      <MotionDetection version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
          <enabled>{enabled_bool}</enabled>
          <enableHighlight>{enabled_bool}</enableHighlight>
          <samplingInterval>2</samplingInterval>
          <startTriggerTime>500</startTriggerTime>
          <endTriggerTime>500</endTriggerTime>
          <regionType>grid</regionType>
          <Grid>
              <rowGranularity>18</rowGranularity>
              <columnGranularity>22</columnGranularity>
          </Grid>
          <MotionDetectionLayout version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
              <sensitivityLevel>20</sensitivityLevel>
              <layout>
                  <gridMap>fffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffcfffffc</gridMap>
              </layout>
          </MotionDetectionLayout>
      </MotionDetection>
    '''


def set_motion_sensor(ip, port, user, password, state=1):
  '''
  Enable/Disable motion sensor
  Docs: http://download.viakom.cz/HIKVISION/SDK/How%20to%20integrate%20with%20Hikvision%20LPR%20function%20via%20ISAPI-v1%200%200.pdf
    :param state: 0 disabled, 1 enabled
  '''

  xml = get_xml(state)
  headers = {'Content-Type': 'application/xml'}

  # Call
  r=requests.put(f'http://{ip}:{port}/ISAPI/System/Video/inputs/channels/1/motionDetection', headers=headers, data=xml, auth=requests.auth.HTTPDigestAuth(user, password))


def get_motion_sensor_state(ip, port, user, password):
  '''
  Get motion sensor state
    :return: 0 disabled, 1 enabled
  '''
  response = requests.get(f'http://{ip}:{port}/ISAPI/System/Video/inputs/channels/1/motionDetection', auth=requests.auth.HTTPDigestAuth(user, password))
  doc = xmltodict.parse(response.content)
  result = doc['MotionDetection']['enabled']
  result_int = 1 if result == 'true' else 0
  print(result_int)


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
  url = f'http://{ip}:{port}/ISAPI/Streaming/channels/101/picture'
  print(url)
  r = requests.get(url, auth=requests.auth.HTTPDigestAuth(user, password))
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
