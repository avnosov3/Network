from fastapi import Depends
from fastapi_users import (
    BaseUserManager, FastAPIUsers, IntegerIDMixin,
    InvalidPasswordException
)
from fastapi_users.authentication import (
    AuthenticationBackend, BearerTransport, JWTStrategy
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.user import User
from .config import settings
from .db import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

bearer_transport = BearerTransport(tokenUrl='auth/jwt/login')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)

LEN_OF_PASSWORD_MESSAGE = 'Password should be at least 3 characters'
EMAIL_IN_PASSWORD = 'Password should not contain e-mail'


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):

    async def validate_password(
        self,
        password: str,
        user: User
    ) -> None:
        if len(password) < 3:
            raise InvalidPasswordException(
                reason=LEN_OF_PASSWORD_MESSAGE
            )

        if user.email in password:
            raise InvalidPasswordException(
                reason=EMAIL_IN_PASSWORD
            )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
