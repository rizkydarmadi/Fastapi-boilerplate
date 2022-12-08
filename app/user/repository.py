from typing import Tuple, List
from .model import User
from sqlalchemy import select, or_, func
from database import Session
import pytz
from datetime import datetime
from passlib.context import CryptContext
from common.utils import SQLutils


class authRepository:
    @staticmethod
    def check_user(id: int) -> bool:
        with Session() as session:
            stmt = select(User).where(User.id == id, User.active == 1)
            data = session.execute(stmt).scalar()
        if data == None:
            return False
        else:
            return True

    @staticmethod
    def check_email(email: str) -> bool:
        with Session() as session:
            stmt = select(User).where(User.email == email, User.active == 1)
            data = session.execute(stmt).scalar()
        if data == None:
            return False
        else:
            return True

    @staticmethod
    def create_new_user(
        first_name: str,
        midle_name: str,
        last_name: str,
        mobile: str,
        email: str,
        password_hash: str,
        intro: str,
        profile: str,
        role_id: str,
    ) -> User:

        with Session() as session:
            new_user = User(
                first_name=first_name,
                midle_name=midle_name,
                last_name=last_name,
                mobile=mobile,
                email=email,
                password_hash=password_hash,
                registered_at=datetime.now(pytz.timezone("Asia/Jakarta")),
                last_login=None,
                intro=intro,
                profile=profile,
                role_id=role_id,
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        return new_user

    @staticmethod
    def verify_password(user_id: int, plain_password: str) -> bool:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        with Session() as session:
            stmt = select(User.password_hash).where(
                User.id == user_id, User.active == 1
            )
            hashed_password = session.execute(stmt).scalar()
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_user(user_id: int) -> User:
        with Session() as session:
            stmt = select(User).where(User.id == user_id, User.active == 1)
            user = session.execute(stmt).scalar()
        return user

    @staticmethod
    def get_all(
        page: int = None, limit: int = None, terms: str = None
    ) -> Tuple[List[User], int]:
        offset = SQLutils.offset(page=page, limit=limit)
        with Session() as session:
            stmt = (
                select(User)
                .where(
                    or_(
                        User.first_name.ilike(f"%{terms}%"),
                        User.midle_name.ilike(f"%{terms}%"),
                        User.last_name.ilike(f"%{terms}%"),
                        User.email.ilike(f"%{terms}%"),
                        User.intro.ilike(f"%{terms}%"),
                        User.profile.ilike(f"%{terms}%"),
                    ),
                    User.active == 1,
                )
                .order_by(User.id.asc())
                .limit(limit=limit)
                .offset(offset=offset)
            )
            data = session.execute(stmt).scalars().all()

            stmt2 = (
                select(func.count(User.username))
                .where(
                    or_(
                        User.first_name.ilike(f"%{terms}%"),
                        User.midle_name.ilike(f"%{terms}%"),
                        User.last_name.ilike(f"%{terms}%"),
                        User.email.ilike(f"%{terms}%"),
                        User.intro.ilike(f"%{terms}%"),
                        User.profile.ilike(f"%{terms}%"),
                    ),
                    User.active == 1,
                )
                .limit(limit=limit)
                .offset(offset=offset)
            )
            num_data = session.execute(stmt2).scalar()

        return data, num_data

    @staticmethod
    def update_user(
        first_name: str,
        midle_name: str,
        last_name: str,
        mobile: str,
        email: str,
        password_hash: str,
        intro: str,
        profile: str,
        role_id: str,
        id: int,
    ) -> User:
        with Session() as session:
            stmt = select(User).where(User.id == id, User.active == 1)
            user = session.execute(stmt).scalar()

            # updated data

            user.first_name = (first_name,)
            user.midle_name = (midle_name,)
            user.last_name = (last_name,)
            user.mobile = (mobile,)
            user.email = (email,)
            user.password_hash = (password_hash,)
            user.intro = (intro,)
            user.profile = (profile,)
            user.role_id = role_id

            session.commit()

            stmt = select(User).where(User.id == id)
            data = session.execute(stmt).scalar()

        return data

    # @staticmethod
    # def update_user_and_username(
    #     username=str, new_username=str, email=str, name=str
    # ) -> User:
    #     with Session() as session:
    #         stmt = select(User).where(User.username == username, User.status == True)
    #         user = session.execute(stmt).scalar()

    #         # updated data
    #         user.username = new_username
    #         user.email = email
    #         user.name = name
    #         session.commit()

    #         stmt = select(User).where(User.username == new_username)
    #         data = session.execute(stmt).scalar()

    #     return data

    # @staticmethod
    # def update_password(username=str, new_password=str) -> None:
    #     with Session() as session:
    #         stmt = select(User).where(User.username == username, User.status == True)
    #         user = session.execute(stmt).scalar()

    #         # updated data
    #         user.password = new_password
    #         session.commit()

    @staticmethod
    def soft_delete_user(user_id: int) -> None:
        with Session() as session:
            stmt = select(User).where(User.id == id, User.active == 1)
            user = session.execute(stmt).scalar()

            # updated data
            user.active = 0
            user.deleted_at = datetime.now()
            session.commit()
