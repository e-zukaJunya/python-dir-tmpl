import json
import os
from logging import ERROR, INFO, Formatter, StreamHandler, getLogger

from src.constants.messages import Msgs
from src.utils.datetime_utility import DatetimeUtility


class CustomJsonFormatter(Formatter):
    """ログフォーマット用クラス
    """

    def format(self, record):
        """ログ出力フォーマットの定義
        """
        msg = record.__dict__.get("log_message")
        format_dict = {
            # ログレベル
            "Level": record.levelname,
            # 本システムのログであることを示すコード
            "SysCode": record.__dict__.get("sys_code"),
            # APIやバッチの名称（論理名でなく何かの物理名で取るのが良い）
            "ProcessName": record.__dict__.get("process_name"),
            # 実行要求をを一意に識別するID
            "ReqId": record.__dict__.get("req_id"),
            # ログ本文
            "Message": msg,
            # 出力日時
            "Time": record.__dict__.get("time"),
            # 最終コミットハッシュ
            "LatestCommit": record.__dict__.get("latest_commit"),
        }

        return f"{msg}\n{json.dumps(format_dict, ensure_ascii=False)}"


class CustomLogger:
    """ロガー
    """

    def __init__(self, log_level: str):
        """コンストラクタ

        Parameters
        ----------
        log_level : str
            ログレベル
        """

        # loggerオブジェクトの宣言
        self.logger = getLogger()

        # 親Loggerオブジェクトにログ出力イベントを渡さないように設定(カスタムロガーで出力したログをrootロガーで再度出力しない)
        self.logger.propagate = False

        # loggerのログレベル設定(ハンドラに渡すエラーメッセージのレベル)
        self.logger.setLevel(log_level)

        # handlerの生成
        sh = StreamHandler()

        # handlerにログ出力フォーマットを設定
        formatter = CustomJsonFormatter()
        sh.setFormatter(formatter)

        # loggerにhandlerをセット
        self.logger.addHandler(sh)

        # ログ出力用固定値
        self.sys_code = "my_system"
        self.process_name = None
        self.req_id = None
        self.latest_commit = os.environ["LATEST_COMMIT"]

    def set_default_value(self, process_name: str, req_id: str):
        """ログ出力用固定値のセット

        Parameters
        ----------
        process_name : str
            処理名
        req_id : str
            実行要求ID
        """

        self.process_name = process_name
        self.req_id = req_id

    def output_log(self, log_level: int, msg: str):
        """ログ出力

        Parameters
        ----------
        log_level : int
            ログレベル
        msg : str
            ログメッセージ
        """
        log_content = {
            "sys_code": self.sys_code,
            "process_name": self.process_name,
            "req_id": self.req_id,
            "log_message": msg,
            "time": str(DatetimeUtility.get_datetime_now()),
            "latest_commit": self.latest_commit,
        }

        self.logger.log(log_level, "", extra=log_content)

    def start(self):
        """開始ログ
        """
        self.output_log(INFO, Msgs.START(self.process_name))

    def end(self):
        """終了ログ
        """
        self.output_log(INFO, Msgs.END(self.process_name))

    def common_error(self, error_message: str, stack_trace: str):
        """共通エラーログ

        Parameters
        ----------
        error_message : str
            ログ本文
        stack_trace : str
            スタックトレース
        """
        # ステップが失敗した旨を出力
        self.output_log(ERROR, Msgs.ERROR(self.process_name))
        # エラーメッセージとスタックトレースを出力
        self.output_log(ERROR, f"{error_message}\n{stack_trace}")
