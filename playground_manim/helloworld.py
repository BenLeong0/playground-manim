# ruff: noqa: F405
from manim import *  # noqa  # type: ignore


class HelloWorld(Scene):
    def construct(self):
        c = Circle(2, color=RED, fill_opacity=0.1)
        self.play(DrawBorderThenFill(c), run_time=2)

        title = Text("Hello World", font_size=50).to_edge(UP)
        subtitle = Text("hi", font_size=25).to_edge(UP).shift(DOWN * 0.6)
        self.play(Write(title), Write(subtitle))

        a = Arc(2.2, TAU * 1 / 4, -TAU * 2.6 / 4, color=BLUE, stroke_width=15)
        self.play(Create(a))

        self.wait(3)
