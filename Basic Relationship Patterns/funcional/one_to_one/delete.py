from main import Parent, Child, session

print(f"Parents {session.query(Parent).all()}")

print(f"Children {session.query(Child).all()}")


parent_to_delete=session.query(Parent).filter(Parent.id==1.first())