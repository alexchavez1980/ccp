# Librerías necesarias: https://docs.manim.community/en/stable/installation/windows.html#required-dependencies
# No me anduvieron, alterné con:
# pip install manimce
# pip install ffmpeg
# pip install manim
 
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen