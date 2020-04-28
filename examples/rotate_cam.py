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
from kivy3 import Material
from kivy3 import Mesh
from kivy3 import PerspectiveCamera
from kivy3 import Renderer
from kivy3 import Scene
from kivy3.extras.geometries import SphereGeometry
from kivy3.loaders import STLLoader
from kivy3.widgets import OrbitControlWidget
import os

_this_path = os.path.dirname(os.path.realpath(__file__))
shader_file = os.path.join(_this_path, "./blinnphong.glsl")
obj_file = os.path.join(_this_path, "./monkey.obj")
stl_file = os.path.join(_this_path, "./test.stl")


class SceneApp(App):
    def build(self):
        root = FloatLayout()

        self.renderer = Renderer(shader_file=shader_file)
        self.renderer.set_clear_color((0.16, 0.30, 0.44, 1.0))

        scene = Scene()
        # geometry = CylinderGeometry(0.5, 2)
        geometry = SphereGeometry(1)
        # geometry = BoxGeometry(1, 1, 1)
        material = Material(
            color=(0.3, 0.0, 0.3), diffuse=(0.3, 0.3, 0.3), specular=(0.1, 0.1, 0.1)
        )

        loader = STLLoader()
        obj = loader.load(stl_file, material)
        self.item = obj
        self.theta = 0.0

        scene.add(self.item)

        self.cube = Mesh(geometry, material)
        self.item.pos.z = 0

        # self.cube.pos.z=-5
        self.camera = PerspectiveCamera(75, 0.3, 0.5, 1000)
        self.camera.pos.z = 1.5
        self.camera.look_at((0, 0, 0))
        # camera = OrthographicCamera()

        # scene.add(self.cube)
        self.camera.bind_to(self.renderer)
        self.renderer.render(scene, self.camera)

        root.add_widget(self.renderer)

        orbit = OrbitControlWidget(self.renderer, 4.0)

        root.add_widget(orbit)

        Clock.schedule_interval(self._rotate_cube, 1 / 20)
        self.renderer.bind(size=self._adjust_aspect)

        return root

    def _adjust_aspect(self, inst, val):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def _rotate_cube(self, dt):
        # self.cube.rotation.x += 1
        # self.cube.rotation.y += 1
        # self.cube.rotation.z += 1
        # self.item.rotation.x += 1
        # self.item.rotation.y += 1
        # self.item.rotation.z += 1
        # self.camera.look_at((0,1,0))

        # self.camera.pos.x = math.sin(self.theta) * 1.
        # self.camera.pos.z = math.cos(self.theta) * 1.

        # self.theta += 0.05

        pass
        # self.camera.update()


if __name__ == "__main__":
    # from kivy.config import Config
    # Config.set('input', 'mouse', 'mouse,disable_multitouch')
    SceneApp().run()
