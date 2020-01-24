
import requests
from  bs4 import BeautifulSoup as soup
import  pandas as pd

def html_parser(a, get_url):
    url = get_url
    req = requests.get(url)
    _page_soup = soup(req.content, 'html5lib')
   # print(soup.prettify(_page_soup))
    if a == 0:
        item_list = _page_soup.findAll('h2', attrs={'class': 'fsdDeptTitle'})  #('div', attrs={'class': 'fsdDeptBox'}) main page 32 main-item( 1-time to get the name)
    elif a == 1:
        item_list = _page_soup.findAll('div', attrs={'class': 'fsdDeptCol'})    # main page 32 main-item (1-time to get 32-url)
    else:
        item_list = _page_soup.findAll('ul', attrs={'aria-labelledby': 'n-title'})   # sub-item iteration (get all category 1-by-1)
    print(len(item_list))
    if len(item_list) > 0:
        all_item_list = item_list
    else:
        all_item_list = []
    return all_item_list

def write_csv( i, url, cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10,
                cat11, cat12, cat13, cat14, cat15, cat16, cat17, cat18, cat19, cat20, cat21):
    select = True
    if i == 0 :
        global  dfObj
        global file_name
        file_name = 'amazon_store_list.csv'
        dfObj = pd.DataFrame( columns=['select', 'amazon_url', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9', 'cat10', 'cat11',
                                      'cat12', 'cat13', 'cat14', 'cat15', 'cat16', 'cat17', 'cat18', 'cat19', 'cat20', 'cat21'])
        dfObj.to_csv(file_name)
    dfObj = dfObj.append(
        {'select': select, 'amazon_url': url, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'cat4': cat4, 'cat5': cat5, 'cat6': cat6, 'cat7': cat7, 'cat8': cat8, 'cat9': cat9, 'cat10': cat10,'cat11': cat11,
         'cat12': cat12, 'cat13': cat13, 'cat14': cat14, 'cat15': cat15, 'cat16': cat16, 'cat17': cat17, 'cat18': cat18, 'cat19': cat19, 'cat20': cat20, 'cat21': cat21}, ignore_index=True)
    dfObj.to_csv(file_name)

def main():
    i  = 0
    cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10, cat_11, cat_12, cat_13, cat_14 = '', '', '', '', '', '', '', '', '', '', '', '', '', ''
    cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21 = '', '', '', '', '', '', ''

    amazon_url = 'https://www.amazon.com/gp/site-directory?ref_=nav_em_T1_0_2_2_35__fullstore'

    main_cat_01_list = html_parser(i, amazon_url)
    for index1, item1 in enumerate(main_cat_01_list):
        try:
            cat_01 = item1.text.strip()
            write_csv(i, amazon_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                      cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

            i += 1
            cat_02_list = html_parser(i, amazon_url)
            cat_02_list = cat_02_list[i:]
            for index2, item2 in enumerate(cat_02_list):
                try:
                    cat_02_url = item2.find('a').attrs=['href']     #item_list[00].find('a').attrs['href']
                    cat_02 = item2.text.strip()
                    write_csv( i, cat_02_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                              cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                    i += 1
                    cat_03_list = html_parser(i, cat_02_url)
                    cat_03_list = cat_03_list[i:]
                    for index3, item3 in enumerate(cat_03_list):
                        try:
                            cat_03_url = item3.find('a').attrs = ['href']
                            cat_03 = item3.text.strip()
                            write_csv(i, cat_03_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09,
                                      cat_10, cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                   # i += 1
                            cat_04_list = html_parser(i, cat_03_url)
                            cat_04_list = cat_04_list[i:]
                            for index4, item4 in enumerate(cat_04_list):
                                try:
                                    cat_04_url = item4.find('a').attrs = ['href']
                                    cat_04 = item4.text.strip()
                                    write_csv(i, cat_04_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                                               cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                    i += 1
                                    cat_05_list = html_parser(i, cat_04_url)
                                    cat_05_list = cat_05_list[i:]
                                    for index5, item5 in enumerate(cat_05_list):
                                        try:
                                            cat_05_url = item5.find('a').attrs = ['href']
                                            cat_05 = item5.text.strip()
                                            write_csv(i, cat_05_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                                                      cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                            i += 1
                                            cat_06_list = html_parser(i, cat_05_url)
                                            cat_06_list = cat_06_list[i:]
                                            for index6, item6 in enumerate(cat_06_list):
                                                try:
                                                    cat_06_url = item6.find('a').attrs = ['href']
                                                    cat_06 = item6.text.strip()
                                                    write_csv(i, cat_06_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                                                              cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                                    i += 1
                                                    cat_07_list = html_parser(i, cat_06_url)
                                                    cat_07_list = cat_07_list[i:]
                                                    for index7, item7 in enumerate(cat_07_list):
                                                        try:
                                                            cat_07_url = item7.find('a').attrs = ['href']
                                                            cat_07 = item7.text.strip()
                                                            write_csv(i, cat_07_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                                                                      cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                                            i += 1
                                                            cat_08_list = html_parser(i, cat_07_url)
                                                            cat_08_list = cat_08_list[i:]
                                                            for index8, item8 in enumerate(cat_08_list):
                                                                try:
                                                                    cat_08_url = item8.find('a').attrs = ['href']
                                                                    cat_08 = item7.text.strip()
                                                                    write_csv(i, cat_08_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                                                                              cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                                                    i += 1
                                                                    cat_09_list = html_parser(i, cat_08_url)
                                                                    cat_09_list = cat_09_list[i:]
                                                                    for index9, item9 in enumerate(cat_09_list):
                                                                        try:
                                                                            cat_09_url = item9.find('a').attrs=['href']
                                                                            cat_09 = item9.text.strip()
                                                                            write_csv(i, cat_09_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                                                                                      cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                                                            i += 1
                                                                            cat_10_list = html_parser(i, cat_09_url)
                                                                            cat_10_list = cat_10_list[i:]
                                                                            for index10, item10 in enumerate(cat_10_list):
                                                                                try:
                                                                                    cat_10_url = item10.find('a').attrs = ['href']
                                                                                    cat_10 = item10.text.strip()
                                                                                    write_csv(i, cat_10_url, cat_01, cat_02, cat_03, cat_04, cat_05, cat_06, cat_07, cat_08, cat_09, cat_10,
                                                                                              cat_11, cat_12, cat_13, cat_14, cat_15, cat_16, cat_17, cat_18, cat_19, cat_20, cat_21)

                                                                                except Exception:
                                                                                    break
                                                                        except Exception:
                                                                            break
                                                                except Exception:
                                                                    break
                                                        except Exception :
                                                             break
                                                except Exception:
                                                    break
                                        except Exception:
                                            break
                                except Exception:
                                    break
                        except Exception:
                            break
                except Exception:
                    break
        except Exception:
                break

if __name__ == '__main__':
    main()
