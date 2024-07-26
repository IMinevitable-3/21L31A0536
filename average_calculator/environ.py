import os
from dotenv import load_dotenv

load_dotenv()
test_base_url = os.environ.get("test_base_url", "http://20.244.56.144/test/")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
