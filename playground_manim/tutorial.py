# ruff: noqa: F405
from manim import *  # noqa  # type: ignore


class Tutorial(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI),
            Rotate(right_square, angle=PI),
            run_time=2,
        )
        self.wait()

    def construct1(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(Rotate(square, angle=PI / 4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(PINK, opacity=0.5))


Tutorial().render()
