from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

def get_db_engine():
    return create_engine('postgresql://{}:{}@{}/{}'.format('postgres', '123', 'localhost:5432', 'postgres'))

# Retry mechanism for connecting to the database
while True:
    try:
        db_engine = get_db_engine().connect()
        if db_engine:
            LOGGER.info("Successfully connected to the database.")
            break
    except OperationalError as e:
        LOGGER.warning(f"++++ Retrying connection to the database because of the issue: {str(e)} ++++")
        time.sleep(5)  # Wait for 5 seconds before retrying+")
