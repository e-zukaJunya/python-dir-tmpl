from src.constants.constants import Paths
from dataclasses import asdict, dataclass
from typing import Any, Callable, Dict
import json
import re
import string


class CommonUtility():
    @classmethod
    def output_next_params(cls, obj: dataclass) -> None:
        """ジョブの出力を行う

        Parameters
        ----------
        obj : Dict
            ジョブの出力とする辞書オブジェクト
        """
        with open(Paths.OUTPUT, mode='w') as f:
            # アウトプットする辞書のキーをパスカルケースに変換して出力
            output_dict = cls.convert_dict_key(
                asdict(obj), cls.snake_to_pascal)
            output = json.dumps(output_dict)
            f.write(output)

    @classmethod
    def pascal_to_snake(cls, s: str) -> str:
        """パスカルケースをスネークケースに変換

        Parameters
        ----------
        s : str
            パスカルケース文字列

        Returns
        -------
        str
            スネークケース文字列
        """
        return re.sub(
            "((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))",
            r"_\1",
            s).lower()

    @classmethod
    def snake_to_pascal(cls, s: str) -> str:
        """スネークケースをパスカルケースに変換

        Parameters
        ----------
        s : str
            スネークケース文字列

        Returns
        -------
        str
            パスカルケース文字列
        """
        return string.capwords(s.replace("_", " ")).replace(" ", "")

    @classmethod
    def convert_dict_key(cls, d: Dict, conv: Callable[[str], str]) -> Dict:
        """辞書のキーのケースを変換

        Parameters
        ----------
        d : Dict
            変換対象の辞書
        conv : Callable[[str], str]
            ケースを変換するメソッド

        Returns
        -------
        dict
            変換後の辞書
        """
        def convert_value(v: Any) -> Any:
            """辞書の値がlistやdictだった場合、中のキーを変換する処理

            Parameters
            ----------
            v : Any
                辞書のvalue

            Returns
            -------
            Any
                変換後のvalue
            """
            return (
                convert_dict_key(v, conv)
                if isinstance(v, dict)
                else [convert_value(e) for e in v]
                if isinstance(v, list)
                else v
            )

        return {conv(k): convert_value(v) for k, v in d.items()}
