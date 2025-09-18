#Assignment A2: A Horse Race created by Yenni Lee (u1545342)

from graphics import *
from Dice import Dice

#set up
Win_h, Win_v = 700, 350
start_point = 20
horse_1 = 120
horse_2 = 260
finish_point = Win_h - 80

#make a horse class
class Horse:
    def __init__(self, speed, y, window, image):
        self.x_pos = 0
        self.y_pos = y
        self.window = window
        self.image = image
        self.dice = Dice(speed)
        self.drawn = False

    def move(self):
        step = self.dice.roll()
        self.x_pos += step
        if self.drawn:
            self.image.move(step,0)
        return step

    def draw(self):
        if not self.drawn:
            self.image.draw_at_pos(self.window, self.x_pos, self.y_pos)
            self.drawn = True

    def crossed_finish_line (self,finish_point):
        return self.x_pos >= finish_point

def draw_finish_line(win, finish_x):
    line = Line(Point(finish_x, 0), Point(finish_x, Win_v))
    line.setWidth(3)
    line.draw(win)

#make a structure for main code
def main():
    win = GraphWin("Horse race", Win_h, Win_v)
    win.setBackground("lightyellow")

#input the image
    img1 = Image(Point(start_point, horse_1), "Cat_Meow.gif")
    img2 = Image(Point(start_point, horse_2), "hamster.gif")
    horse1 = Horse(speed=8, y=horse_1, image=img1, window=win)
    horse2 = Horse(speed=8, y=horse_2, image=img2, window=win)

#before start
    title = Text(Point(Win_h // 2, 30), "Are you ready to race?!")
    title.setSize(14)
    title.draw(win)
    draw_finish_line (win, finish_point)
    horse1.draw()
    horse2.draw()
    win.getMouse()

#start race
    while True:
        horse1.move()
        horse2.move()

        win.setBackground("lightyellow")
        draw_finish_line (win, finish_point)

        horse1.draw()
        horse2.draw()

        h1 = horse1.crossed_finish_line(finish_point)
        h2 = horse2.crossed_finish_line(finish_point)

        if h1 or h2:
            if h1 and h2:
                text = "Tie"
            elif h1:
                text = "Cat is winner"
            else:
                text = "Hamster is winner"

            result = Text(Point(Win_h // 2, 60), text)
            result.setSize(16)
            result.draw(win)

            break

        update(10) #adjust speed

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()