"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        #                #
        #      TODO:     #
        #                #
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find_all('table', {'class': 't-stripe'})
        total_males = 0
        total_female = 0
        for item in items:
            tbody_text = item.tbody.text
            tbody_text_list = tbody_text.split('\n')
            print(tbody_text_list)
            for i in range(len(tbody_text_list)):
                if i % 2 == 0:
                    name_rank = tbody_text_list[i].split()
                    if len(name_rank) == 4:
                        total_males += int(name_rank[1].replace(',', ''))
                        total_female += int(name_rank[3].replace(',', ''))
            print('total_male:' + str(total_males))
            print('total_female:'+str(total_female))


def string_manipulating(word):
    ans = ''
    for ch in word:
        if ch.isdigit():
            ans += ch
    return ans




if __name__ == '__main__':
    main()
