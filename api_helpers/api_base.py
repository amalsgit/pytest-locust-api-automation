import requests
import allure
from configs.config import get_environment


env = get_environment()
host_url = env.get("host_url")
