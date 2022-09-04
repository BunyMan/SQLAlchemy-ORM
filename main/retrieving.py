from main import User, Session, engine


local_session=Session(bind=engine)


#dá return de todos os objetos
users=local_session.query(User).all()[:3]

# for user in users:
#     print(user.username)

#query para um só objeto

buny=local_session.query(User).filter(User.username=="Jose").first()

print(buny)