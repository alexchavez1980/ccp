#--------------------------------------------------------------
# Acá voy a acumular pequeñas clases que grafican cosas específicas.
#-------------------------------------------------------------- 
# Comando para ejecutar: manim -pql example01.py RectangleExample
# Comando para ejecutar: manim -pqh example01.py RectangleExample ALTA DEFINICION

from manim import *
from latex import *

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
		
class contexto(Scene):
	def construct(self):
		ax = Axes(x_range=(-5,10), y_range=(-5,10))
		curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=BLUE)
		area = ax.get_area(curve, x_range=(-2,0))
		#self.wait(3)
		texto=Text("Esto es una prueba de Manim", font="sans-serif")
		#texto=Text("Beto, ponete a trabajar!!!")
		self.play(Write(texto))
		self.wait(1)
		self.play(FadeOut(texto))
		self.wait(1)

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
		self.play(FadeOut(ax, curve, area))
		
		#texto2=Text("Si, no tiene nada que ver la gráfica!")
		#texto3=Text("Toy probando")
		texto2=Text("Si, no tiene nada que ver la gráfica!").move_to(RIGHT+UP)
		texto3=Text("Toy probando").move_to(DOWN*3.2)
		self.play(FadeIn(texto2))
		self.wait(2)
		self.play(Transform(texto2,texto3))
		self.wait(2)
		
