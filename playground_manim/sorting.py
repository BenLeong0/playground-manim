# ruff: noqa: F405, E741
from math import ceil, log2
from typing import TypeVar
from manim import *  # noqa  # type: ignore

T = TypeVar("T")


class Sorting(Scene):
    word: str = "903452358"
    word_arr: list[str]

    letters: list[Text]
    boxes: list[Square]

    def __len__(self):
        return len(self.word)

    @property
    def entries(self):
        return [
            Group(letter_text, letter_box)
            for letter_text, letter_box in zip(self.letters, self.boxes)
        ]

    def construct(self):
        self.word_arr = list(self.word)

        intro_text = Text(self.word)
        self.play(Write(intro_text))

        self.letters = [
            Text(char, line_spacing=0).shift(RIGHT * (i - len(self.word) // 2) * 1.2)
            for (i, char) in enumerate(self.word)
        ]
        self.boxes = [Square(0.8).match_coord(letter, 0) for letter in self.letters]

        self.play(ReplacementTransform(intro_text, VGroup(*self.letters)))
        self.play(*(Create(letter_box) for letter_box in self.boxes))

        # self.play(Group(*self.entries).animate.shift(UP * 2))

        for l, r in self.binary_pairings(len(self.word)):
            self.mergesort(l, r)

        for box in self.boxes:
            self.play(
                box.animate.set_fill(BLUE, opacity=0.5),
                run_time=0.05,
            )
        # for i in range(len(self.boxes) + 1):
        #     if i > 0:
        #         self.play(
        #             self.boxes[i - 1].animate.set_fill(BLUE, opacity=0.0),
        #             run_time=0.05,
        #         )
        #     if i < len(self) - 1:
        #         self.play(
        #             self.boxes[i + 1].animate.set_fill(BLUE, opacity=0.5),
        #             run_time=0.05,
        #         )

        self.wait(1)

        # self.mergesort()
        # selected = [0, 1]
        # self.play(
        #     *(letter_boxes[i].animate.set_color(YELLOW) for i in selected), run_time=0.5
        # )
        # self.play(Swap(letters[0], letters[1]))

        self.wait(1)

    def mergesort(self, l: int, r_: int):
        m = min((l + r_) // 2, len(self.word) - 1)
        r = min(r_, len(self))
        if l > 0 or r < len(self):
            self.play(
                *(entry.animate.shift(LEFT * 0.1) for entry in self.entries[:l]),
                *(entry.animate.shift(RIGHT * 0.1) for entry in self.entries[r:]),
                run_time=0.2,
            )
        self.play(
            *(box.animate.set_fill(YELLOW_B, opacity=0.8) for box in self.boxes[l:m]),
            *(box.animate.set_fill(BLUE_B, opacity=0.8) for box in self.boxes[m:r]),
            run_time=0.4,
        )

        p1, p2 = l, m
        while p1 < p2 and p2 < r:
            if p1 > l:
                self.play(
                    self.boxes[p1 - 1].animate.set_fill(GREY, opacity=0.0),
                    run_time=0.4,
                )

            if self.word_arr[p1] <= self.word_arr[p2]:
                p1 += 1
            else:
                self.play(
                    CyclicReplace(*(self.entries[p1 : p2 + 1])),
                    run_time=0.4,
                )
                self.word_arr = self.shift(self.word_arr, p2, p1)
                self.letters = self.shift(self.letters, p2, p1)
                self.boxes = self.shift(self.boxes, p2, p1)
                p1 += 1
                p2 += 1
        self.wait(0.2)

        self.play(
            *(box.animate.set_fill(WHITE, opacity=0) for box in self.boxes[l:r]),
            *(entry.animate.shift(RIGHT * 0.1) for entry in self.entries[:l]),
            *(entry.animate.shift(LEFT * 0.1) for entry in self.entries[r:]),
            run_time=0.4,
        )

    def binary_pairings(self, length: int):
        for n in range(ceil(log2(length))):
            for p1 in range(0, length, 2 ** (n + 1)):
                p2 = p1 + 2 ** (n + 1)
                yield p1, p2

    def shift(self, arr: list[T], curr_pos: int, new_pos: int) -> list[T]:
        return [
            *arr[:new_pos],
            arr[curr_pos],
            *arr[new_pos:curr_pos],
            *arr[curr_pos + 1 :],
        ]


Sorting().render()
