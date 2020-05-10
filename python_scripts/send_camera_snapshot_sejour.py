import os
import yaml

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
foscam_snapshot_url = f'http://{foscam_ip}:{foscam_port}/cgi-bin/CGIProxy.fcgi\\?cmd\\=snapPicture2\\&usr\\={foscam_username}\\&pwd\\={foscam_password}'

# Get snapshot
os.system(f'curl {foscam_snapshot_url} -o /home/homeassistant/.homeassistant/tmp/snapshot.jpg')

# Send photo
os.system(f'curl -s -X POST "https://api.telegram.org/bot{api_key}/sendPhoto" -F chat_id={chat_id} -F photo="@/home/homeassistant/.homeassistant/tmp/snapshot.jpg" ')
