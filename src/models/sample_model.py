from dataclasses import dataclass


@dataclass
class SampleInput():
    """サンプルの入力
    """
    # 実際は各引数にコメントつけてね
    message: str
    suuji: int


@dataclass
class SampleOutput():
    """サンプルの出力
    """
    id: int
    name: str
