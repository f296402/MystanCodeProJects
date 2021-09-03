"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

提供打磚塊遊戲所會用到的各種物件以及method,包含class BreakoutGraphics。
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10     # Number of rows of bricks.
BRICK_COLS = 10   # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    """BreakoutGraphics 是遊戲中一些物件的創造與設定
    例如:我在利用class GRect 創造一個paddle的物件,並且加到class BreakoutGraphics的window世界中

    以下class 是GRect的使用方式:
        window = GWindow()
        rect = GRect(200, 100)
        rect.filled = True
        rect.color = "RED"
        window.add(rect, 0, 0)
    """
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        """
        創造打磚塊遊戲的物件以及遊戲條件設定
        :param ball_radius:球的半徑長度
        :param paddle_width:板子的寬度
        :param paddle_height:板子的高度
        :param paddle_offset:為板子與視窗底部之距離
        :param brick_rows:為總共有幾列磚塊
        :param brick_cols:為總共有幾行磚塊
        :param brick_width:磚塊的寬度
        :param brick_height:磚塊的高度
        :param brick_offset:為第一列磚塊頂部與視窗頂端之距離
        :param brick_spacing: 為磚塊與磚塊之間（左右、上下）的小空隙
        :param title:遊戲名稱
        """
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle,(self.window.width-self.paddle.width)/2
                        , self.window.height-self.paddle.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, self.window.width/2-ball_radius, self.window.height/2-ball_radius)
        self.start = False
        # Default initial velocity for the ball
        self.random_dx = 0
        self.dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.game_start)
        # Draw bricks
        for i in range(brick_rows): # 列
            for j in range(brick_cols): # 行
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = (85,180,255-i*12)
                self.window.add(brick, 0+(i*brick_width)+(i*brick_spacing)
                                , brick_offset+(j*brick_height)+(j*brick_spacing))
        self.total_bricks_number = brick_cols*brick_rows
        self.current_bricks_number = 0
        self.score = 0
        self.score_label= GLabel('Score: '+str(self.score)+' /'+str(self.total_bricks_number))
        self.score_label.color = (0,125,115)
        self.score_label.font = 'Dialog-15-italic'
        self.window.add(self.score_label, 0, self.score_label.height + 5)
        self.life = 3
        self.life_label= GLabel('❤ ' * self.life)
        self.life_label.color ='black'
        self.life_label.font = '-20'
        self.window.add(self.life_label, self.window.width-self.life_label.width, self.life_label.height + 10)

    def paddle_move(self,mouse):
        """讓paddle可以跟跟著滑鼠中心左右移動"""
        if self.paddle.width/2 < mouse.x < self.window.width-self.paddle.width/2:
            self.window.add(self.paddle,mouse.x-(self.paddle.width/2),self.paddle.y)

    def game_start(self,event):
        """遊戲開始開關打開(滑鼠不能點按),創造隨機球速讓球移動"""
        if  not self.start:
            self.start = True
            self.random_dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.random_dx = -self.random_dx
            self.dy = INITIAL_Y_SPEED

    def lose_life(self):
        """每次球超出視窗就少一個'❤' """
        self.life -= 1
        self.life_label.text = '❤' * self.life


    def hit_window_right_or_left(self):
        """ 球打到視窗左右邊,反彈速度變號"""
        self.random_dx = -self.random_dx

    def dy_bounce(self):
        """ 球打到視窗頂端,反彈速度變號"""
        self.dy = -self.dy

    def check_object(self):
        """檢查球邊上四個點是否有偵測到物件,有偵測到物件,球速要反彈並移除物件,如果物件是paddle則不移除。"""
        for i in range(2): # 找鄰居的演算法
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x + i*self.ball.width
                                                , self.ball.y + j*self.ball.height)
                if obj is not None and obj is not self.score_label \
                        and obj is not self.life_label : # 有偵測到物件
                    self.dy_bounce()
                    if obj is not self.paddle:  # 如果物件不是paddle
                        self.window.remove(obj)
                        self.current_bricks_number += 1
                        self.score += 1
                        self.score_label.text = 'Score:' + str(self.score)+' /'+str(self.total_bricks_number)
                        return
                    else:
                        self.ball.y = self.paddle.y - self.ball.height  # 防止球黏在板子上
                        return

    def get_random_x(self):
        """
        得到x的球速
        :return: int,x的球速
        """
        return self.random_dx

    def get_random_y(self):
        """
        得到y的球速
        :return: int,y的球速
        """
        return self.dy

    def ball_move(self):
        """
        讓球以得到x的球速得到y的球速移動
        :return:method,讓球移動的程式
        """
        dx = self.get_random_x()
        dy = self.get_random_y()
        return self.ball.move(dx, dy)

    def reset_speed(self):
        """球速歸零"""
        self.random_dx = 0
        self.dy = 0

    def reset_ball_position(self):
        """
        讓球回到起始位置
        """
        self.window.add(self.ball, self.window.width / 2 - self.ball.width / 2,
                        self.window.height / 2 - self.ball.height / 2)

    def win(self):
        """當磚塊都被打完時,球速變成0,並印出文字
        :return:布林值,True
        """
        if self.current_bricks_number == self.total_bricks_number:
            self.random_dx = 0
            self.dy = 0
            label = GLabel('You win!!!')
            label.color = (255,170,14)
            label.font = 'Verdana-50-italic'
            self.window.add(label, self.window.width/2-label.width/2, self.window.height/2)
            return True

    def lose(self):
        """
         當遊戲次數為0,球速變成0,並印出文字
        :return:布林值,True
        """
        self.random_dx = 0
        self.dy = 0
        label = GLabel('GAME OVER! :(')
        label.color = (255,49,15)
        label.font = 'Dialog-35-italic'
        self.window.add(label, self.window.width / 2 - label.width / 2, self.window.height / 2)
        return True
