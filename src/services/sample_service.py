class SampleService:
    """サンプルサービス
    """

    def __init__(self) -> None:
        """コンストラクタ
        """
        # メンバ変数の作り方
        self.member = "sample member"

    def test(self):
        """実際のバッチ固有の処理
        """
        # メンバ変数参照
        print(self.member)

        return
