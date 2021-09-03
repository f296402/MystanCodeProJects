"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    distance_of_each_line = (width-GRAPH_MARGIN_SIZE)//len(YEARS)
    x_coordinate = year_index * distance_of_each_line  # 用每段平均長度乘上year的index
    return int(x_coordinate)+GRAPH_MARGIN_SIZE  # 加上左邊扣掉的GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                       , CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)  # 劃上界線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,  # 劃下界線
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                           0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)  # 畫背景直線（間隔線）
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)  # 畫每個年份的位置
    #################################


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    # Write your code below this line
    for i in range(len(lookup_names)):  # 跑lookup_names裡的所有名字
        if lookup_names[i] in name_data:  # 檢查名字有沒有在字典裡
            rank_lst = []  # 設一個空list等等裝name
            for j in range(len(YEARS)):
                if str(YEARS[j]) in name_data[lookup_names[i]]:  # 檢查年份有沒有在字典裡
                    rank = name_data[lookup_names[i]][str(YEARS[j])]  # 得到lookup_names[i]YEARS[j]的排名
                    rank_lst.append(rank)
                else:
                    rank_lst.append('**')  # 沒有排名資料就用＊
            # 1900第一筆資料
            x1 = get_x_coordinate(CANVAS_WIDTH, 0) + TEXT_DX
            if rank_lst[0] == '**':
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                # 沒排名的y座標
            else:
                y1 = int(rank_lst[0]) * (CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE * 2)) / 1000 + GRAPH_MARGIN_SIZE
                # 有排名的y座標
            canvas.create_text(x1, y1, text=lookup_names[i] + rank_lst[0], anchor=tkinter.NW, fill=COLORS[i % 4])
            # From 1910
            for j in range(len(YEARS) - 1):  # 第二筆資料開始（所以次數減1)
                x2 = get_x_coordinate(CANVAS_WIDTH, j + 1) + TEXT_DX
                if rank_lst[j + 1] == '**':
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # 沒排名的y座標
                else:
                    y2 = int(rank_lst[j + 1]) * (CANVAS_HEIGHT - (GRAPH_MARGIN_SIZE * 2)) / 1000 + GRAPH_MARGIN_SIZE
                    # 有排名的y座標
                canvas.create_text(x2, y2, text=lookup_names[i] + rank_lst[j + 1], anchor=tkinter.NW,
                                   fill=COLORS[i % 4])
                canvas.create_line(x1, y1, x2, y2, width=TEXT_DX, fill=COLORS[i % 4])
                x1 = x2  # 終點更新為起點
                y1 = y2  # 終點更新為起點
    #################################


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
