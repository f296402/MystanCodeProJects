"""
File: my_drawing.py
Name:Hsu chunlin
----------------------
此程式將創造一個長度為700,寬度為600的window。
並且利用非常多的GOval, GRect,GPolygon,GLine來組合出TOTORO(龍貓)在海邊黃昏的場景。
"""


from campy.graphics.gobjects import GOval, GRect,GLabel,GPolygon,GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause


def main():
    """
    此程式畫出龍貓到海邊玩到黃昏的樣子~
    首先先將圖畫分為許多部分，包括背景、海、太陽、雲、以及主角TOTORO。
    其中比較特別的地方是背景以及海的部分，有使用顏色的漸層來凸顯黃昏以及海浪的感覺。
    """
    window = GWindow(700, 600, title='TOTORO')
    background(window)
    sea(window)
    sun(window)
    cloud1(window)
    cloud2(window)
    cloud3(window)
    totoro(window)
    word(window)


def word(window):
    label= GLabel('Design by Angel',x=560,y=590)
    label.font='-15'
    label.color = True
    window.add(label)


def totoro(window):
    """
    此程式會畫出主角TOTORO的部分(好像不小心畫得太胖了XD)
    :param window:畫布的大小(700*600)
    """
    belly_2 = GOval(550, 450, x=75, y=350)
    belly_2.filled = True
    belly_2.fill_color = (142, 119, 127)
    window.add(belly_2)
    belly_3 = GOval(350, 300, x=170, y=260)
    belly_3.filled = True
    belly_3.fill_color = (142, 119, 127)
    window.add(belly_3)
    belly = GOval(400, 300, x=150, y=470)
    belly.filled = True
    belly.fill_color =(230,214,189)
    window.add(belly)
    eye_r = GOval(50, 35)
    eye_r.filled = True
    eye_r.fill_color = 'white'
    window.add(eye_r, 400, 320)
    eye2_r = GOval(15, 15)
    eye2_r.filled = True
    window.add(eye2_r, 414, 330)
    eye_l = GOval(50, 35)
    eye_l.filled = True
    eye_l.fill_color = 'white'
    window.add(eye_l, 250, 320)
    eye2_l = GOval(15, 15)
    eye2_l.filled = True
    window.add(eye2_l, 270, 330)
    ear_l = GPolygon()
    ear_l.add_vertex((270, 180))
    ear_l.add_vertex((245, 230))
    ear_l.add_vertex((260, 280))
    ear_l.add_vertex((280, 280))
    ear_l.add_vertex((295, 230))
    window.add(ear_l)
    ear_l.filled = True
    ear_l.fill_color = (142, 119, 127)
    ear_r = GPolygon()
    ear_r.add_vertex((410, 180))
    ear_r.add_vertex((385, 230))
    ear_r.add_vertex((400, 280))
    ear_r.add_vertex((420, 280))
    ear_r.add_vertex((435, 230))
    window.add(ear_r)
    ear_r.filled = True
    ear_r.fill_color = (142, 119, 127)
    line = GLine(110, 420, 190, 400)
    window.add(line)
    line_2 = GLine(105, 390, 190, 380)
    window.add(line_2)
    line_3 = GLine(110, 350, 190, 360)
    window.add(line_3)
    line_4 = GLine(500, 395, 580, 410)
    window.add(line_4)
    line_5 = GLine(495, 375, 575, 375)
    window.add(line_5)
    line_6 = GLine(485, 360, 570, 350)
    window.add(line_6)
    mouse = GOval(160,90)
    mouse.filled=True
    mouse.fill_color='white'
    window.add(mouse,270,360)
    rect =GRect(160,40)
    rect.filled= True
    rect.color=(142, 119, 127)
    rect.fill_color=(142, 119, 127)
    window.add(rect,270,360)
    nose = GPolygon()
    nose.add_vertex((335, 350))
    nose.add_vertex((365, 350))
    nose.add_vertex((350, 370))
    window.add(nose)
    nose.filled = True
    line7=GLine(270,400,430,400)
    window.add(line7)
    line8=GLine(300,400,300,440)
    window.add(line8)
    line9=GLine(330,400,330,450)
    window.add(line9)
    line10=GLine(360,400,360,450)
    window.add(line10)
    line10=GLine(390,400,390,445)
    window.add(line10)
    line11=GLine(420,400,420,425)
    window.add(line11)
    stripe=GPolygon()
    stripe.add_vertex((250,510))
    stripe.add_vertex((230, 550))
    stripe.add_vertex((250, 530))
    stripe.add_vertex((270, 550))
    window.add(stripe)
    stripe.filled=True
    stripe.fill_color='gray'
    stripe2=GPolygon()
    stripe2.add_vertex((320,500))
    stripe2.add_vertex((300,540))
    stripe2.add_vertex((320,520))
    stripe2.add_vertex((340,540))
    window.add(stripe2)
    stripe2.filled=True
    stripe2.fill_color='gray'
    stripe3=GPolygon()  # 多邊形
    stripe3.add_vertex((390,500))
    stripe3.add_vertex((370, 540))
    stripe3.add_vertex((390, 520))
    stripe3.add_vertex((410, 540))
    window.add(stripe3)
    stripe3.filled=True
    stripe3.fill_color='gray'
    stripe4=GPolygon()  # 多邊形
    stripe4.add_vertex((460,510))
    stripe4.add_vertex((440, 545))
    stripe4.add_vertex((460, 525))
    stripe4.add_vertex((480, 545))
    window.add(stripe4)
    stripe4.filled=True
    stripe4.fill_color='gray'
    stripe5=GPolygon()  # 多邊形
    stripe5.add_vertex((200,570))
    stripe5.add_vertex((190, 590))
    stripe5.add_vertex((200, 580))
    stripe5.add_vertex((210, 590))
    window.add(stripe5)
    stripe5.filled=True
    stripe5.fill_color='gray'
    stripe6=GPolygon()
    stripe6.add_vertex((280,560))
    stripe6.add_vertex((265, 590))
    stripe6.add_vertex((280, 575))
    stripe6.add_vertex((295, 590))
    window.add(stripe6)
    stripe6.filled=True
    stripe6.fill_color='gray'
    stripe7=GPolygon()
    stripe7.add_vertex((350,560))
    stripe7.add_vertex((330, 590))
    stripe7.add_vertex((350, 575))
    stripe7.add_vertex((370, 590))
    window.add(stripe7)
    stripe7.filled=True
    stripe7.fill_color='gray'
    stripe8=GPolygon()
    stripe8.add_vertex((430,560))
    stripe8.add_vertex((415,590))
    stripe8.add_vertex((430,575))
    stripe8.add_vertex((445,590))
    window.add(stripe8)
    stripe8.filled=True
    stripe8.fill_color='gray'
    stripe9=GPolygon()
    stripe9.add_vertex((510,570))
    stripe9.add_vertex((500, 590))
    stripe9.add_vertex((510, 580))
    stripe9.add_vertex((520, 590))
    window.add(stripe9)
    stripe9.filled=True
    stripe9.fill_color='gray'


def sun(window):
    """
    此程式會畫出天空中太陽的部分
    :param window:畫布的大小(700*600)
    """
    sun=GOval(70,70)
    sun.color=(255,150,31)
    sun.filled=True
    sun.fill_color=(255,233,31)
    window.add(sun,475,170)


def background(window):
    """
    此程式畫出黃昏時橘黃色的漸層背景
    :param window: 畫布的大小(700*600)
    """
    for i in range(50):
        rect=GRect(window.width,8)
        rect.color=(225,175+i,10)
        rect.filled =True
        rect.fill_color=(225,170+i,10)
        window.add(rect,0,i*8)


def sea(window):
    """
    此程式會畫出漸層色的海(背景)
    :param window: 畫布的大小(700*600)
    """
    for i in range(50):
        rect =GRect(window.width,4)
        rect.color=(180,250,250-i)
        rect.filled=True
        rect.fill_color=(120,250,250-i)
        window.add(rect,0,400+i*4)


def cloud1(window):
    """
    此程式會畫出雲的部分
    :param window: 畫布的大小(700*600)
    """
    c1 = GOval(50,50)
    c1.color = (255, 255, 255)
    c1.filled = True
    c1.fill_color = (255,255,255)
    window.add(c1,60,55)
    c2 = GOval(70,70)
    c2.color = (255, 255, 255)
    c2.filled = True
    c2.fill_color = (255,255,255)
    window.add(c2,c1.x+c1.width/2+5,c1.height-10)
    c3 = GOval(50,50)
    c3.color = (255, 255, 255)
    c3.filled = True
    c3.fill_color = (255,255,255)
    window.add(c3,c2.x+c2.width/2+15,c1.height)


def cloud2(window):
    """
    此程式會畫出雲的部分
    :param window: 畫布的大小(700*600)
    """
    c1 = GOval(50,50)
    c1.color = (255, 255, 255)
    c1.filled = True
    c1.fill_color = (255,255,255)
    window.add(c1,50,255)
    c2 = GOval(60,60)
    c2.color = (255, 255, 255)
    c2.filled = True
    c2.fill_color = (255,255,255)
    window.add(c2,80,245)
    c3 = GOval(45,50)
    c3.color = (255, 255, 255)
    c3.filled = True
    c3.fill_color = (255,255,255)
    window.add(c3,120,250)


def cloud3(window):
    """
    此程式會畫出雲的部分
    :param window: 畫布的大小(700*600)
    """
    c1 = GOval(50,50)
    c1.color = (255, 255, 255)
    c1.filled = True
    c1.fill_color = (255,255,255)
    window.add(c1,530,300)
    c2 = GOval(60,60)
    c2.color = (255, 255, 255)
    c2.filled = True
    c2.fill_color = (255,255,255)
    window.add(c2,557,295)
    c3 = GOval(50,50)
    c3.color = (255, 255, 255)
    c3.filled = True
    c3.fill_color = (255,255,255)
    window.add(c3,595,300)


if __name__ == '__main__':
    main()
