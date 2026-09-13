from sqlalchemy import create_engine, String, Integer, Float, ForeignKey, select, Column, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

DATABASE_URL = "sqlite:///./schedule.db"

engine = create_engine(DATABASE_URL, echo=True)


class Base(DeclarativeBase):
    pass


class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    call = Column(JSON)


def init_db():
    Base.metadata.create_all(engine)


def return_bells(schedule: str):
    init_db()
    with Session(engine) as session:
        current_schedule = session.query(Schedule).filter(Schedule.name == schedule).first()
        return current_schedule.call


def create_schedule(schedule: str, calls: list):
    init_db()
    with Session(engine) as session:
        schedule_new = Schedule(
            name=schedule,
            call=calls
        )
        session.add(schedule_new)
        session.commit()
        session.refresh(schedule_new)


def delite_schedule(schedule: str):
    init_db()
    with Session(engine) as session:
        session.delete(session.query(Schedule).fliter(Schedule.name == schedule).first())
        session.commit()


def get_all_schedule():
    init_db()
    with Session(engine) as session:
        stmt = select(Schedule.name)
        return list(session.scalars(stmt))


print(get_all_schedule())
