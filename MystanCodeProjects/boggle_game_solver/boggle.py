"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
# # Global Variable
d = {}

def main():
	"""
	此程式執行Boggle的桌遊，使用者一開始會先輸入排出一個 4 x 4 的方形字母，接著此程式將找出存在於這個 4 x 4 的方
	形字母拼盤的所有英文單字。
	"""
	read_dictionary()
	start = time.time()
	####################
	all_row_lst = []  # 裝使用者輸入row1到row4
	for i in range(4):
		row = input(f'{i+1} row of letters:')
		row = row.lower()
		row = row.split()
		all_row_lst.append(row)
	ans = boggle(all_row_lst)
	####################
	end = time.time()
	print('----------------------------------')
	print('There are', len(ans), 'words in total.')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(all_row_lst):
	"""
	:param all_row_lst: list,包含使用者輸入row1,到row4的list
	:return answer_list:list,裝所有湊出可與字典相符的英文單字
	"""
	answer_list = []
	for x in range(len(all_row_lst)):  # for loop讓16個字母輪流坐在單字第一個位置（跑所有字母x座標）
		for y in range(len(all_row_lst[0])):  # for loop讓16個字母輪流坐在單字第一個位置（跑所有字母y座標）
			current_word = []  # 每次回來以後會清空
			already_down_digit = []  # 每次回來以後會清空
			current_word.append(all_row_lst[x][y])  # 將座標是（x,y)的字加進current_word
			already_down_digit.append((x, y))  # 將（x,y)的座標加進already_down_digit
			boggle_helper(x, y, all_row_lst, current_word, answer_list, already_down_digit)
	return answer_list


def boggle_helper(x, y, all_row_lst, current_word, answer_list, already_down_digit):
	"""
	:param y: 目前程式跑到的Y座標
	:param x: 目前程式跑到的x座標
	:param all_row_lst: list,包含使用者輸入row1,到row4的list
	:param current_word: list,裝目前所湊出的英文字母
	:param answer_list:list,裝所有湊出可與字典相符的英文單字
	:param already_down_digit:tuple,裝已經跑過的座標,之後要用來檢查某個座標是否已經跑過了
	:return:
	"""
	for i in range(-1, 2, 1):  # 找到周圍點的演算法(i=-1/0/1)
		for j in range(-1, 2, 1):  # 找到周圍點的演算法(j=-1/0/1))
			if -1 < x + i < 4:  # 防止超出組合字的範圍（ex:如果x=0,i=-1,就沒有x=-1的字)
				if -1 < y + j < 4:  # 防止超出組合字的範圍（ex:如果y=0,i=-1,就沒有y=-1的字)
					if (x + i, y + j) not in already_down_digit:  # 檢查目前的鄰居(x + i, y + j)如果沒有在already_down_digit裡面才能跑
						already_down_digit.append((x + i, y + j))  # 將鄰居（x+i,y+j)的座標加進already_down_digit(list)
						current_word.append(all_row_lst[x + i][y + j])  # 將座標是（x+i,y+j)的英文字加進current_word(list)
						compare = ''
						for k in range(len(current_word)):  # for loop將current_word的英文字list轉成一個字串(compare)
							compare += current_word[k]
						if compare in d and compare not in answer_list:  # if key in d 語法
							print('Found', compare)
							answer_list.append(compare)
						# explore
						if has_prefix(compare):
							boggle_helper(x + i, y + j, all_row_lst, current_word, answer_list, already_down_digit)
						# un choose
						already_down_digit.pop()  # already_down_digit最後一個座標,在跑回上一層boggle_helper()時也要pop掉！
						current_word.pop()  # 跑回上一層boggle_helper()時要把current_word最後一個字pop掉。
#  x 0 1 2 3
# y0 f y c l
# y1 i o m g
# y2 o r i l
# y3 h j h u


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open('dictionary.txt', 'r') as f:
		for line in f:
			if len(line) > 4:
				word = ','.join(line.split())  # line.split()完以後是list,list轉成str要用','.join（）的語法
				d[word] = 1  # 把dictionary.txt裡的單字加到字典裡
	return d


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in d:
		ans = word.startswith(sub_s)  # 檢查開頭有沒有在字典裡
		if ans is True:
			return True  # 有return True
	return False  # 沒有return False



if __name__ == '__main__':
	main()
