
from sqlalchemy import create_engine, MetaData, ForeignKey, Column, DateTime, String, Integer
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from cockroachdb.sqlalchemy import run_transaction

from datetime import datetime

# "clinic" is the database to be tested
engine = create_engine(name_or_url='cockroachdb://root@localhost:26257/clinic?sslmode=disable', echo=True)
Base = declarative_base()
class Appointment(Base):
    """
    Appointment information for physician's records.

    Args:
        Base (sqlalchemy.ext.declarative): Base class acts as root holding all databases and subsequent tables
    """
    __tablename__ = 'Appointment'
    _id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)

    # METHODS
    def __repr__(self):
        """

        Returns:
            str: Representation of appointment
        """
        return f'Appointnment<first_name: {first_name}, last_name: {last_name}, datetime: {date_time}>'

class Prescription(Base):
    """
    Prescription information for patient.

    Args:
        Base (sqlalchemy.ext.declarative): Base class acts as root holding all databases and subsequent tables
    """
    __tablename__ = 'Prescription'
    rx = Column(Integer, primary_key=True, nullable=False)
    medication = Column(String, nullable=False)
    mg = Column(Integer, nullable=False)


Session = sessionmaker(bind=engine)
sess = Session()
# appt1 = Appointment(id=1, first_name='John', last_name='Smith', date_time=datetime(year=2021, month=11, day=30, hour=18))

# sess.begin()
sess.add(Appointment(_id=1, first_name='John', last_name='Smith', date_time=datetime(year=2021, month=11, day=30, hour=18)))
sess.commit()
