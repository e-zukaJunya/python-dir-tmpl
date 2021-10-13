import json
from pprint import pprint

from src.services.storage_service import StorageService


# region オブジェクトキー一覧
# オブジェクトキー一覧 バケットのみ指定
def listBucketLevel():
    bucket = "e-zuka-anything-test"
    storage = StorageService()
    res = storage.list_object_keys(bucket)
    pprint(len(res))


listBucketLevel()


# オブジェクトキー一覧 プレフィックス指定
def listPrefixLevel():
    bucket = "e-zuka-anything-test"
    prefix = "nest"
    storage = StorageService()
    res = storage.list_object_keys(bucket, prefix)
    pprint(res)


listPrefixLevel()


# オブジェクトキー一覧 ファイル無し(0件)
def listNoFiles():
    bucket = "e-zuka-anything-test"
    prefix = "zero"
    storage = StorageService()
    res = storage.list_object_keys(bucket, prefix)
    pprint(res)


listNoFiles()


# オブジェクトキー一覧 1000以上
def listThousandFiles():
    bucket = "e-zuka-anything-test"
    prefix = "page_test"
    storage = StorageService()
    res = storage.list_object_keys(bucket, prefix)
    pprint(len(res))


listThousandFiles()


# オブジェクトキー一覧 バケット無し
def listObjectsFail():
    try:
        bucket = "naibacket"
        prefix = "page_test"
        storage = StorageService()
        res = storage.list_object_keys(bucket, prefix)
        pprint(res)
    except Exception as ex:
        print("正常に失敗")
        print(ex)


listObjectsFail()

# endregion


# region ファイル読み込み
# ファイル読み込み バケットあり ファイルあり
def getJson():
    bucket = "e-zuka-anything-test"
    key = "nest/inline.json"
    storage = StorageService()
    res = storage.get_object(bucket, key)
    data = json.loads(res.decode("utf-8"))
    pprint(data)


getJson()


# ファイル読み込み バケットあり ファイル無し
def getJsonFail():
    try:
        bucket = "e-zuka-anything-test"
        key = "nai.json"
        storage = StorageService()
        res = storage.get_object(bucket, key)
        data = json.loads(res.decode("utf-8"))
        pprint(data)
    except Exception as ex:
        print("正常に失敗")
        print(ex)


getJsonFail()


# ファイル読み込み バケット無し ファイルあり
def getJsonFailNoBucket():
    try:
        bucket = "naibucket"
        key = "nest/inline.json"
        storage = StorageService()
        res = storage.get_object(bucket, key)
        data = json.loads(res.decode("utf-8"))
        pprint(data)
    except Exception as ex:
        print("正常に失敗")
        print(ex)


getJsonFailNoBucket()
# endregion


# region ファイル書き込み
# ファイル書き込み バケットあり
def putObject():
    bucket = "e-zuka-anything-test"
    key = "upload/upload_test.json"
    storage = StorageService()
    test_data = {"id": 0, "name": "e-zuka!"}
    json_str = json.dumps(test_data)
    storage.put_text_object(bucket, key, json_str)


putObject()


# ファイル書き込み バケット無し
def putObjectFail():
    try:
        bucket = "naibacket"
        key = "upload/upload_test.json"
        storage = StorageService()
        test_data = {"id": 0, "name": "e-zuka!"}
        json_str = json.dumps(test_data)
        storage.put_text_object(bucket, key, json_str)
    except Exception as ex:
        print("正常に失敗")
        print(ex)


putObjectFail()
# endregion
