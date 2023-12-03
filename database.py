from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs import Config


db = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(db, echo=True)


Session = sessionmaker(bind=engine)




