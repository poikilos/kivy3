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
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy3 import PerspectiveCamera
from kivy3 import Renderer
from kivy3 import Scene
from kivy3 import Vector3
from kivy3.loaders import OBJMTLLoader
import os

# Resources pathes
_this_path = os.path.dirname(os.path.realpath(__file__))
shader_file = os.path.join(_this_path, "../textures/simple.glsl")
obj_file = os.path.join(_this_path, "../textures/orion.obj")
mtl_file = os.path.join(_this_path, "../textures/orion.mtl")


class MainApp(App):
    def build(self):
        self.look_at = Vector3(0, 0, -1)
        root = FloatLayout()
        self.renderer = Renderer(shader_file=shader_file)
        scene = Scene()
        self.camera = PerspectiveCamera(75, 1, 1, 1000)
        self.camera.pos.z = 5
        loader = OBJMTLLoader()
        obj = loader.load(obj_file, mtl_file)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, root)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        scene.add(*obj.children)

        self.renderer.render(scene, self.camera)
        self.orion = scene.children[0]

        root.add_widget(self.renderer)
        self.renderer.bind(size=self._adjust_aspect)
        Clock.schedule_interval(self._rotate_obj, 1 / 20)
        return root

    def _adjust_aspect(self, inst, val):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "w":
            self.camera.pos.z -= 0.2
        elif keycode[1] == "s":
            self.camera.pos.z += 0.2
        elif keycode[1] == "a":
            self.camera.pos.y -= 0.2
        elif keycode[1] == "d":
            self.camera.pos.y += 0.2

        elif keycode[1] == "up":
            self.look_at.y += 0.2
        elif keycode[1] == "down":
            self.look_at.y -= 0.2
        elif keycode[1] == "right":
            self.look_at.x += 0.2
        elif keycode[1] == "left":
            self.look_at.x -= 0.2

        self.camera.look_at(self.look_at)

    def _rotate_obj(self, dt):
        self.orion.rot.x += 2
        self.orion.rot.z += 2


if __name__ == "__main__":
    MainApp().run()
