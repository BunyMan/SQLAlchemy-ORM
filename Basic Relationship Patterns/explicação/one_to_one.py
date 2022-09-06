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

    # coleção "one to many"
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))

    # scalar "many to one"
    parent = relationship("Parent", back_populates="children")



#   neste caso Parent.children é o lado "one to many" a referenciar uma coleção e child.parent é o "many to one"
#       a referenciar um unico objeto. Para converter isto para "one to one", o lado "one to many" é convertido
#       para uma relação escalar ao usar o uselist=False, renomeando o Parent.children para Parent.child

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)

    # o que era antes uma "one to many" Parent.children é agora uma "one to one" Parent.child
    child = relationship("Child", back_populates="parent", uselist=False)


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))

    # o "many to one" mantém-se
    parent = relationship("Parent", back_populates="child")