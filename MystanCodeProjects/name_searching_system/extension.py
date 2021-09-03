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
        total_males = []
        total_female = []
        for item in items:
            tbody_text = item.tbody.text
        print(tbody_text)
            # tbody_list = tbody_text.split()
        # print(tbody_list)
        # for i in range(200):
        #     total_males.append(int(tbody_list[2].replace(',', '')))
        #     total_female.append(int(tbody_list[4].replace(',', '')))
        #     # item = string_manipulating(total_males[i])
        #     tbody_list = tbody_list[5:]
        # print('total_male:' + str(sum(total_males)))
        # print('total_female:'+str(sum(total_female)))


# def string_manipulating(word):
#     ans = ''
#     for ch in word:
#         if ch.isdigit():
#             ans += ch
#     return ans




if __name__ == '__main__':
    main()
