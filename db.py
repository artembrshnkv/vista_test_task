from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from config_reader import config

engine = create_engine(
    "mysql+pymysql://{}:{}@{}/{}".format(config.db_user, config.db_password,
                                         config.db_host, config.db_name)
)

metadata = MetaData()
Base = declarative_base(metadata=metadata)
Session = sessionmaker(bind=engine)
session = Session()
