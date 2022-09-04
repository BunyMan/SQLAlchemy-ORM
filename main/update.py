from main import Session, engine, User

local_session=Session(bind=engine)

user_to_update=local_session.query(User).filter(User.username == "Artur").first()

user_to_update.username = "ArturLouçano"
user_to_update.email = "AL@empresa.com"

local_session.commit()
