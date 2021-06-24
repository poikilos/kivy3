# Kivy3 - 3D graphics framework for Kivy

Kivy3 is a framework which helps people work with 3D elements and rendering
within Kivy application. Basically with Kivy and Kivy3 you may create a 3D
application for any platform Kivy supports, such as: iOS, Android, Windows,
OSX, Linux (including Raspberry Pi).

Kivy3 provides a toolset and abstraction levels to work with 3D objects like
Camera, Scene, Renderers, loaders you may use to load 3D objects.

# Installation

Create a virtual environment.

    $ python3 -m venv .
    $ ./bin/pip install -U pip
    $ ./bin/pip install wheel

To install latest development version of kivy3 run:

    $ ./bin/pip install https://github.com/kivy/kivy3/zipball/development

or, if you do local development:

    $ ./bin/pip install -e .[stl,urdf]

For further info about kivy visit
[Kivy documentation](https://kivy.org/docs/installation/installation.html).
