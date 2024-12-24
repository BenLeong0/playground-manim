import sys

from playground_manim.helloworld import HelloWorld
from playground_manim.sin import Sin
from playground_manim.sorting import Sorting
from playground_manim.trig import Trig


def render():
    match (scene_name := " ".join(sys.argv[1:])):
        case "Hello World":
            HelloWorld().render()
        case "Sin":
            Sin().render()
        case "Trig":
            Trig().render()
        case "Sort":
            Sorting().render()
        case _:
            raise ValueError(f"Invalid {scene_name=}")
