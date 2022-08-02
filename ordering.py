from main import Session, engine, User
from sqlalchemy import desc

local_session=Session(bind=engine)

#ordem ascendente
#users=local_session.query(User).order_by(User.username).all()

#ordem descendente
users_descending=local_session.query(User).order_by(desc(User.username)).all()

for user in users_descending:
    print(f"User {user.username}")