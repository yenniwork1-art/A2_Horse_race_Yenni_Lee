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
    def __init__(self, speed, y, image, window):
        self.x_pos = 0
        self.y_pos = y
        self.window = window
        self.image = image
        self.dice = Dice(speed)

    def draw(self):
        try:
            self.image.draw(self.window)
        except:
            pass

    def move(self):
        steps = self.dice.roll()
        self.x_pos += steps
        self.image.move(steps, 0)


    def crossed_finish_line(self, finish_x):
        return self.x_pos >= finish_x

    def change_lane(self, new_y):
        self.y_pos = new_y

def draw_finish_line(win, finish_x):
    line = Line(Point(finish_x, 0), Point(finish_x, Win_v))
    line.setWidth(3)
    line.draw(win)

#make a structure for main code
def main():
    win = GraphWin("Horse race", Win_h, Win_v)
    win.setBackground("lightyellow")

    img1 = Image(Point(start_point, horse_1), "Cat_Meow.gif")
    img2 = Image(Point(start_point, horse_2), "hamster.gif")
    horse1 = Horse(speed=8, y=horse_1, image=img1, window=win)
    horse2 = Horse(speed=8, y=horse_2, image=img2, window=win)

    title = Text(Point(Win_h // 2, 30), "Are you ready to race?!")
    title.setSize(14)
    title.draw(win)

    draw_finish_line(win, finish_point)
    horse1.draw()
    horse2.draw()
    win.getMouse()

    while True:
        horse1.move()
        horse2.move()

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

        update(10)

    exit_text = Text(Point(Win_h // 2, Win_v - 20), "Click on the horse to exit")
    exit_text.setSize(12)
    exit_text.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()