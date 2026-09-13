from sqlalchemy import create_engine, String, Integer, Float, ForeignKey, select, Column, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

# ============ 1. Подключение к БД ============
# SQLite (файл в текущей папке)
DATABASE_URL = "sqlite:///./app.db"

# PostgreSQL:
# DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/mydb"

# MySQL:
# DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/mydb"

engine = create_engine(DATABASE_URL, echo=True)


# ============ 2. Базовый класс моделей ============
class Base(DeclarativeBase):
    pass


# ============ 3. Модели (таблицы) ============
class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    call = Column(JSON)


def init_db():
    Base.metadata.create_all(engine)
    print("Таблицы созданы!")


def return_bells(schedule: str):
    with Session(engine) as session:
        current_schedule = session.query(Schedule).filter(Schedule.name == schedule).first()
        return current_schedule.call


def create_schedule(schedule: str, calls: list):
    with Session(engine) as session:
        schedule_new = Schedule(
            name=schedule,
            call=calls
        )
        session.add(schedule_new)
        session.commit()
        session.refresh(schedule_new)


def delite_schedule(schedule: str):
    with Session(engine) as session:
        session.delete(session.query(Schedule).fliter(Schedule.name == schedule).first())
        session.commit()



init_db()
# create_schedule("Полный день", ["12:30", "10:10"])
# print(return_bells("Полный день"))

# class User(Base):
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(50))
#     age: Mapped[int] = mapped_column(Integer, nullable=True)
#
#     # Связь один-ко-многим
#     posts: Mapped[list["Post"]] = relationship(back_populates="author")
#
#     def __repr__(self) -> str:
#         return f"User(id={self.id}, name={self.name}, age={self.age})"
#
#
# class Post(Base):
#     __tablename__ = "posts"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(100))
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#
#     author: Mapped["User"] = relationship(back_populates="posts")
#
#     def __repr__(self) -> str:
#         return f"Post(id={self.id}, title={self.title})"
#
#
# # ============ 4. Создание таблиц ============
# def init_db():
#     Base.metadata.create_all(engine)
#     print("Таблицы созданы!")
#
#
# # ============ 5. CRUD операции ============
# def create_user(name: str, age: int | None = None) -> User:
#     with Session(engine) as session:
#         user = User(name=name, age=age)
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         return user
#
#
# def get_user(user_id: int) -> User | None:
#     with Session(engine) as session:
#         return session.get(User, user_id)
#
#
# def get_all_users() -> list[User]:
#     with Session(engine) as session:
#         stmt = select(User)
#         return list(session.scalars(stmt))
#
#
# def update_user(user_id: int, new_name: str) -> None:
#     with Session(engine) as session:
#         user = session.get(User, user_id)
#         if user:
#             user.name = new_name
#             session.commit()
#
#
# def delete_user(user_id: int) -> None:
#     with Session(engine) as session:
#         user = session.get(User, user_id)
#         if user:
#             session.delete(user)
#             session.commit()
#
#
# # ============ 6. Пример использования ============
# if __name__ == "__main__":
#     init_db()
#
#     # Создание
#     user = create_user("Иван", 30)
#     print(f"Создан: {user}")
#
#     create_user("Мария", 25)
#     create_user("Пётр", 40)
#
#     # Чтение
#     print("\nВсе пользователи:")
#     for u in get_all_users():
#         print(f"  {u}")
#
#     # Обновление
#     update_user(user.id, "Иван Иванович")
#     print(f"\nПосле обновления: {get_user(user.id)}")
#
#     # Удаление
#     delete_user(user.id)
#     print("\nПосле удаления:")
#     for u in get_all_users():
#         print(f"  {u}")
