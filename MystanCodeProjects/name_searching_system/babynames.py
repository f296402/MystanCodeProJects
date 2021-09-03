"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name in name_data:
        if year in name_data[name]:  # 名字/年分一樣 要更新排名
            if int(name_data[name][year]) > int(rank):
                name_data[name][year] = rank
        else:  # 名字一樣但要增新年分與排名
            name_data[name][year] = rank
    else:  # 增新全不同的名字/年分/排名
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        for line in f:
            word_list = line.split(',')  # split是把每一行,分割成許多個word的list
            print(word_list)
            # if len(word_list) == 1:  # 只有年份
            #     year = word_list[0]
            #     year = year.strip()
            # else:
            #     rank = word_list[0]  # 位置0是排名
            #     rank = rank.strip()
            #     name_man = word_list[1]  # 位置1是男生名字
            #     name_man = name_man.strip()
            #     name_female = word_list[2]  # 位置2是女生名字
            #     name_female = name_female.strip()
            #     add_data_for_name(name_data, year, rank, name_man)  # 加到字典裡
            #     add_data_for_name(name_data, year, rank, name_female)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    names = []  # 存target搜尋到的名字
    # target = input('search name:'
    target = str(target.lower())
    for name in name_data:  # 跑list裡面的每一個name
        if len(name) >= len(target):
            name2 = str(name.lower())
            for i in range(len(name2)-len(target)+1):  # 比較名字每段有沒有一樣
                compare_name = name2[:len(target)]
                if compare_name == target:
                    names.append(name)
                    break   # 如果有一樣的就跳出迴圈
                name2 = name2[1:]
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
