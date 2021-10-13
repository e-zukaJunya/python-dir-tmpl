import traceback

from src.services.db_service import DbService

HOST = "mysql"
PORT = 3306
USER = "user"
PASSWORD = "pass"
DATABASE = "Test"


def success():
    db = DbService(HOST, PORT, USER, PASSWORD, DATABASE)

    with db.conn.cursor() as cur:
        query = "select * from m_user where user_id = %s"
        cur.execute(query, (1,))
        result = cur.fetchall()
        print("成功")
        print(result)


success()


def fail():
    try:
        db = DbService(HOST, PORT, USER, "fail", DATABASE)

        with db.conn.cursor() as cur:
            query = "select * from m_user where user_id = %s"
            cur.execute(query, (1,))
            result = cur.fetchall()
            print(result)
    except Exception as ex:
        print("正しく失敗した")
        print(ex)
        print(traceback.format_exc())


fail()
