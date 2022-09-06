from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

#   Uma relação "one to many" coloca uma foreign key na tabela filha a referenciar a tabela mãe.
#   A função .relationship() é especificada depois na tabela mãe a referenciar os items representados
#       pela filha.

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))




#   Para estabelecer uma relação bidirecional em "one to many" onde o inverso é "many to one", basta
#       especificar uma .relationship() adicional e ligar as duas usando o parametro 
#       .relationship.back_populates().

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")

#   Assim "Child" vai ficar com um atributo "Parent" com semântica de "many to one".


#   Alternativamente a opção relationship.backref pode ser utilizada numa unica relationship() em vez de se utilizar
#   relationship.back_populates

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")