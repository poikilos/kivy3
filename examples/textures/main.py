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
from kivy3.loaders import OBJMTLLoader
import os

# Resources pathes
_this_path = os.path.dirname(os.path.realpath(__file__))
shader_file = os.path.join(_this_path, "./simple.glsl")
obj_file = os.path.join(_this_path, "./orion.obj")
mtl_file = os.path.join(_this_path, "./orion.mtl")


class MainApp(App):
    def build(self):
        root = FloatLayout()
        self.renderer = Renderer(shader_file=shader_file)
        scene = Scene()
        camera = PerspectiveCamera(15, 1, 1, 1000)
        loader = OBJMTLLoader()
        obj = loader.load(obj_file, mtl_file)

        scene.add(*obj.children)
        for obj in scene.children:
            obj.pos.z = -20.0

        self.renderer.render(scene, camera)
        self.orion = scene.children[0]

        root.add_widget(self.renderer)
        self.renderer.bind(size=self._adjust_aspect)
        Clock.schedule_interval(self._rotate_obj, 1 / 20)
        return root

    def _adjust_aspect(self, inst, val):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def _rotate_obj(self, dt):
        self.orion.rot.x += 2


if __name__ == "__main__":
    MainApp().run()
