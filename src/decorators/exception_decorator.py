import traceback
from typing import Callable

from src.logger.custom_logger import CustomLogger


def common_exception(logger: CustomLogger):
    """引数を受け取るためのラッパー

    Parameters
    ----------
    logger : CustomLogger
        ロガー
    """
    def _common_exception(func: Callable):
        """共通例外処理

        Parameters
        ----------
        func : Callable
            これをデコレータとして利用している関数自体
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.common_error(e, traceback.format_exc())
                # フロー自体は例外が起きたら異常終了させたいため、ここでraise
                raise(e)
        return wrapper

    return _common_exception
