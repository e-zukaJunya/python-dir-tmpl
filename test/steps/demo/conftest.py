import pytest

# conftest.pyという名前のファイルは自動で読み込まれてそのディレクトリ以下に自動で適用される
# "yield"の前が前処理、後が後処理になる

# @pytest.fixture(scope="session", autouse=True)
# # テスト全体で一度実行
# def session_f():
#     print("session fixture pre")
#     yield
#     print("session fixture post")


@pytest.fixture(scope="module", autouse=True)
# ファイル単位で一度実行(このコメントはコピペしてかないで)
def module_f():
    print("module fixture pre")
    yield
    print("module fixture post")


@pytest.fixture(scope="class", autouse=True)
# クラス単位で一度実行(このコメントはコピペしてかないで)
def class_f():
    print("class fixture pre")
    yield
    print("class fixture post")


@pytest.fixture(scope="function", autouse=True)
# 関数単位で一度実行(このコメントはコピペしてかないで)
def func_f():
    print("function fixture pre")
    yield
    print("function fixture post")
