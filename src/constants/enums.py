# 列挙型を定義

class HogeType():
    """番号だけ定義しておけばいい場合
    """
    IKKOME = 0
    NIKOME = 1
    SANKOME = 1


class KeyAndVal():
    """番号と表示文字があるような場合
    """
    class Value:
        ADMIN = 0
        COMMON = 1

    class DispValue:
        ADMIN = "管理者"
        COMMON = "一般"
