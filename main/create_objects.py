from main import User, Session, engine


users=[
    {
        "username":"Artur",
        "email":"artur@empresa.com"
    },
     {
        "username":"Jose",
        "email":"jose@empresa.com"
    },
     {
        "username":"Flora",
        "email":"flora@empresa.com"
    },
     {
        "username":"Andre",
        "email":"andre@empresa.com"
    },
     {
        "username":"Rui",
        "email":"rui@empresa.com"
    },
     {
        "username":"Humberto",
        "email":"humberto@empresa.com"
    },
]



local_sesion=Session(bind=engine)

# new_user=User(username="Buny", email="buny@empresa.com")

# local_sesion.add(new_user)

# local_sesion.commit()

for u in users:
    new_user=User(username=u["username"], email=u["email"])
    
    local_sesion.add(new_user)

    local_sesion.commit()

    print(f"Added {u['username']}")