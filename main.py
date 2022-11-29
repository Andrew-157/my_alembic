from models import Contact
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from random import randint

engine = create_engine("sqlite:///mybase.db", echo=True)
Session = sessionmaker(bind=engine)

session = Session()


fake = Faker()
for id in range(1, 3):
    fake_name = fake.name()
    session.add(Contact(id=id, name=fake_name, phone=randint(1000, 2000)))

for id in range(3, 5):
    fake_name = fake.name()
    session.add(Contact(id=id, name=fake_name, phone=randint(1000, 2000)))


session.commit()
