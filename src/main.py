import re
import urllib.request
from argparse import ArgumentParser

from dotenv import load_dotenv
from tinysegmenter import TinySegmenter

from lib import x_api


class CommonKeywordDataset:
    def __init__(self):
        self.user1 = None
        self.user2 = None
        self.tweets1 = []
        self.tweets2 = []

        self._load_metadata()

    def _load_metadata(self):
        if args.mock:
            self.user1 = "634829374928374657"
            self.user2 = "783295847239182374"
            get_posts_method = x_api.get_user_posts_mock
        else:
            self.user1 = args.user1
            self.user2 = args.user1
            get_posts_method = x_api.get_user_posts
        self.tweets1 = [extract_post_text(t.text) for t in get_posts_method(self.user1).data]
        self.tweets2 = [extract_post_text(t.text) for t in get_posts_method(self.user2).data]


# 日本語ストップワードを取得（GitHubのstopwords-jaを使用）
def load_stopwords():
    url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-ja/master/stopwords-ja.txt"
    response = urllib.request.urlopen(url)
    return set(response.read().decode("utf-8").splitlines())


# 共通キーワード抽出関数
def extract_common_keywords(texts1, texts2, top_n=10):
    stopwords_ja = load_stopwords()
    segmenter = TinySegmenter()
    tokens1 = segmenter.tokenize(" ".join(texts1))
    tokens2 = segmenter.tokenize(" ".join(texts2))
    keywords1 = [t for t in tokens1 if t not in stopwords_ja and len(t.strip()) > 1]
    keywords2 = [t for t in tokens2 if t not in stopwords_ja and len(t.strip()) > 1]
    return list(set(keywords1) & set(keywords2))[:top_n]


# テキスト前処理
def extract_post_text(text):
    text = re.sub(r"http\S+", "", text)  # URL削除
    text = re.sub(r"[@#]\S+", "", text)  # @メンションや#ハッシュタグ削除
    return text.lower()


def parse_args():
    parser = ArgumentParser(description="オモイアイ 共通点発見ツール")

    parser.add_argument("--mock", action="store_true", help="モックデータを使用する")

    parser.add_argument("--user1", type=str, help="一人目のXのユーザー名")
    parser.add_argument("--user2", type=str, help="二人目のXのユーザー名")

    args = parser.parse_args()

    # バリデーション
    if args.mock:
        # モック使用時は他の引数を指定してはいけない
        if any([args.user1, args.user2]):
            parser.error("--mock を指定した場合、--user1、--user2 は指定できません。")
    else:
        # 実データ使用時は全ての引数が必要
        missing = [opt for opt in ["user1", "user2"] if getattr(args, opt) is None]
        if missing:
            parser.error(f"--mock を使わない場合、以下の引数が必要です: {', '.join('--' + m for m in missing)}")

    return args


def main():
    print("共通のキーワードを抽出中...")
    dataset = CommonKeywordDataset()
    keywords = extract_common_keywords(dataset.tweets1, dataset.tweets2)
    print(f"\n🧩 {dataset.user1} さんと {dataset.user2} さんの共通トピック候補：")
    print(keywords)


if __name__ == "__main__":
    load_dotenv()
    args = parse_args()
    main()
