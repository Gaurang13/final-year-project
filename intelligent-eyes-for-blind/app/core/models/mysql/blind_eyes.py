from .helper import execute_one, fetch_rows
from ...models import sql_scripts

__all__ = ['set_text', 'set_user']


def set_user(conn, message):
    """This method is used to enter data into user tabel"""
    row = execute_one(conn, params={
        "first_name": message.first_name,
        "last_name": message.last_name,
        "email": message.email,
        "phone_number": message.phone_number,
        "created_at": message.current_timestamp
    }, sql_stmt=sql_scripts['set_user'])
    if row:
        message.user_id = row['id']


def set_text(conn, message):
    """This method is used to insert data in text table"""

    row = execute_one(conn, params={
        "text": message.text,
        "user_id": message.user_id,
        "created_at": message.current_timestamp
    }, sql_stmt=sql_scripts['set_text'])
    if row:
        message.text_id = row['id']