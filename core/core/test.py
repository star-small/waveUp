import os
from dotenv import load_dotenv

load_dotenv("/etc/environment")
print(os.environ["SECRET_KEY"])
