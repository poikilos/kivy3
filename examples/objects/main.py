from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy3 import Material
from kivy3 import Object3D
from kivy3 import Scene, Renderer, PerspectiveCamera
from kivy3.extras.objects import ArrowObject
from kivy3.extras.objects import AxisObject
from kivy3.widgets import OrbitControlWidget
import os

_this_path = os.path.dirname(os.path.realpath(__file__))
shader_file = os.path.join(_this_path, "../blinnphong.glsl")
obj_file = os.path.join(_this_path, "./monkey.obj")
stl_file = os.path.join(_this_path, "./test.stl")
urdf_file = os.path.join(
    _this_path, "./rs1_description/urdf/generated_rs1_parallel.urdf"
)
package_path = os.path.join(_this_path, "./")  # parent of the package path
arrow_img_file = os.path.join(_this_path, "./assets/icon-rotate-360.png")
prismatic_arrow_img_file = os.path.join(_this_path, "./assets/icon-arrows.png")


class VisualisationWidget(FloatLayout):
    def __init__(self, **kw):
        super(VisualisationWidget, self).__init__(**kw)

        self.renderer = Renderer(shader_file=shader_file)
        self.renderer.set_clear_color((0.16, 0.30, 0.44, 1.0))

        scene = Scene()

        base = Object3D()
        # id_color = (1,0,0)

        object1 = AxisObject(length=0.5, alpha=0.4)

        base.add(object1)

        material = Material(
            color=(0, 0.3, 0), diffuse=(0, 0.3, 0), specular=(0.3, 0.3, 0.3)
        )
        object = ArrowObject(material, length=0.5, radius=0.04)
        object.pos.y = 1
        base.add(object)

        base.rot.x = -90
        scene.add(base)

        self.camera = PerspectiveCamera(90, 0.3, 0.1, 1000)
        self.camera.pos.z = 1.5
        self.camera.look_at((0, 0, 0))

        self.camera.bind_to(self.renderer)
        self.renderer.render(scene, self.camera)

        self.add_widget(self.renderer, index=30)
        self.orbit = OrbitControlWidget(self.renderer, 4.0)
        self.add_widget(self.orbit, index=99)
        # self.add_widget(self.selection_widget, index=98)
        self.renderer.bind(size=self._adjust_aspect)

    def _adjust_aspect(self, inst, val):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect


class VisualisationApp(App):
    def build(self):

        return VisualisationWidget()


if __name__ == "__main__":
    # from kivy.config import Config
    # Config.set('input', 'mouse', 'mouse,disable_multitouch')
    VisualisationApp().run()
