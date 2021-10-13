from os import truncate
from typing import List, Optional
import boto3
from botocore.client import Config
import json


class StorageService:
    """S3操作クラス
    """

    def __init__(self) -> None:
        """コンストラクタ
        """
        self.client = boto3.client(
            "s3", config=Config(signature_version='s3v4'),)
        self.resource = boto3.resource("s3")

    def get_object(self, bucket: str, key: str) -> bytes:
        """S3からのファイル読み込み

        Parameters
        ----------
        bucket : str
            バケット名
        key : str
            オブジェクトキー

        Returns
        -------
        bytes
            読み込んだファイルのバイナリ
        """
        obj = self.client.get_object(Bucket=bucket, Key=key)
        return obj['Body'].read()

    def put_text_object(self, bucket: str, key: str, data_str: str) -> None:
        """ファイルアップロード（テキストデータ）

        Parameters
        ----------
        bucket : str
            バケット名
        key : str
            オブジェクトキー
        data_str : str
            テキストデータ
        """
        obj = self.resource.Object(bucket, key)
        obj.put(Body=data_str)

    def list_object_keys(self, bucket: str, prefix: str = "") -> List[str]:
        """S3のオブジェクトキーを一覧する

        Parameters
        ----------
        bucket : str
            バケット
        prefix : str, optional
            プレフィックス, by default ""

        Returns
        -------
        List[str]
            オブジェクトキー一覧
        """
        paginator = self.client.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket, Prefix=prefix)

        key_list: List[str] = []
        for page in page_iterator:
            # 1件もない場合はContentというKeyが無い
            if "Contents" in page:
                key_list += [
                    obj['Key']
                    for obj
                    in page["Contents"]
                    # ディレクトリを表すオブジェクトがあるので、それを除外
                    if obj['Key'].rfind("/") != len(obj['Key']) - 1
                ]
        return key_list
