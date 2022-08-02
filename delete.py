from main import Session, User, engine

local_session = Session(bind=engine)

user_to_delete=local_session.query(User).filter(User.username== "BunyMan").first()

local_session.delete(user_to_delete)

local_session.commit()