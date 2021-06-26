# !/usr/bin/nev python
# -*-coding:utf8-*-


import tkinter as tk
import os
from lxml import etree
from xpinyin import Pinyin
from requests_html import HTMLSession
session = HTMLSession()


class BATSpider(object):

    def __init__(self):
        """定义可视化窗口，并设置窗口和主题大小布局"""
        self.window = tk.Tk()
        self.window.title('爬取彼岸图4k壁纸')
        self.window.geometry('800x600')

        """创建label_user按钮，与说明书"""
        self.label_user = tk.Label(self.window, text='输入需要爬取的壁纸类型（风景，美女，游戏，动漫，影视，明星，汽车，动物，人物，美食，宗教，背景）：',
                                   font=('Arial', 12), width=130, height=2)
        self.label_user.pack()
        """创建label_user关联输入"""
        self.entry_user = tk.Entry(self.window, show=None, font=('Arial', 14))
        self.entry_user.pack(after=self.label_user)

        """创建label_passwd按钮，与说明书"""
        self.label_passwd = tk.Label(self.window, text="爬取多少页：", font=('Arial', 12), width=30, height=2)
        self.label_passwd.pack()
        """创建label_passwd关联输入""
