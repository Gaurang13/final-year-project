import difflib
import pandas as pd
from ..models import MysqlDatabaseHandler, set_text
from ...common import BadRequestError, get_utc_datetime, CommandIdEnum
from ...common.errors import errors
from pymysql import IntegrityError
from ...files import question_file


class TextProcessing:
    def __init__(self, message):
        self.message = message
        self.message.text_id = None
        self.message.current_timestamp = get_utc_datetime()
        self.message.command_id = None

    def process_text(self):
        """This method is used to processing incoming request text.Give the instruction what have to do next"""

        try:
            with MysqlDatabaseHandler() as conn:
                set_text(conn, self.message)
                conn.commit()
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
                    a = dataset['Question'][i]
                    seq = difflib.SequenceMatcher(None, a, b)
                    d = seq.ratio() * 100
                    if max2 < d:
                        max2 = d
                        index = i
                if max2 < 90:
                    tts("sorry!i can't understand")
                else:
                    tts(dataset['id'][index])
            else:
                if max > 60 and index <= 16:
                    value = int(dataset['id'][index])
                    if value == 1:
                        object_detection(True)
                    if value == 2 or value == 5:
                        object_segmentation(b, index)
                    if value == 3:
                        action(index)
                    if value == 4:
                        action(index)
                    if value == 6:
                        action(index)
                    if value == 7:
                        # print(current_time1())
                        current_time1()
                    if value == 8:
                        current_date()
                    if value == 9:
                        current_date_and_time()
                    if value == 10:
                        action(index)
                else:
                    tts("sorry!i can't understand")

    def sequence_matcher(self):



