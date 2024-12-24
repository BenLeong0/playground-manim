# ruff: noqa: F405
from manim import *  # noqa  # type: ignore


class Trig(Scene):
    def construct(self):
        a, b, c = (np.array((0, 0, 0)), np.array((3, 0, 0)), np.array((0, 4, 0)))
        ab, ac, bc = [
            x.shift(DOWN).shift(LEFT) for x in [Line(a, b), Line(a, c), Line(b, c)]
        ]
        self.play(Create(ab), Create(ac), Create(bc))
        self.wait(1)

        s_ab = Square(3, color=BLUE).shift(DOWN * 2.5).shift(RIGHT * 0.5)
        self.play(DrawBorderThenFill(s_ab))
        self.wait(1)
