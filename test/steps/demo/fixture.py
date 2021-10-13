import pytest

# 関数個別に適用するfixture


@pytest.fixture
def individual_f():
    print("individual fixture pre")
    yield
    print("individual fixture post")
