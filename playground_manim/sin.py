# ruff: noqa: F405
from manim import *  # noqa  # type: ignore


class Sin(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 20, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
        )
        sin_graph = axes.plot(lambda x: np.sin(x)).set_stroke(opacity=0)
        self.add(
            TracedPath(
                lambda: sin_graph.get_end(),
                dissipating_time=0.2,
                stroke_color=BLUE,
                stroke_width=4,
            )
        )

        cos_graph = axes.plot(lambda x: np.cos(x)).set_stroke(opacity=0)
        self.add(
            TracedPath(
                lambda: cos_graph.get_end(),
                dissipating_time=0.2,
                stroke_color=RED,
                stroke_width=4,
            )
        )

        self.add(axes)
        self.play(
            Create(sin_graph),
            Create(cos_graph),
            run_time=2,
            rate_func=linear,
        )

        self.wait(1)
