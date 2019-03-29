#!/usr/bin/env python3
# coding: utf-8
# File: chatBot.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 19-3-29

import urllib.request
from urllib.parse import quote_plus
from lxml import etree
import json

class ZhidaoChatbot:
    def __init__(self):
        return

    '''获取搜索页'''
    def get_html(self, url):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17"}
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        return html


    '''采集问答首页'''
    def collect_urls(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        questions = [i.xpath('string(.)').replace('搜狗问问','').replace('搜狗', '').replace('-','') for i in selector.xpath('//div[@class="vrwrap"]/h3[@class="vrTitle"]/a')]
        links = ['https://wenwen.sogou.com/z/' + i.split('.htm&')[0].split('2F')[-1] + '.htm' for i in selector.xpath('//div[@class="vrwrap"]/div/a/@href')]
        pairs = list(zip(questions, links))
        return pairs[:3]

    '''采集答案'''
    def parser_answer(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        answers = [i.xpath('string(.)').replace('\u3000','').replace('\n', '').replace('\xa0', '').replace(' ', '。').replace('\r', '') for i in selector.xpath('//pre')]
        answers = [i for i in answers if '?' not in i and '？' not in i and len(set(i)) > 2 and '为什么' not in i]
        answer_dict = {answer:len(answer) for answer in answers}
        answers = [i[0] for i in sorted(answer_dict.items(), key=lambda asd:asd[1])]
        return answers

    '''收集答案'''
    def collect_answers(self, url):
        answers_all = []
        url_pairs = self.collect_urls(url)
        for question, answer_url in url_pairs:
            answers = self.parser_answer(answer_url)
            answers_all += answers
        answer_dict = {answer:len(answer) for answer in answers_all}
        best_answers = [i[0] for i in sorted(answer_dict.items(), key=lambda asd:asd[1])][:5]
        return best_answers

    '''扩展问句'''
    def expand_question(self, question):
        url = 'https://wenwenfeedapi.sogou.com/sgapi/web/related_search_new?key=' + quote_plus(question)
        data = json.loads(self.get_html(url))
        others = data["data"]
        return others

    '''问答'''
    def qa_main(self, question):
        url = 'https://www.sogou.com/sogou?query='+quote_plus(question) +'&ie=utf8&s_from=result_up&insite=wenwen.sogou.com'
        answers = self.collect_answers(url)
        other_questions = self.expand_question(question)
        return answers, other_questions

'''测试'''
def test():
    handler = ZhidaoChatbot()
    while 1:
        question = input('你的问题:').strip()
        answers, other_questions = handler.qa_main(question)
        print('回答:', answers)
        print('你可能还想问:', other_questions)
        print('*******'*6)

if __name__ == '__main__':
    test()



