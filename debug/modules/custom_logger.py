import os
import traceback
from logging import WARN

from src.logger.custom_logger import CustomLogger

logger = CustomLogger(os.environ["LOG_LEVEL"])
service_name = "logger_test"
req_id = "test_req"
logger.set_default_value(service_name, req_id)

logger.start()
logger.end()
logger.output_log(WARN, "警告ログ")

try:
    zero = 0
    div = 1/zero
except Exception as ex:
    logger.common_error(ex.args[0], traceback.format_exc())
