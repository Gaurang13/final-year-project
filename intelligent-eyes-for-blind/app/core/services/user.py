from ...common import get_utc_datetime, BadRequestError
from ...common.errors import errors
from ..models import MysqlDatabaseHandler, set_user
from pymysql import IntegrityError
import re


def integrity_error_handler(e):

    message = e.args[1]
    uk_name = re.findall(r'uk\w+', message)
    error_list = ['uk_user_email', 'uk_user_phone_number']
    exception_dictionary = {
        error_list[0]: "duplicate_email",
        error_list[1]: "duplicate_phone_number"
    }
    error = errors['BadRequestError']
    error['message'] = exception_dictionary[uk_name[0]]
    return BadRequestError(error)


class UserHelper:
    def __init__(self, message):
        self.message = message
        self.message.current_timestamp = get_utc_datetime()
        self.message.user_response = None
        self.message.user_id = None

    def create_user(self):
        try:
            with MysqlDatabaseHandler() as conn:
                set_user(conn, self.message)
                conn.commit()
            self.message.user_response = {
                "user_id": self.message.user_id
            }
        except IntegrityError as e:
            exception = integrity_error_handler(e)
            raise exception
