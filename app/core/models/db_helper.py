from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from asyncio import current_task
from core.config import settings
from sqlalchemy.orm import sessionmaker

# Асинхронный БД движок
class DataBaseHelper:
    def __init__(self, url: str, echo: bool=False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        print(self.engine)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
            )
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return self.session_factory()
    async def session_dependency(self):
        async with self.get_scoped_session() as session:
            yield session
            
        
db_helper = DataBaseHelper(
     url=settings.db_url,
    echo=settings.db_echo,
)
