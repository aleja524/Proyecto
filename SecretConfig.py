from dotenv import load_dotenv
import os

load_dotenv()  # carga variables de .env

PGHOST     = os.getenv("PGHOST")
PGDATABASE = os.getenv("PGDATABASE")
PGUSER     = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")