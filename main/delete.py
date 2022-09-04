from main import Session, User, engine

local_session = Session(bind=engine)

user_to_delete=local_session.query(User).filter(User.username== "Artur").first()

local_session.delete(user_to_delete)

local_session.commit()