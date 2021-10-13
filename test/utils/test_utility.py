
import os

from src.constants.constants import Paths


class TestUtility():
    """テスト用共通処理クラス
    """
    @classmethod
    def read_output(cls) -> str:
        """各ステップで出力したアウトプットを読み込み

        Returns
        -------
        str
            アウトプットの内容
        """
        with open(Paths.OUTPUT) as f:
            s = f.read()
        return s

    @classmethod
    def delete_output(cls) -> None:
        """各ステップで出力したアウトプットを削除
        """
        if os.path.isfile(Paths.OUTPUT):
            os.remove(Paths.OUTPUT)
