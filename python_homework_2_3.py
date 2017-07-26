import json
from pprint import pprint


def import_json_news():
    with open("newsafr.json", "r") as news:
        news_feed = json.load(news)
        return news_feed


def parse_news(news_feed):
    parsed_description = []
    for line in news_feed["rss"]["channel"]["items"]:
        # print(line["description"])
        parsed_description.append(line["description"].split(" "))
    return parsed_description


def word_sorting(parsed_description):
    words_longer_than_six = []
    for article in parsed_description:
        for word in article:
            if len(word) >= 6:
                words_longer_than_six.append(word)
    # print(words_longer_than_six)
    return words_longer_than_six


def word_counter(words_longer_than_six):
    print(type(words_longer_than_six))
    sorted_words = sorted(words_longer_than_six)
    print(sorted_words)
    # print(words_longer_than_six)
    # print(words_longer_than_six.sort())

word_counter(word_sorting(parse_news(import_json_news())))
