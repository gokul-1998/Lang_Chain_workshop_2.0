
import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
QDRANT_URL= os.environ.get("QDRANT_URL")
qdrant_Api_Key= os.environ.get("qdrant_Api_Key")

