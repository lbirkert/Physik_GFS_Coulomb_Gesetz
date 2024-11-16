from manim import Scene, Write, Text

class MyScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))