#--------------------------------------------------------------
# Acá voy a acumular pequeñas clases que grafican cosas específicas.
#-------------------------------------------------------------- 
# Comando para ejecutar: manim -p -ql example01.py RectangleExample
from manim import *

class a_ejemplo1(Scene):
	def construct(self):
		blue_circle = Circle(color=BLUE, fill_opacity=0.5)
		green_square = Square(color=GREEN, fill_opacity=0.8)
		green_square.next_to(blue_circle, RIGHT)
		self.add(blue_circle, green_square)

class RectangleExample(Scene):
    def construct(self):
        rect1 = Rectangle(
						width=10.0, 
						height=5.0, 
						grid_xstep=1.0, 
						grid_ystep=0.5,
						color=BLUE,
						fill_opacity=0.2,	
						)
        rect2 = Rectangle(
						width=1.0, 
						height=4.0,
						color=GREEN,
						fill_opacity=0.2,
						)
        rects = Group(rect1,rect2).arrange(buff=1)
        self.add(rects)		

class myfirstfunction(Scene):
	def construct(self):
		ax = Axes(x_range=(-5,10), y_range=(-5,10))
		curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=BLUE)
		area = ax.get_area(curve, x_range=(-2,0))
		self.add(ax, curve, area)

class mysecondfunction(Scene):
	def construct(self):
		ax = Axes(x_range=(-5,10), y_range=(-5,10))
		curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=BLUE)
		area = ax.get_area(curve, x_range=(-2,0))
		#self.wait(3)
		self.play(Create(ax), 
				#Create(curve), 
				run_time=3
				) # Puedo hacerlos agrupados o cada uno por aparte con el self.play
		self.play(Create(curve), 
				#Create(curve), 
				run_time=3
				) # Puedo hacerlos agrupados o cada uno por aparte con el self.play
		#self.play(FadeIn(curve))
		self.play(FadeIn(area))
		self.wait(0.5)
		

		
