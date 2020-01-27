
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd


def html_parser(a, get_url):
    url = get_url
    req = requests.get(url)
    list = []
    if req.status_code == 200:
        _page_soup = soup(req.content, 'html5lib')
        if a == 0:
            item_list = _page_soup.findAll('div', attrs={'class': 'fsdDeptCol'})
            for x in item_list:
                y = x.find('a')['href']
                list.append('https://www.amazon.com'+y)
        elif a == 1:
            list = _page_soup.findAll('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-one'})[0].find('li').find('a')['href']
        elif a==2:
            list = _page_soup.findAll('li', attrs={'class': 's-ref-indent-neg-micro'})[0].find('a')           # sub-item iteration (get all category 1-by-1)
        else:
            try:
                list = _page_soup.findAll('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-one'})[0].findAll('li')
            except Exception:
                pass
            if list == []:
                list = _page_soup.findAll('ul', attrs={'class': 'a-unordered-list a-nostyle a-vertical s-ref-indent-two'})[0].findAll('li')
        print(len(list))
        print(list)
        return list

def write_csv( j, url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11, cat12, cat13, cat14, cat15):
    select = True
    if j == 0 :
        global  dfObj
        global file_name
        file_name = 'amazon_test_2.csv'
        dfObj = pd.DataFrame(columns=['select', 'amazon_url', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9', 'cat10', 'cat11',
                                      'cat12', 'cat13', 'cat14', 'cat15'])
        dfObj.to_csv(file_name)
    dfObj = dfObj.append(
        {'select': select, 'amazon_url': url, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'cat4': cat4, 'cat5': cat5, 'cat6': cat6, 'cat7': cat7, 'cat8': cat8,
         'cat9': cat9, 'cat10': cat10,'cat11': cat11, 'cat12': cat12, 'cat13': cat13, 'cat14': cat14, 'cat15': cat15}, ignore_index=True)
    dfObj.to_csv(file_name)

def main():
    i = 0
    k=0
    cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''

    amazon_url = 'https://www.amazon.com/gp/site-directory?ref_=nav_em_T1_0_2_2_35__fullstore'

    main_cat_01_list = html_parser(i, amazon_url)

    for index, item in enumerate(main_cat_01_list):
        try:
            i=1
            cat_01_url = item
            main_list = html_parser(i, cat_01_url)
            i=2
            sec_url = html_parser(i, main_list)

            main_cat_01 = sec_url.text.strip()
            main_url = sec_url['href']
            cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', '', '', '', '', '', '', ''
            write_csv(k, main_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)
            k += 1

            i = 3
            cat_02_list = html_parser(i, main_url)
            for index2, item2 in enumerate(cat_02_list):
                try:
                    cat_02_url = item2.find('a')['href']
                    cat_02 = item2.text.strip()
                    K=2
                    cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', '', '', '', '', '', '',
                    write_csv(k, cat_02_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                    cat_03_list = html_parser(i, cat_02_url)                                # **************************************
                    for index3, item3 in enumerate(cat_03_list):
                        try:
                            cat_03_url = item3.find('a')['href']
                            cat_03 = item3.text.strip()
                            K = 2
                            cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', '', '', '', '', ''
                            write_csv(k, cat_03_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                            cat_04_list = html_parser(i, cat_03_url)
                            for index4, item4 in enumerate(cat_04_list):
                                try:
                                    cat_04_url = item4.find('a')['href']
                                    cat_04 = item4.text.strip()
                                    K = 2
                                    cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', '', '', '', ''
                                    write_csv(k, cat_04_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                                    cat_05_list = html_parser(i, cat_04_url)
                                    for index5, item5 in enumerate(cat_05_list):
                                        try:
                                            cat_05_url = item5.find('a')['href']
                                            cat_05 = item5.text.strip()
                                            K = 2
                                            cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', '', '', ''
                                            write_csv(k, cat_05_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                                            cat_06_list = html_parser(i, cat_05_url)
                                            for index6, item6 in enumerate(cat_06_list):
                                                try:
                                                    cat_06_url = item6.find('a')['href']
                                                    cat_06 = item6.text.strip()
                                                    K = 2
                                                    cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', '', ''
                                                    write_csv(k, cat_06_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                                                    cat_07_list = html_parser(i, cat_06_url)
                                                    for index7, item7 in enumerate(cat_07_list):
                                                        try:
                                                            cat_07_url = item7.find('a')['href']
                                                            cat_07 = item7.text.strip()
                                                            K = 2
                                                            cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', ''
                                                            write_csv(k, cat_07_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                                                            cat_08_list = html_parser(i, cat_07_url)
                                                            for index8, item8 in enumerate(cat_08_list):
                                                                try:
                                                                    cat_08_url = item8.find('a')['href']
                                                                    cat_08 = item8.text.strip()
                                                                    K = 2
                                                                    cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', ''
                                                                    write_csv(k, cat_08_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                                                                    cat_09_list = html_parser(i, cat_08_url)
                                                                    for index9, item9 in enumerate(cat_09_list):
                                                                        try:
                                                                            cat_09_url = item9.find('a')['href']
                                                                            cat_09 = item9.text.strip()
                                                                            K = 2
                                                                            cat_10, cat_11, cat_12, cat_13, cat_14, cat_15 = '', '', '', '', '', '', '', ''
                                                                            write_csv(k, cat_09_url, main_cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14, cat_15)

                                                                        except Exception:
                                                                            pass
                                                                except Exception:
                                                                    pass
                                                        except Exception:
                                                            pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass


if __name__ == '__main__':
    main()


