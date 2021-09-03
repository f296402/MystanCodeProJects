"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

此程式創造一個名為breakout打磚塊的遊戲,點擊滑鼠後遊戲開始,球開始上下左右隨機移動,
玩家必須用滑鼠控制paddle,讓球反彈,玩家有三次的機會,最後打完所有磚塊就獲勝,反之玩家遊戲結束。
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    此程式創造一個名為breakout打磚塊的遊戲,遊戲開始前球會出現在正中間不動,底下的paddle則會依滑鼠左右移動
    ,點擊滑鼠後遊戲開始,球開始上下左右隨機移動,玩家有三次沒接到球的機會,最後打完所有磚塊就獲勝,反之玩家輸了遊戲結束。
    """
    graphics = BreakoutGraphics()  # 取得 class BreakoutGraphics裡所創造的物件
    num_lives = NUM_LIVES  # 玩家遊戲次數
    while num_lives != 0:
        pause(FRAME_RATE)
        graphics.ball_move()  # 先get球新移動的速度,再把get到的速度帶入讓球移動的method
        graphics.check_object()  # 檢查球邊上四個點是否有偵測到物件的method
        if graphics.ball.x <= 0 or graphics.ball.x > (graphics.window.width - graphics.ball.width):
            graphics.hit_window_right_or_left() # 球打到視窗左右邊反彈的method
        if  graphics.ball.y <= 0 :
            graphics.dy_bounce()  # # 球打到視窗頂端反彈的method
        elif graphics.ball.y >= graphics.window.height :  # 球超出視窗底部
            num_lives -= 1
            graphics.start = False  # 遊戲開關關起來(可以滑鼠點按)
            graphics.reset_ball_position()  # 讓球回到開始位置的method
            graphics.reset_speed()  # 讓球速度規0的method(才不會滑鼠還沒點按球就開始亂跑)
        if graphics.win():
            break
    if num_lives == 0:
        graphics.lose()

if __name__ == '__main__':
    main()
