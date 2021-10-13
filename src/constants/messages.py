# メッセージ定義

class Msgs():
    """
    メッセージ本体
    """
    def START(process): return f"{process} 開始"
    def END(process): return f"{process} 終了"
    def ERROR(process): return f"{process} 失敗"


class Words():
    """
    単語
    """
    TANGO = "単語"
