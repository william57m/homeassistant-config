import yaml
from helpers.config import SECRETS_PATH


# Open secrets
def get_secrets(path = SECRETS_PATH):
  secret_file = open(path, 'r')
  secrets = yaml.load(secret_file, Loader=yaml.FullLoader)
  return secrets
