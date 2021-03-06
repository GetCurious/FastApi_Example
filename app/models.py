# SQLAlchemy Models for Alembic (migration)
# These are for creating Database Table

# Think Java Model for Hibernate


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    # id, email, hashed_password, is_active will be stored in "Users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # items will be stored in "item" table under "owner" column
    items = relationship("Item", back_populates="owner")
    # relationship expects Class name instead of __tablename__


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
