from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import validates
from db import Base, session


class Wish(Base):
    __tablename__ = "Wish"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    price = Column(Integer(), nullable=False)
    url = Column(String(256), nullable=False)
    note = Text()

    @validates("price")
    def validate_age(self, key, value):
        if value < 0:
            raise ValueError(f'Invalid price {value}')
        return value


def create_wish(title, price, url, note):
    new_wish = Wish(
        title=title,
        price=price,
        url=url,
        note=note
    )
    session.add(new_wish)
    session.commit()
    session.close()


def get_wish_by_id(wish_id) -> Wish:
    return session.query(Wish.title, Wish.price, Wish.url).get(wish_id)


def get_all_wishes():
    return session.query(Wish.id, Wish.title, Wish.price, Wish.url).all()


def delete_wish_by_id(wish_id):
    deletion_wish = session.query(Wish).get(wish_id)
    if deletion_wish:
        session.delete(deletion_wish)

    session.commit()
    session.close()


def update_wish_by_id(wish_id, title=None, price=None, url=None, note=None):
    wish_for_update = session.query(Wish).get(wish_id)
    if wish_for_update:
        if title:
            wish_for_update.title = title
        if price:
            wish_for_update.price = price
        if url:
            wish_for_update.url = url
        if note:
            wish_for_update.note = note

    session.add(wish_for_update)
    session.commit()
    session.close()
