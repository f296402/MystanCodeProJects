"""
File: draw_line.py
Name:Hsu chunlin
-------------------------
此程式可以讓使用者在GWindow畫布上,第一次點選滑鼠時畫上一個空心小圓點,並且在使用者第二次點及滑鼠時,畫出一條直線；
直線的起點為小圓點中心位置，終點為第二次點擊滑鼠的位置,畫上直線以後,原點會消失在畫布上。
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

#常數
SIZE = 10
#全域變數
window = GWindow()
start_x=0
start_y=0
first_mouse_clicked = True  # 目前是第一次點滑鼠


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(creat_hole)


def creat_hole(mouse):
    """
    每次點擊滑鼠以後就會進入一次此程式,首先程式會先創造一個空心圓在第一次滑鼠點擊的位置,
    連接第二次滑鼠點擊的位置,畫出一條直線,同時將圓圈消除。
    :param mouse:啟動滑鼠功能
    """
    global first_mouse_clicked,start_y,start_x  # 全域變數要加globel
    hole = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)  # 創造空心小圓點在滑鼠位置
    if  first_mouse_clicked:  # 如果是第一次點滑鼠,就畫空心小圓圈
        hole.filled=False
        hole.color="black"
        window.add(hole)
        start_x = mouse.x  # 更新全域變數
        start_y = mouse.y  # 更新全域變數
        first_mouse_clicked = False  # 第一次點擊結束(所以已經不是第一次點擊)
    else:  # 不是第一次點滑鼠,就畫直線然後消掉圓圈
        hole=window.get_object_at(start_x,start_y)  # 取得start_x,start_y的位置
        if hole is not None :  # 檢查start_x,start_y位置是不是有物件(小圓圈)
            window.remove(hole)  #有就移除小圓圈
        line=GLine(start_x,start_y,mouse.x,mouse.y)  # 畫直線(起點X,Y,終點X,Y)
        window.add(line)
        first_mouse_clicked = True  # 第二次點擊結束(所以已經不是第二次點擊)


if __name__ == "__main__":
    main()
