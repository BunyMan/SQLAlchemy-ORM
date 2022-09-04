from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

#   Uma relação "many to one" coloca a foreign key na tabla mãe a referenciar a filha. relationship()
#       é declarada na mãe com o atributo scalar-holding (um valor que é apenas uma coisa e não uma coleção)


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("child.id"))
    child = relationship("Child")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)

#   Adicionar bidirecionalidade é tão simples como adicionar uma segunda relationship() e usar o parâmetro
#       relationship.back_populates nas duas direções.

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("child.id"))
    child = relationship("Child", back_populates="parents")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parents = relationship("Parent", back_populates="child")


#   Alternativamente a opção relationship.backref pode ser utilizada numa unica relationship() (ex.: Parent.child)

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("child.id"))
    child = relationship("Child", backref="parents")