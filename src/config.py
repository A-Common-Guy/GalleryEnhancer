import os
from dotenv import load_dotenv

load_dotenv()

LIGHTLY_KEY = os.getenv("LIGHTLY_KEY")
DATASET_NAME = "Gallery"
REPORTS_PATH = "reports"