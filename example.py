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

class a_ejemplo1(Scene):
	def construct(self):
		blue_circle = Circle(color=BLUE, fill_opacity=0.5)
		green_square = Square(color=GREEN, fill_opacity=0.8)
		green_square.next_to(blue_circle, RIGHT)
		self.add(blue_circle, green_square)

class a_ejemplo2(Scene):
	def construct(self):
		blue_circle = Circle(color=BLUE, fill_opacity=0.5)
		green_square = Square(color=GREEN, fill_opacity=0.8)
		green_square.next_to(blue_circle, RIGHT)
        self.play(Create(blue_circle))  # show the circle on screen
		#self.add(blue_circle, green_square)

        