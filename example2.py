from manim import *
# manim -v WARNING --disable_caching -ql -s Example1

class Example1(Scene):
    def construct(self):
        self.add(Circle())
# manim -v WARNING --disable_caching -qm HelloManim

# set the maximum width for video outputs to a predefined value
config.media_width = "20vw"
# embed video
config.media_embed = True

class HelloManim(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner_large = ManimBanner(dark_theme=False).scale(0.7)
        self.play(banner_large.create())
        self.play(banner_large.expand())