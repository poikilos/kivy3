#
# The MIT License (MIT)
#
# Copyright (c) 2020 kivy3 Contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy3 import PerspectiveCamera
from kivy3 import Renderer
from kivy3 import Scene
from kivy3.loaders import OBJLoader
import os

# Resources pathes
_this_path = os.path.dirname(os.path.realpath(__file__))
shader_file = os.path.join(_this_path, "./blinnphong.glsl")
obj_file = os.path.join(_this_path, "./MQ-27.obj")


class MainApp(App):
    def build(self):
        root = FloatLayout()
        self.renderer = Renderer(shader_file=shader_file)
        scene = Scene()
        camera = PerspectiveCamera(90, 1, 1, 10000)

        # loader = OBJMTLLoader()
        # obj = loader.load(obj_file, mtl_file)

        loader = OBJLoader()
        obj = loader.load(obj_file)

        self.renderer.main_light.pos = 1, 20, 50
        self.renderer.main_light.intensity = 1000

        camera.pos = 0, 0, 50
        camera.look_at((0, 0, 0))

        scene.add(*obj.children)
        for obj in scene.children:
            obj.pos.z = -0.0
            obj.scale = 0.1, 0.1, 0.1

        self.renderer.render(scene, camera)
        self.orion = scene.children

        root.add_widget(self.renderer)
        self.renderer.bind(size=self._adjust_aspect)
        Clock.schedule_interval(self._rotate_obj, 1 / 20)
        # Clock.schedule_interval(self.print_color, 2)
        return root

    def _adjust_aspect(self, inst, val):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def _rotate_obj(self, dt):
        # self.renderer.main_light.pos = 1, 20, 50
        for child in self.orion:
            child.rot.x += 2


if __name__ == "__main__":
    MainApp().run()
