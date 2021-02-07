import time
from selenium import webdriver
import chromedriver_binary

from model import Keyword, Statistics


def search(word, url, max_page=20, wait_time=3):
    search_page_url = 'https://www.google.com/'
    
    # 設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    # 検索画面を開く
    driver.get(search_page_url)
    time.sleep(wait_time)

    # 検索を実行
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(word)
    search_box.submit()
    time.sleep(wait_time)

    page = 0
    count = 0
    count_in_page = 0
    finding = False

    while page < max_page:
        page += 1
        count_in_page = 0
        
        element_group = driver.find_elements_by_xpath('//a/h3')
        for elem in element_group:
            count += 1
            count_in_page += 1
            # title = elem.text
            link = elem.find_element_by_xpath('..').get_attribute('href')
            # print(f'Page:{page:2} Count:{count:3} Title: {title} Link: {link[:30]}')
        
            if link == url:
                finding = True
                break
        
        if finding:
            break
        if driver.find_elements_by_id('pnnext') == []:
            break
        
        # print('next page')
        next_page = driver.find_element_by_id('pnnext').get_attribute('href')
        driver.get(next_page)
        time.sleep(wait_time)
    driver.quit()

    return finding, {'rank': count, 'page': page, 'rank_in_page': count_in_page}


if __name__ == '__main__':
    search_words = [
        '新巻葡萄酒',
        '山梨 ワイン 一宮',
        '山梨 ワイナリー 一宮',
        '山梨 ゴールドワイン 一宮',
    ]
    search_url = 'https://aramakiwinery.jp/'

    for search_word in search_words:
        find, data = search(search_word, search_url, max_page=20, wait_time=3)
        print(f'Search word: {search_word}')
        print(find, data)
    print('finish')

        
