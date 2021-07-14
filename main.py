from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import column, or_
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine(
    "postgresql://postgres:password@localhost:5436/alchemy", echo=False
)

Session = sessionmaker(bind=engine)

session = Session()  # created new session for db

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# once table is done we have to migrate to database
Base.metadata.create_all(engine)


# instance of Student class

student1 = Student(name="jery", age=27, grade="fitth")

student2 = Student(name="tommy", age=66, grade="mca")
student3 = Student(name="renold", age=33, grade="phd")
# add student1 data to session we have created earlier


session.add(student1)  # if you have to add once record data

session.add_all([student1, student2, student3])

# commit session to database
session.commit()


# Get the data from database

students = session.query(Student)

for student in students:
    print(student.name, student.id, student.grade)
    print()


# Get data in order

students = session.query(Student).order_by(Student.name)

for student in students:
    print(student.name)

print(students)

# Get data by filter

student = session.query(Student).filter(Student.name == "jery").first()

print(student.name, student.age, student.grade)


students = session.query(Student).filter(
    or_(Student.name == "jery", Student.name == "renold")
)

for student in students:
    print(student.name, student.age)


# update data

student = session.query(Student).filter(Student.name == "abhi").first()

# student.name = "abhi"
# session.commit()

print(student.name)
# session.delete(student)
# session.commit()
