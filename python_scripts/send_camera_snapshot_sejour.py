import os
import yaml

# Open secrets
secret_file = open('/home/homeassistant/.homeassistant/secrets.yaml', 'r')
secrets = yaml.load(secret_file, Loader=yaml.FullLoader)

# Bot informations
apiKey = secrets['telegram_api_key']
chatId = secrets['telegram_chat_id']

# Foscam informations
foscamUsername = secrets['foscam_user']
foscamPassword = secrets['foscam_password']
foscamIp = '192.168.2.118'
foscamPort = '88'
foscamSnapshotUrl = f'http://{foscamIp}:{foscamPort}/cgi-bin/CGIProxy.fcgi\\?cmd\\=snapPicture2\\&usr\\={foscamUsername}\\&pwd\\={foscamPassword}'

# Get snapshot
os.system(f'curl {foscamSnapshotUrl} -o /home/homeassistant/.homeassistant/tmp/snapshot.jpg')

# Send photo
os.system(f'curl -s -X POST "https://api.telegram.org/bot{apiKey}/sendPhoto" -F chat_id={chatId} -F photo="@/home/homeassistant/.homeassistant/tmp/snapshot.jpg" ')

