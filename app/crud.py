# Think Java DAO

from sqlalchemy.orm import Session

from app import interface, models


# User
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: interface.UserCreate):
    # TODO hashing feature
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email,
                          hashed_password=fake_hashed_password)
    db.add(db_user)
    # commit to save the data
    db.commit()
    # refresh for new generated ID
    db.refresh(db_user)
    return db_user


# Item
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item_by_title(db: Session, title: str):
    return db.query(models.Item).filter(models.Item.title == title).first()


def create_user_item(db: Session,
                     item: interface.ItemCreate,
                     user_id: int):
    # **item.dict() instead of reading one by one
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
