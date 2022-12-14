from turtle import Turtle


class BulletManager:

    def __init__(self):
        self.bullets = []
        self.alien_shots = []
        self.count = 0

    def create_bullet(self, position):
        if self.count % 2 == 0:
            new_bullet = Turtle()
            new_bullet.shape("bullet.gif")
            new_bullet.penup()
            new_bullet.left(90)
            new_bullet.goto(position[0] + 2, position[1] + 70)
            self.bullets.append(new_bullet)
        self.count += 1

    def create_enemy_bullet(self, position):
        if self.count % 200 == 0:
            new_bullet = Turtle()
            new_bullet.shape("enemy_bullet.gif")
            new_bullet.penup()
            new_bullet.right(90)
            new_bullet.goto(position[0] + 2, position[1] - 70)
            self.alien_shots.append(new_bullet)
        self.count += 1

    def move(self):
        for bullet in self.bullets:
            bullet.forward(25)
        for bullet in self.alien_shots:
            bullet.forward(15)


