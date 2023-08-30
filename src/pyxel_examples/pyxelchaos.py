import pyxel


class App:
    def __init__(self):
        pyxel.init(164, 164, title="Perlin Noise", capture_scale=2)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(10)
        for y in range(164):
            for x in range(164):
                n = pyxel.noise(
                    x / 25,
                    y / 25,
                    pyxel.frame_count / 10,
                )
                if n > 0.05:
                    col = 8
                elif n > 0:
                    col = 7
                elif n > -0.05:
                    col = 1
                else:
                    col = 0
                pyxel.pset(x, y, col)


App()
