# 開発中のデバッグ用スクリプト
# ファイル名はそのコードで確かめたい挙動で付けるといいんじゃなかろうか

import json
from test.utils.test_utility import TestUtility

from src.controllers.sample_controller import main
from src.models.sample_model import SampleInput, SampleOutput
from src.utils.common_utility import CommonUtility

# パラメータの生成
moji = "test"
suuji = 0
obj = SampleInput(suuji=suuji, message=moji)
args = json.dumps(obj.__dict__)

# 実行
main(args)

# 出力確認
output_str = TestUtility.read_output()
obj = CommonUtility.convert_dict_key(
    json.loads(output_str), CommonUtility.pascal_to_snake)
res = SampleOutput(**obj)
print(res)
