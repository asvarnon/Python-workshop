
# SQLAlchemy setup using config/settings.py
from sqlalchemy import create_engine, MetaData, Table
from config.settings import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_SERVICE

oracle_url = f"oracle+cx_oracle://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"
engine = create_engine(oracle_url)
metadata = MetaData()

# Example: reflect the player table (add more as needed)
player = Table('player', metadata, autoload_with=engine)

# You can add more table reflections here, e.g.:
# artisan = Table('artisan', metadata, autoload_with=engine)