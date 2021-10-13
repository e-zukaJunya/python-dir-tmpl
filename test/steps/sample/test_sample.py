import json
from logging import INFO
from test.utils.test_utility import TestUtility

from src.constants.messages import Msgs
from src.controllers.sample_controller import main
from src.models.sample_model import SampleInput, SampleOutput
from src.utils.common_utility import CommonUtility


class TestSample():
    def test_aaa(self, caplog):
        # caplogの設定（ログ確認用）
        caplog.set_level(INFO)

        # パラメータの生成
        moji = "test"
        suuji = 0
        obj = SampleInput(suuji=suuji, message=moji)
        args = json.dumps(obj.__dict__)

        # 実行
        main(args)

        # 出力された結果の取得
        output_str = TestUtility.read_output()
        obj = CommonUtility.convert_dict_key(
            json.loads(output_str), CommonUtility.pascal_to_snake)
        res = SampleOutput(**obj)
        print(res)

        # 結果の検証
        expect = SampleOutput(id=suuji, name=moji)
        assert res.id == expect.id
        assert res.name == expect.name

        # 開始ログの出力確認
        assert caplog.records[0].log_message == Msgs.START("sample_controller.py")

        # 終了ログの出力確認
        assert caplog.records[1].log_message == Msgs.END("sample_controller.py")
