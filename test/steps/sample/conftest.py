import pytest


@pytest.fixture(scope="module", autouse=True)
# ファイル単位で一度実行(このコメントはコピペしてかないで)
def module_f():
    print("module fixture pre")
    yield
    print("module fixture post")


@pytest.fixture(scope="function", autouse=True)
# 関数単位で一度実行(このコメントはコピペしてかないで)
def func_f():
    print("function fixture pre")
    yield
    print("function fixture post")
