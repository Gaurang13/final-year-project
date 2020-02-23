import difflib
import pandas as pd
from ..models import MysqlDatabaseHandler, set_text
from ...common import BadRequestError, get_utc_datetime, CommandIdEnum
from ...common.errors import errors
from pymysql import IntegrityError
from ...files import question_file
from datetime import date, datetime, time


class TextProcessing:
    def __init__(self, message):
        self.message = message
        self.message.text_id = None
        self.message.current_timestamp = get_utc_datetime()
        self.message.command_id = None
        self.message.response = {}

    def process_text(self):
        """This method is used to processing incoming request text.Give the instruction what have to do next"""

        try:
            with MysqlDatabaseHandler() as conn:
                set_text(conn, self.message)
                conn.commit()
                self.abstract_text()
        except IntegrityError:
            error = errors['BadRequestError']
            error['message'] = "user_not_exist"
            raise BadRequestError(error)

    def abstract_text(self):
        dataset = pd.read_csv(question_file)
        index = 0
        max = 0
        seq = difflib.SequenceMatcher(None, "object near to me", self.message.text)
        seq1 = difflib.SequenceMatcher(None, "object surronding  me", self.message.text)
        seq_ratio = seq.ratio() * 100
        seq1_ratio = seq1.ratio() * 100

        if seq_ratio > 85 or seq1_ratio > 85:

            self.message.command_id = CommandIdEnum.CAPTURE_IMAGE.values

        else:
            for i in range(1, len(dataset)):
                dataset_text = dataset['Question'][i]
                seq = difflib.SequenceMatcher(None, dataset_text, self.message.text)
                match_ratio = seq.ratio() * 100
                if max < match_ratio:
                    max = match_ratio
                    index = i
            if max > 60 and index > 16:
                max2 = 0
                for i in range(17, len(dataset)):
                    dataset_text = dataset['Question'][i]
                    seq = difflib.SequenceMatcher(None, dataset_text, self.message.text)
                    match_ratio = seq.ratio() * 100
                    print(dataset_text, seq, match_ratio)
                    if max2 < match_ratio:
                        max2 = match_ratio
                        index = i
                if max2 < 90:
                    self.wrong_text()
                else:
                    self.success_message_response(dataset['id'][index])
            else:
                if max > 60 and index <= 16:
                    value = int(dataset['id'][index])
                    if value == 1:
                        pass  # Object detection will use to detect all the object
                    if value == 2 or value == 5:
                        pass  # object_segmentation(b, index)
                    if value == 3:
                        pass
                    if value == 4:
                        pass
                    if value == 6:
                        pass
                    if value == 7:
                        self.success_message_response(datetime.now().time().strftime("%H:%M:%S"))
                    if value == 8:
                        self.success_message_response(date.today().strftime("%d/%m/%Y"))
                    if value == 9:
                        self.success_message_response(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                    if value == 10:
                        pass
                else:
                    self.wrong_text()

    def wrong_text(self):
        self.message.response = {
            "text": "Sorry!I can't understand",
            "text_id": self.message.text_id,
            "user_id": self.message.user_id,
            "status": "400"
        }

    def success_message_response(self, text):
        self.message.response = {
            "text": text,
            "text_id": self.message.text_id,
            "user_id": self.message.user_id,
            "status": "200"
        }
