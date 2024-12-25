# ruff: noqa: F405
from manim import *  # noqa  # type: ignore


class Himmelblau(Scene):
    def construct(self):
        axes = ThreeDAxes(x_range=(-4, 4, 1), y_range=(-5, 5, 1), z_range=(0, 100, 1))

        scaling_factor = 1 / 3

        def himmelblau(u: float, v: float):
            x, y = u * 2, v * 2
            return ((x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2) * scaling_factor

        trig_plane = axes.plot_surface(
            himmelblau,
            resolution=160,
            u_range=(-3, 3),
            v_range=(-3, 3),
            colorscale=[BLUE, GREEN, YELLOW, ORANGE, RED],
        )

        self.add(axes, trig_plane)


Himmelblau().render()
