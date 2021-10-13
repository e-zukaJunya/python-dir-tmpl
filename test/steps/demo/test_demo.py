from test.steps.demo.fixture import individual_f

import pytest

# ファイル名に"test_"というprefixを付けることでテストコードがあるファイルと認識される


def test_only_func(individual_f):
    # 関数名に"test_"というprefixを付けることでテストと認識される
    # 引数にfixtureを入れることでそのfixtureが適用される
    a = 1
    assert a == 1


numeric_datas = [
    (2, 5, 10),
    (3, 6, 18),
    (5, 9, 45)
]


class TestGroup():
    # クラス名に"Test"というprefixを付けることでテストと認識される
    # 内部の関数も同様
    def test_in_class(self):
        a = 1
        assert a == 1

    # 複数パラメータのパターンでテストしたい場合
    @pytest.mark.parametrize("a, b, expect", numeric_datas)
    def test_with_params(self, a, b, expect):
        print(a, b, expect)
        a = True
        assert a
