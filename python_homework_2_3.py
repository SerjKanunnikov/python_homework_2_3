import json
import chardet


def import_json_news():
    """Импорт новостей из json-файла"""
    with open("newsafr.json", "rb") as news:
        data = news.read()
        result = chardet.detect(data)
        news_feed = json.loads(data.decode(result["encoding"]))
        return news_feed


def parse_news(news_feed):
    """Разбор текстов новостей"""
    parsed_description = []
    for line in news_feed["rss"]["channel"]["items"]:
        parsed_description.append(line["description"].split(" "))
    return parsed_description


def word_sorting(parsed_description):
    """Поиск слов длиной больше 6 символов"""
    words_longer_than_six = []
    for article in parsed_description:
        for word in article:
            if len(word) >= 6:
                words_longer_than_six.append(word)
    return words_longer_than_six


def word_counter(words_longer_than_six):
    top_ten_words = {}
    popular_words = {word: int(words_longer_than_six.count(word)) for word in words_longer_than_six}
    popular_words_sorted = sorted(popular_words.items(), key=lambda word: word[1], reverse=True)
    top_ten_words.update(popular_words_sorted[0:9])
    print("Десять самых популярных слов:")
    for word, word_count in top_ten_words.items():
        print("Слово \"{}\" — {} вхождений".format(word, word_count))

word_counter(word_sorting(parse_news(import_json_news())))
