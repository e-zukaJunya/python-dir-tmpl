import pymysql


class DbService:
    """RDB操作クラス
    """

    def __init__(
            self,
            host: str,
            port: int,
            user: str,
            password: str,
            database: str) -> None:
        """コンストラクタ

        Parameters
        ----------
        host : str
            ホスト名
        port : int
            ポート
        user : str
            ユーザー名
        password : str
            パスワード
        database : str
            DB名
        """
        self.conn = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )

    def __del__(self):
        """デストラクタ
        """
        # このクラスからのインスタンス初期化の際に接続で失敗してるとconnectionオブジェクト無いので、その場合を回避
        if hasattr(self, "conn"):
            # 接続のクローズ
            self.conn.close()
