import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image

# 変数"url"にリンク先アドレス入れる。"r(response)"という変数で欲しい情報元にアクセスする
# url = "https://itest.5ch.net/topics/news"
# r = requests.get(url)
# 情報元のurlを取得。ステイタスコード確認(200=成功,400-499=失敗,500番台=サーバー側に問題あり)　情報元の"html"取得
# requests取得したhtmlが「文字列」か確認。"BeautifulSoup"は「文字列のhtml」である必要がある
# ("r.url", "r.status_code", "r.text", "type(r.text)") 
# soup = BeautifulSoup(r.text, features="html.parser")

#print(soup.find('h2').text) #"h2"タグのtextを読み取る ※いくつか方法がある "get"はErrorが返ってくる場合がある為非推奨
#print(soup.find_all('h2')[1].text) #２個目の"h2"タグ
#print(soup.h3.text) #"h3"タグ
#print(soup.h2.get_text()) #非推奨　※辞書を扱う際挙動が変わる事がある為

# print(soup.find_all(['h2','h3'])) #複数取得したい場合はリスト形式を使う
# header_2_and_3 = [i.text for i in soup.find_all(['h2','h3'])] #リスト内包表記を使って取得タグ内の'text'を取得
# print(header_2_and_3)

#"h2"タグ全検索
# test_list = []
# for i,j in enumerate(soup.find_all('h2')):
#     test_list.append(j.text)

#リスト内包表記の場合
# test_list = [j.text for j in soup.find_all('h2')]
# print(test_list)

# print(len(soup.find_all('span'))) #"span"タグの数
# print(soup.find_all('span', class_='say-no-more')) #"span"タグ全検索-->>特定の"class_"のみ取得
# print(soup.find_all('span', {'class':'say-no-more'})) #pythonの辞書で"class"を扱う事もできる
# print(soup.find_all('span', class_=['say-no-more', 'message'])) #複数の"class"を取得する場合はリストで書く

#限定した抽出は２種類（範囲を限定(推奨)/不要部削除(非推奨)）
# print(soup.find('div',class_='row').find_all('h2')) #範囲を限定して取得
# soup.find('div', class_="psf-widget").find('h2').extract() #不要部削除"extract()"-->>※破壊的なので非推奨




# st.set_page_config(layout="wide") # ページを広く使う

# #beautifurusoup以外でスクレイピング
# import lxml.html

# root = lxml.html.fromstring(r.text)
# body = root.body
# # 記事内の見出しのみを取得
# elems = body.xpath('//div[@class="news_link"]//a')
# for elem in elems:
#     print(elem.text)
    
        
        
        
# with st.form(key='profile_form'):
#     st.text('会員登録画面')
#     user_name = st.text_input('ユーザーネーム')
#     email = st.text_input('メールアドレス')
#     password = st.text_input('パスワード')    
#     submit_btn = st.form_submit_button('送信')
#     cancel_btn = st.form_submit_button('キャンセル')
#     if submit_btn:
#         st.text('登録完了しました。')