from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)

# Декоратор который присваивает имя таблице в БД на основе имя класса
    @declared_attr
    def __tablenamr__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    