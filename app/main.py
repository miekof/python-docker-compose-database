from datetime import datetime

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mariadb+mariadbconnector://root:example@database:3306/test_db?charset=utf8mb4", pool_size=20)
Base = declarative_base()


class TestInfo(Base):
    __tablename__ = 'test_info'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    create_time = sqlalchemy.Column(sqlalchemy.dialects.mysql.DATETIME)
    name = sqlalchemy.Column(sqlalchemy.String(length=255))
    test_type = sqlalchemy.Column(sqlalchemy.Integer)


Base.metadata.create_all(engine)
Session = sessionmaker(engine)


def add_test_info(name, test_type):
    new_test_info = TestInfo(name=name, create_time=datetime.now(), test_type=test_type)
    database_add(new_test_info)


def database_add(*data_models):
    with Session() as session:
        session.begin()
        try:
            for data_model in data_models:
                session.add(*data_models)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()


def select_all():
    with Session() as session:
        return session.query(TestInfo).all()


def print_all_list(test_info_list: [TestInfo]):
    for test_info in test_info_list:
        print(test_info.name)


if __name__ == '__main__':
    print('---------')
    add_test_info("Name A", 1)
    add_test_info("Name B", 2)
    add_test_info("Name Cd", 3)
    print_all_list(select_all())
