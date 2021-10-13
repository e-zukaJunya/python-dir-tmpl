from datetime import datetime

import pytz


class DatetimeUtility:
    """日付操作クラス
    """
    @classmethod
    def get_datetime_now(cls) -> datetime:
        """現在日時(JST)を返却する

        Returns
        -------
        datetime
            現在日時(JST)
        """
        return datetime.now(pytz.timezone('Asia/Tokyo'))
