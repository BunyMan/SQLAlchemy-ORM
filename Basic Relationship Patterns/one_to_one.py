from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

#   "one to one" é essencialmente uma relação bidirecional com atributos do tipo scalar dos dois lados. 
#   quando se usam ORMs "one to one" é qconsiderado uma convenção onde a ORM assume que cada linha filha 
#       tem apenas uma linha mãe.
#   a relação "one to one" é criada ao dar o valor False ao parâmetro relationship.uselist da função relationship()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)

    # one-to-many collection
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))

    # many-to-one scalar
    parent = relationship("Parent", back_populates="children")