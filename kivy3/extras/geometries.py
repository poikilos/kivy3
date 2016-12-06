"""
The MIT License (MIT)

Copyright (c) 2013 Niko Skrypnik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from kivy3 import Vector3
from kivy3.core.geometry import Geometry
from kivy3.core.face3 import Face3
from math import sqrt


def get_normals(faces, vertices):
    normals = []
    for face in faces:
        ix = face[0]
        iy = face[1]
        iz = face[2]
        norm = (
            vertices[ix][0] + vertices[iy][0] + vertices[iz][0],
            vertices[ix][1] + vertices[iy][1] + vertices[iz][1],
            vertices[ix][2] + vertices[iy][2] + vertices[iz][2]
        )
        det = sqrt(norm[0] * norm[0] + norm[1] * norm[1] + norm[2] * norm[2])
        norm = [n / float(det) for n in norm]
        normals.append(norm)
    return normals


class BoxGeometry(Geometry):

    _cube_vertices = [(-1, 1, -1), (1, 1, -1),
                      (1, -1, -1), (-1, -1, -1),
                      (-1, 1, 1), (1, 1, 1),
                      (1, -1, 1), (-1, -1, 1),
                      ]

    _cube_faces = [(0, 1, 2), (0, 2, 3), (3, 2, 6),
                   (3, 6, 7), (7, 6, 5), (7, 5, 4),
                   (4, 5, 1), (4, 1, 0), (4, 0, 3),
                   (7, 4, 3), (5, 1, 2), (6, 5, 2)
                   ]

    _cube_normals = [(0, 0, 1), (-1, 0, 0), (0, 0, -1),
                     (1, 0, 0), (0, 1, 0), (0, -1, 0)
                     ]

    def __init__(self, width, height, depth, **kw):
        name = kw.pop('name', '')
        super(BoxGeometry, self).__init__(name)
        self.width_segment = kw.pop('width_segment', 1)
        self.height_segment = kw.pop('height_segment', 1)
        self.depth_segment = kw.pop('depth_segment', 1)

        self.w = width
        self.h = height
        self.d = depth

        self._build_box()

    def _build_box(self):

        for v in self._cube_vertices:
            v = Vector3(0.5 * v[0] * self.w,
                        0.5 * v[1] * self.h,
                        0.5 * v[2] * self.d)
            self.vertices.append(v)

        n_idx = 0
        for f in self._cube_faces:
            face3 = Face3(*f)
            normal = self._cube_normals[n_idx / 2]
            face3.vertex_normals = [normal, normal, normal]
            n_idx += 1
            self.faces.append(face3)


class TetrahedronGeometry(Geometry):

    _tetra_vertices = [(1, 1, 1), (-1, -1, 1),
                      (-1, 1, -1), (1, -1, -1)
    ]

    _tetra_faces = [(0, 1, 2), (0, 2, 3), (0, 1, 3),
                   (1, 2, 3)
                   ]

    _tetra_normals = [(-1, 1, 1), (1, 1, -1),
                      (1, -1, 1), (-1, -1, 0)
                     ]

    def __init__(self, width, height, depth, **kw):
        name = kw.pop('name', '')
        super(TetrahedronGeometry, self).__init__(name)
        self.width_segment = kw.pop('width_segment', 1)
        self.height_segment = kw.pop('height_segment', 1)
        self.depth_segment = kw.pop('depth_segment', 1)

        self.w = width
        self.h = height
        self.d = depth

        self._build_geo()

    def _build_geo(self):

        for v in self._tetra_vertices:
            v = Vector3(0.5 * v[0] * self.w,
                        0.5 * v[1] * self.h,
                        0.5 * v[2] * self.d)
            self.vertices.append(v)

        n_idx = 0
        for f in self._tetra_faces:
            face3 = Face3(*f)
            normal = self._tetra_normals[n_idx / 2]
            face3.vertex_normals = [normal, normal, normal]
            n_idx += 1
            self.faces.append(face3)


class OctahedronGeometry(Geometry):

    _octa_vertices = [(0, 0, -1), (1, 0, 0),
                      (0, -1, 0), (0, 1, 0),
                      (-1, 0, 0), (0, 0, 1)
    ]

    _octa_faces = [(0, 1, 2), (0, 1, 3),
                   (0, 2, 4), (0, 3, 4),
                   (1, 2, 5), (1, 3, 5),
                   (2, 4, 5), (3, 4, 5)
                   ]

    _octa_normals = [(1, -1, -1), (1, 1, -1),
                     (-1, -1, -1), (-1, 1, -1),
                     (1, -1, 1), (1, 1, 1),
                     (-1, -1, 1), (-1, 1, 1)
                     ]

    def __init__(self, width, height, depth, **kw):
        name = kw.pop('name', '')
        super(OctahedronGeometry, self).__init__(name)
        self.width_segment = kw.pop('width_segment', 1)
        self.height_segment = kw.pop('height_segment', 1)
        self.depth_segment = kw.pop('depth_segment', 1)

        self.w = width
        self.h = height
        self.d = depth

        self._build_geo()

    def _build_geo(self):

        for v in self._octa_vertices:
            v = Vector3(0.5 * v[0] * self.w,
                        0.5 * v[1] * self.h,
                        0.5 * v[2] * self.d)
            self.vertices.append(v)

        n_idx = 0
        for f in self._octa_faces:
            face3 = Face3(*f)
            normal = self._octa_normals[n_idx / 2]
            face3.vertex_normals = [normal, normal, normal]
            n_idx += 1
            self.faces.append(face3)


class SphereGeometry(Geometry):

    _sphere_vertices = [
        (-0.749908, -0.500243, -0.432973), (-0.432920, -0.866268, -0.249961),
        (-0.499908, -0.000243, -0.865986), (-0.432920, -0.500243, -0.749961),
        (-0.749908, 0.499757, -0.432974), (-0.865933, -0.000243, -0.499961),
        (-0.999908, -0.000243, 0.000039), (-0.865933, -0.500243, 0.000039),
        (-0.499908, -0.866268, 0.000039), (-0.432920, 0.865783, -0.249961),
        (-0.249908, 0.865783, -0.432973), (-0.432920, 0.499757, -0.749961),
        (0.433105, -0.500243, -0.749961), (0.250092, -0.866268, -0.432973),
        (-0.499908, -0.000243, 0.866064), (-0.432920, -0.500243, 0.750039),
        (-0.749908, -0.500243, 0.433052), (-0.432920, -0.866268, 0.250039),
        (0.866117, -0.000243, -0.499961), (0.750092, -0.500243, -0.432973),
        (-0.249908, -0.866268, -0.432973), (0.000092, 0.865783, -0.499961),
        (0.000092, -0.500243, -0.865986), (0.000092, -0.866268, -0.499961),
        (0.433105, 0.499757, -0.749961), (0.500092, -0.000243, -0.865986),
        (-0.249908, -0.866268, 0.433052), (-0.432920, 0.865783, 0.250039),
        (-0.749908, 0.499757, 0.433052), (-0.865933, -0.000243, 0.500039),
        (0.000092, 0.499757, -0.865986), (0.000092, -0.000243, -0.999961),
        (0.433105, 0.865783, -0.249961), (0.750092, 0.499757, -0.432974),
        (0.433105, -0.866268, -0.249961), (0.500092, 0.865783, 0.000039),
        (-0.499908, 0.865783, 0.000039), (-0.865933, 0.499757, 0.000039),
        (0.866117, -0.500243, 0.000039), (0.500092, -0.866268, 0.000039),
        (0.500092, -0.000243, 0.866064), (0.433105, -0.500243, 0.750039),
        (0.000092, -0.500243, 0.866064), (0.000092, -0.866268, 0.500039),
        (0.750092, -0.500243, 0.433052), (0.433105, -0.866268, 0.250039),
        (-0.249908, 0.865783, 0.433052), (-0.432920, 0.499757, 0.750039),
        (0.000092, 0.999757, 0.000039), (0.250092, 0.865783, -0.432973),
        (0.866118, 0.499757, 0.000039), (1.000092, -0.000243, 0.000039),
        (0.000092, -1.000243, 0.000039), (0.433105, 0.865783, 0.250039),
        (0.750092, 0.499757, 0.433052), (0.866117, -0.000243, 0.500039),
        (0.250092, -0.866268, 0.433052), (0.000092, 0.865783, 0.500039),
        (0.000092, 0.499757, 0.866064), (0.000092, -0.000243, 1.000039),
        (0.250092, 0.865783, 0.433052), (0.433105, 0.499757, 0.750039)
    ]

    _sphere_faces = [
        (15, 20, 21), (36, 25, 30), (21, 20, 26), (36, 30, 35),
        (26, 20, 31), (36, 35, 41), (31, 20, 37), (36, 41, 46),
        (14, 13, 18), (18, 19, 14), (13, 12, 17), (17, 18, 13),
        (12, 11, 16), (16, 17, 12), (11, 10, 15), (15, 16, 11),
        (19, 18, 24), (24, 25, 19), (18, 17, 23), (23, 24, 18),
        (17, 16, 22), (22, 23, 17), (16, 15, 21), (21, 22, 16),
        (25, 24, 29), (29, 30, 25), (24, 23, 28), (28, 29, 24),
        (23, 22, 27), (27, 28, 23), (22, 21, 26), (26, 27, 22),
        (30, 29, 34), (34, 35, 30), (29, 28, 33), (33, 34, 29),
        (28, 27, 32), (32, 33, 28), (27, 26, 31), (31, 32, 27),
        (37, 20, 42), (36, 46, 51), (42, 20, 47), (36, 51, 56),
        (41, 40, 45), (45, 46, 41), (40, 39, 44), (44, 45, 40),
        (39, 38, 43), (43, 44, 39), (38, 37, 42), (42, 43, 38),
        (46, 45, 50), (50, 51, 46), (45, 44, 49), (49, 50, 45),
        (44, 43, 48), (48, 49, 44), (43, 42, 47), (47, 48, 43),
        (51, 50, 55), (55, 56, 51), (50, 49, 54), (54, 55, 50),
        (49, 48, 53), (53, 54, 49), (48, 47, 52), (52, 53, 48),
        (56, 55, 60), (60, 61, 56), (55, 54, 59), (59, 60, 55),
        (54, 53, 58), (58, 59, 54), (53, 52, 57), (57, 58, 53),
        (5, 20, 10), (36, 14, 19), (10, 20, 15), (36, 19, 25),
        (47, 20, 52), (36, 56, 61), (52, 20, 57), (36, 61, 4),
        (35, 34, 40), (40, 41,35), (34, 33, 39), (39, 40, 34),
        (33, 32, 38), (38, 39, 33), (32, 31, 37), (37,38, 32),
        (57, 20, 0), (36, 4, 9), (0, 20, 5), (36, 9, 14),
        (61, 60, 3), (3, 4, 61), (60, 59, 2), (2, 3, 60),
        (59, 58, 1), (1, 2, 59), (58, 57, 0), (0, 1, 58),
        (9, 8, 13), (13, 14, 9), (8, 7, 12), (12, 13, 8),
        (7, 6, 11), (11, 12, 7), (6, 5, 10), (10, 11, 6),
        (4, 3, 8), (8, 9, 4), (3, 2, 7), (7, 8, 3),
        (2, 1, 6), (6, 7, 2), (1, 0, 5), (5, 6, 1)
    ]

    _sphere_normals = get_normals(_sphere_faces, _sphere_vertices)

    def __init__(self, width, height, depth, **kw):
        name = kw.pop('name', '')
        super(SphereGeometry, self).__init__(name)
        self.width_segment = kw.pop('width_segment', 1)
        self.height_segment = kw.pop('height_segment', 1)
        self.depth_segment = kw.pop('depth_segment', 1)

        self.w = width
        self.h = height
        self.d = depth

        self._build_geo()

    def _build_geo(self):

        for v in self._sphere_vertices:
            v = Vector3(0.5 * v[0] * self.w,
                        0.5 * v[1] * self.h,
                        0.5 * v[2] * self.d)
            self.vertices.append(v)

        n_idx = 0
        for f in self._sphere_faces:
            face3 = Face3(*f)
            normal = self._sphere_normals[n_idx / 2]
            face3.vertex_normals = [normal, normal, normal]
            n_idx += 1
            self.faces.append(face3)
