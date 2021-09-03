"""
File: bouncing_ball.py
Name:Hsu chunlin
-------------------------
    每次點擊滑鼠以後就會進入一次此程式,點擊以後球會開始落下並彈跳至跳出視窗為止,最後回到起始位置。
    但球在彈跳過程中,滑鼠的點擊不會影響到正在進行彈跳的球,且進行三次以後程式將終止。
    :param mouse: 啟動滑鼠功能
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


#常數
VX = 4
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
#全域變數
times = 0
vy= 0
ball_is_moving = False
window = GWindow(width=800,height=500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = True
    window.add(ball)
    onmouseclicked(creat_ball)

def creat_ball(mouse):
    """
    每次點擊滑鼠以後就會進入一次此程式,點擊以後球會開始落下並彈跳至跳出視窗為止,最後回到起始位置。
    但球在彈跳過程中,滑鼠的點擊不會影響到正在進行彈跳的球,且進行三次以後程式將終止。
    :param mouse: 啟動滑鼠功能
    """
    global vy,times,ball_is_moving  # 全域變數要加globel
    if not ball_is_moving:  # 當球沒有移動才可進入下面的程式
        ball_is_moving = True  # 打開開關(球現在正在移動)
        times = times+1  # 紀錄次數(每跑一次就加1)
        if times <= 3:  # 次數不可大於3
            while True:  # 不知道會彈跳幾次 所以用while
                vy = (vy + GRAVITY)  # 垂直速度
                ball.move(VX,vy)  # 球(水平、垂直)移動速度
                if ball.y+ball.height>=window.height:  # 當球超出視窗的底部
                    vy= -(vy*REDUCE)  # 就反彈(速度*0.9改成向上)
                    window.add(ball,x=ball.x,y=window.height-ball.height) # 指定球到視窗底部上方的位置
                if ball.x >= window.width: # 當球大於視窗的長度時
                    ball_is_moving = False  # 關掉開關(球不再移動)
                    break  # 跳出程式
                pause(DELAY)  # 放慢球速
            window.add(ball,START_X,START_Y)  # 球回到起點


if __name__ == "__main__":
    main()
