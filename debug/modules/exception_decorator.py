import os

from src.decorators.exception_decorator import common_exception
from src.logger.custom_logger import CustomLogger

# ロガーの取得
logger = CustomLogger(os.environ["LOG_LEVEL"])

# region 例外デコレーターのテスト


@common_exception(logger)
def for_ex_decorator():
    # ロガーのセットアップ
    process_name = "test_func"
    logger.set_default_value(process_name)
    # 0で割り算を行って例外を発生させている
    zero = 0
    num = 1 / zero


def test_common_exception():
    try:
        # 実際にデコレーターを付けた関数を実行
        for_ex_decorator()
    except Exception as ex:
        # 例外がここまで送出されていれば正しい
        print("例外が発生")


# 例外デコレーターのテスト
test_common_exception()
# endregion
