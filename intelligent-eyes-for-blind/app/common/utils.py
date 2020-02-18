from datetime import datetime
import pytz
import os
from io import StringIO
from configparser import ConfigParser
from .constants import (DT_FMT_ymdHMSf)


def read_properties_file(file_path):
    with open(file_path) as f:
        config = StringIO()
        config.write('[dummy_section]\n')
        config.write(f.read().replace('%', '%%'))
        config.seek(0, os.SEEK_SET)
        cp = ConfigParser()
        cp.read_file(config)
        return dict(cp.items('dummy_section'))


def get_current_timestamp(timezone=pytz.utc):
    return datetime.now(tz=timezone)


def datetime_to_str(date_time, str_format=DT_FMT_ymdHMSf):
    return date_time.strftime(str_format)


def str_to_datetime(date_time, str_format=DT_FMT_ymdHMSf):
    return datetime.strptime(date_time, str_format)


def get_utc_timestamp():
    return datetime_to_str(get_current_timestamp())


def get_utc_datetime():
    return datetime.now(tz=pytz.utc)