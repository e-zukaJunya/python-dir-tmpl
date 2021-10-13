# バッチ用Pythonサンプル

過去案件でバッチを作成した際のものを参考にしたPython構成サンプル。

Pythonプロジェクト全般のディレクトリ・ファイル構成の1パターンとして参考に。

ちなみにargo workflowで実行できるサンプルである。

## 準備

- VSCode
- VSCode拡張
  - Remote-Containers

### .envの用意

このREADMEと同じディレクトリに.envという名前のファイルを作り、以下の内容を記載する。

文字コードがUTF-8以外だとだめなので注意。

```ini
# docker-compose プロジェクト名
COMPOSE_PROJECT_NAME="好きなプロジェクト名"

# AWS credentials
AWS_ACCESS_KEY_ID={自分のアクセスキーID}
AWS_SECRET_ACCESS_KEY={自分のシークレットアクセスキー}
AWS_DEFAULT_REGION="ap-northeast-1"
AWS_DEFAULT_OUTPUT="json"
```

### 開発環境の起動

※DBとかのコンテナはAPI側のdocker-composeで構築されるので、Pythonだけいじる人もVisualStudioからAPI側のコンテナ群を事前に起動しておくこと！

このディレクトリをルートとしてVSCodeで開き、Ctrl + Shift + p でコマンドパレットを開き、Reopen in Containerを選ぶ。

起動に失敗したようなダイアログが出ることがあるが、Retryするとうまく行くことが多い。

コンテナのセットアップには5分ほどかかる。

2021/10/4時点ではコンテナの初回起動時にはvscodeのpython拡張が再起動を必要とするので、拡張機能タブ開いてpython拡張のリロードボタンを押すと動かせる。

## 構成

- .devcontainer/: vscode devcontainerのための設定。
- .vscode/: vscodeの設定ファイル。
- debug/: 作った処理のデバッグ用ファイル。
  - modules/: モジュール単位
  - その他はバッチ単位
- develop/: 開発中に使用する便利なものを置く。今はjupyterのサンプルのみ。
- src/: 実際のバッチ処理。
  - constants/: 固定値系。
    - 各ファイルについてはファイル内のサンプルやコメント参照。
  - controllers/: C#のController的立場の、入出力部分。
  - decorators/: デコレータ。
  - logger/: ロガー。
  - models/: dataclass(C#でいうモデル)を配置。
  - services/: C#でいうService的立場のファイルを配置。外部とやり取りを行う共通モジュールも、Controllerと対応するserviceもどっちも置いてる。
  - utils/: 共通処理。
- test/: 各種テスト用コードを配置。
  - constants/: テスト用固定値。
  - steps/: ステップ単位のテスト用コードを配置。
  - utils/: テスト用ユーティリティクラス。

## デバッグ

VSCodeのデバッグ機能で今開いているファイルをエントリーポイントとしてデバッグ実行ができる。

このリポジトリの構成としては、debugディレクトリ以下にステップ単位かモジュールの単位かできって疎通用ファイルを置いてデバッグ実行する感じ。

## ビルド

docker-compose.build.yml, Dockerfile.buildがビルド用。

```sh
docker-compose -f docker-compose.build.yml build
```

## テスト

test/steps/以下に各ステップ用のディレクトリを切ってテストコードを作成する。

実装例についてはサンプル参照。

demo/以下がpytest一般、sample/以下がsample関連の実装を例にした実際のっぽいテストコード

### 個別実行

個別にはVS CodeのGUIテストツールを使用

### 全体実行

下記コマンドでテスト全体を実行できる

vscodeの左のメニューのフラスコマークがテストツール

```bash
pipenv run test
```

実行後は遅い順に10個のテストの処理が表示される。

テストのパフォーマンスが落ちている場合はそれらを参考に。

## Todo

- DI
- mypyによる型チェック

## Tips

### docker コマンドメモ

```sh
docker-compose up

docker-compose down -v

docker-compose down -v --rmi local --remove-orphans
```
