import json
import os

import fire
from src.decorators.exception_decorator import common_exception
from src.logger.custom_logger import CustomLogger
from src.models.sample_model import SampleInput, SampleOutput
from src.services.sample_service import SampleService
from src.utils.common_utility import CommonUtility

# ロガーの取得
logger = CustomLogger(os.environ["LOG_LEVEL"])


@common_exception(logger)
def main(args: str) -> None:
    """Controller

    Parameters
    ----------
    args : str
        引数のJSON文字列
    """
    # 実行処理名としてファイル名を取得
    process_name = os.path.basename(__file__)
    req_id = os.environ["REQ_ID"]

    # ロガーのセットアップ
    logger.set_default_value(process_name, req_id)
    # 開始ログ
    logger.start()

    # 引数のJSON文字列をモデル(dataclass)に変換
    obj = json.loads(args)
    model = SampleInput(**obj)

    # 実際のバッチとしての処理
    main_service = SampleService()
    main_service.test()

    # 出力処理
    output = SampleOutput(id=model.suuji, name=model.message)
    CommonUtility.output_next_params(output)

    # 終了ログ
    logger.end()


if __name__ == "__main__":
    """サンプル
    """
    fire.Fire(main)
