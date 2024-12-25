# ruff: noqa: F405
import numpy as np
from manim import *  # noqa  # type: ignore


class Himmelblau(Scene):
    def construct(self):
        resolution_fa = 160
        axes = ThreeDAxes(x_range=(-5, 5, 1), y_range=(-5, 5, 1), z_range=(0, 100, 1))

        trig_plane = axes.plot_surface(
            self.get_himmelblau_fn(1 / 3),
            resolution=(resolution_fa, resolution_fa),
            u_range=(-3, 3),
            v_range=(-3, 3),
            colorscale=[BLUE, GREEN, YELLOW, ORANGE, RED],
        )

        self.add(axes, trig_plane)

    @staticmethod
    def heatmap(x: float, y: float):
        return np.sqrt(x**2 + y**2)

    @staticmethod
    def get_himmelblau_fn(scaling_factor: float = 1 / 3):
        def himmelblau(u: float, v: float):
            x, y = u * 2, v * 2
            return ((x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2) * scaling_factor

        return himmelblau


Himmelblau().render()
