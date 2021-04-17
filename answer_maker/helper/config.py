import os

from google.cloud.secretmanager_v1beta1.services import secret_manager_service as secretmanager

from .singleton import Singleton


def get_secret_manager(want: str):
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project=os.getenv("PROJECT_ID"), secret=want, secret_version=1)
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode('UTF-8')


class Config(Singleton):
    PROJECT_ID = str(os.getenv("PROJECT_ID"))
    TIMEZONE = str(os.getenv("TIMEZONE"))
    LINE_ACCESS_TOKEN = get_secret_manager("LINE_ACCESS_TOKEN")
    LINE_CHANNEL_SECRET = get_secret_manager("LINE_CHANNEL_SECRET")
    DEBUG = bool(os.getenv("DEBUG_MODE"))
    REPLY_TOKEN : str = ""
