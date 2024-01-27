import pyxel
import random

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.radius = 4
        self.color = 9
        self.speed = 2

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_S):
            self.y += self.speed
        if pyxel.btn(pyxel.KEY_A):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)

class Enemy:
    def __init__(self):
        self.x = random.randint(10, 240)
        self.y = random.randint(10, 240)
        self.radius = 4
        self.color = 8
        self.speed = random.randint(1, 3)
        self.angle = random.uniform(0, 2 * 3.14)

    def update(self):
        self.x += self.speed * pyxel.cos(self.angle)
        self.y += self.speed * pyxel.sin(self.angle)

        # Периодически изменяем направление движения
        if random.randint(0, 100) < 2:
            self.angle = random.uniform(0, 2 * 3.14)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)

class App:
    def __init__(self):
        pyxel.init(256, 256)
        self.player = Player()
        self.enemies = []
        self.bullets = []

        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.shoot()

        # Добавляем нового врага случайным образом
        if random.randint(0, 100) < 3:
            self.enemies.append(Enemy())

        for enemy in self.enemies:
            enemy.update()

        for bullet in self.bullets:
            bullet.update()

        # Удаляем врагов, которые вышли за пределы экрана
        self.enemies = [enemy for enemy in self.enemies if enemy.x > 0 and enemy.x < pyxel.width and
                        enemy.y > 0 and enemy.y < pyxel.height]

        # Удаляем пули, которые вышли за пределы экрана
        self.bullets = [bullet for bullet in self.bullets if bullet.x > 0 and bullet.x < pyxel.width and
                        bullet.y > 0 and bullet.y < pyxel.height]

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

        for enemy in self.enemies:
            enemy.draw()

        for bullet in self.bullets:
            bullet.draw()

    def shoot(self):
        angle = pyxel.atan2(pyxel.mouse_y - self.player.y, pyxel.mouse_x - self.player.x)
        self.bullets.append(Bullet(self.player.x, self.player.y, angle))

App()

