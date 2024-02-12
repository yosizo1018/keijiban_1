import requests
import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#トップページ
orange_color = "#FF4500"

#ヘッダー部品
col1,col2,col3 = st.columns(3)
with col1:st.link_button("板一覧:cactus:", "https://itest.5ch.net/#")
with col2:st.subheader('itest.5ch.net')
with col3:st.link_button("設定:gear:", "https://itest.5ch.net/setting")

#タイトル
coll1,coll2,coll3 = st.columns(3)
with coll2:st.image('./data/5ch.png', width=250)

#サイト概要
st.text('話題を検索')
st.caption('「ハッキング」から「今晩のおかず」までを手広くカバーする巨大掲示板群 『５ちゃんねる』へようこそ！')
colll1,colll2,colll3 = st.columns(3)
with colll3:st.markdown(f'[<span style="color:{orange_color};">使い方を見る</span>](https://info.5ch.net/index.php/Guidel)', unsafe_allow_html=True)

#検索窓の実装
col4,col5 = st.columns(2)
with col4:
    search_info_w = st.text_input("", placeholder="話題を検索")
with col5:
    st.text('')
    st.text('')
    search_info = st.button('検索')
if search_info:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #Chromeを使える状態にする
    driver = webdriver.Chrome(options=options)
    #自動表示したいURLを指定して表示する
    url = "https://itest.5ch.net/"
    driver.get(url)
    #pathを指定する
    #ターゲットは、検索窓のinput箇所
    form = driver.find_element(By.XPATH, '//*[@id="search_input_text"]')
    form.send_keys("search_input_text")
    form.submit()
    driver.close()

#大分類用"url"と"topics"をまとめた
news_url = "https://itest.5ch.net/topics/news"
population_url = "https://itest.5ch.net/topics/popular"
new_arrival_url = "https://itest.5ch.net/topics/new"
live_url = "https://itest.5ch.net/topics/live"
views_history_url = "https://itest.5ch.net/histories"
threads_url = "https://itest.5ch.net/histories"
urls = [news_url, population_url, new_arrival_url,live_url,views_history_url, threads_url]
topics = ['ニュース', '人気', '新着', '実況', '閲覧履歴', '板一覧']

#大分類("emoji"を使ってクオリティを本物に近づける)
colu1,colu2,colu3 = st.columns(3)
with colu1:
    st.link_button("ニュース:earth_americas:", news_url)
    st.link_button("実況:desktop_computer:", live_url)
with colu2:
    st.link_button("人気:boom:", population_url)
    st.link_button("閲覧履歴:clock3:", views_history_url)
with colu3:
    st.link_button("新着:signal_strength:", new_arrival_url)
    st.link_button("板一覧:cactus:", threads_url)

#謎の言葉
st.markdown('<span style="background-color:pink;"><a href="https://uplift.5ch.net/">UPLIFTで 広告なしで体験しましょう！快適な閲覧ライフをお約束します！</a></span>', unsafe_allow_html=True)

#大分類の各記事Top5をスクレイピングで表示させていく
#"ニュース"見出し
st.markdown(f'[<span style="color:{orange_color};">ニュース</span>]({news_url})', unsafe_allow_html=True)
r = requests.get(news_url)
soup = BeautifulSoup(r.text, "html.parser")
#テキスト取得
news_list = [i.text for i in soup.find_all('div', class_="news_title")]
#url取得
news_urls = [i.get('href') + "?v=pc" for i in soup.find_all('a')]
#５回"for文"を回してリンク付きテキストを表示させる
for i, j in zip(news_list[:5], news_urls[11:16]):
    st.link_button(i, j)
colulu1 = st.columns(3)
with colulu1[2]:
    st.markdown(f'[<span style="color:{orange_color};">ニュースをもっと見る</span>]({news_url})', unsafe_allow_html=True)

#"人気"見出し
st.markdown(f'[<span style="color:{orange_color};">人気</span>]({population_url})', unsafe_allow_html=True)
r2 = requests.get(population_url)
soup2 = BeautifulSoup(r2.text, "html.parser")
#テキスト取得
populations_list = [i.text for i in soup2.find_all('div', class_="news_title")]
#url取得
population_urls = [i.get('href') + "?v=pc" for i in soup2.find_all('a')]
#５回"for文"を回してリンク付きテキストを表示させる
for i, j in zip(populations_list[:5], new_arrival_url[11:16]):
    st.link_button(i, j)
colulu2 = st.columns(3)
with colulu2[2]:
    st.markdown(f'[<span style="color:{orange_color};">人気をもっと見る</span>]({population_url})', unsafe_allow_html=True)

#"新着"見出し
st.markdown(f'[<span style="color:{orange_color};">新着</span>]({new_arrival_url})', unsafe_allow_html=True)
r3 = requests.get(new_arrival_url)
soup3 = BeautifulSoup(r3.text, "html.parser")
#テキスト取得
new_arrival_list = [i.text for i in soup3.find_all('div', class_="news_title")]
#url取得
new_arrival_urls = [i.get('href') + "?v=pc" for i in soup3.find_all('a')]
#５回"for文"を回してリンク付きテキストを表示させる
for i, j in zip(new_arrival_list[:5], new_arrival_urls[11:16]):
    st.link_button(i, j)
colulu3 = st.columns(3)
with colulu3[2]:
    st.markdown(f'[<span style="color:{orange_color};">新着をもっと見る</span>]({new_arrival_url})', unsafe_allow_html=True)

#実況"見出し
st.markdown(f'[<span style="color:{orange_color};">実況</span>]({live_url})', unsafe_allow_html=True)
r4 = requests.get(live_url)
soup4 = BeautifulSoup(r4.text, "html.parser")
#テキスト取得
live_list = [i.text for i in soup4.find_all('div', class_="news_title")]
#url取得
live_urls = [i.get('href') + "?v=pc" for i in soup3.find_all('a')]
#５回"for文"を回してリンク付きテキストを表示させる
for i, j in zip(live_list[:5], live_urls[11:16]):
    st.link_button(i, j)
colulu4 = st.columns(3)
with colulu4[2]:
    st.markdown(f'[<span style="color:{orange_color};">実況をもっと見る</span>]({"https://itest.5ch.net/topics/live"})', unsafe_allow_html=True)

#閲覧履歴
st.markdown(f'[<span style="color:{orange_color};">閲覧履歴</span>]({views_history_url})', unsafe_allow_html=True)
st.markdown(f'[<span style="color:{orange_color};">本日の書込数ランキング</span>]({views_history_url})', unsafe_allow_html=True)

#板一覧
st.markdown(f'[<span style="color:{orange_color};">板一覧</span>]({threads_url})', unsafe_allow_html=True)