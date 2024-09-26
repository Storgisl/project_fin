from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

import os
import logging
import time

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

engine = create_engine('postgresql://{}:{}@{}/{}'.format(os.getenv('POSTGRES_USER'), os.getenv('POSTGRES_PASSWORD'), os.getenv('POSTGRES_HOST'), os.getenv('POSTGRES_DB')))

# Retry mechanism for connecting to the database
# while True:
#     try:
#         db_engine = get_db_engine().connect()
#         if db_engine:
#             LOGGER.info("Successfully connected to the database.")
#             break
#     except OperationalError as e:
#         LOGGER.warning(f"++++ Retrying connection to the database because of the issue: {str(e)} ++++")
#         time.sleep(5)
