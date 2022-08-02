from main import Session, engine, User

local_session=Session(bind=engine)

user_to_update=local_session.query(User).filter(User.username == "Buny").first()

user_to_update.username = "BunyMan"
user_to_update.email = "bunyman@empresa.com"

local_session.commit()