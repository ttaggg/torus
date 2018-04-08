from mayavi import mlab
from tvtk.tools import visual
from traits.api import Range, on_trait_change, HasTraits, Instance, Button, Enum
from traitsui.api import View, Item, HGroup, Group
from mayavi.core.ui.api import SceneEditor, MlabSceneModel
import numpy as np
from numpy import pi, sin, cos, sqrt
from shapes import *

#################
### VISUALIZE ###
#################
class Visualization(HasTraits):
    p = Range(0, 30, 1)
    q = Range(0, 30, 1)
    p2 = Range(0, 30, 3)
    q2 = Range(0, 30, 2)
    op = Enum(1, 0.75, 0.5, 0.25, 0)
    scene = Instance(MlabSceneModel, ())

    create_data = Button('Draw the curve (experimental)')
    def _create_data_fired(self):
        coordinates = getLine()
        u = []
        v = []
        pieces = 50
        for j in range(len(coordinates)-1):
            u.extend(np.linspace(coordinates[j][0],coordinates[j+1][0], pieces, endpoint=False))
            v.extend(np.linspace(coordinates[j][1],coordinates[j+1][1], pieces, endpoint=False))

        self.u = np.array(u)
        self.v = np.array(v)
        self.update_op()

    def __init__(self):
        HasTraits.__init__(self)
        self.scene.background = (1,1,1)
        self.u = np.linspace(0,1,len(tt))
        self.v = np.linspace(0,0,len(tt))

    @on_trait_change('scene.activated')
    def create_scene(self):
        self.torus = self.scene.mlab.mesh( *torus() , color=(0.75,0.75,0.75), opacity = self.op, figure = self.scene.mayavi_scene)
        self.scene.mlab.plot3d( *curve(1, 0) , color = (1,1,1))
        self.scene.mlab.plot3d( *curve(0, 1) , color = (1,1,1))
        self.plot = self.scene.mlab.plot3d( *curve(self.p, self.q) , color = (1,0,0))
        self.plot2 = self.scene.mlab.plot3d( *curve(self.p2, self.q2) , color = (0,1,0))
        self.plot3 = self.scene.mlab.plot3d( *curveArbitrary(self.u,self.v) , color = (0,0,1))

    @on_trait_change('p')
    def update_p(self):
        x, y, z = curve(self.p, self.q)
        self.plot.mlab_source.set(x=x, y=y, z=z)
    @on_trait_change('q')
    def update_q(self):
        x, y, z = curve(self.p, self.q)
        self.plot.mlab_source.set(x=x, y=y, z=z)
    @on_trait_change('p2')
    def update_p2(self):
        x, y, z = curve(self.p2, self.q2)
        self.plot2.mlab_source.set(x=x, y=y, z=z)
    @on_trait_change('q2')
    def update_q2(self):
        x, y, z = curve(self.p2, self.q2)
        self.plot2.mlab_source.set(x=x, y=y, z=z)
    @on_trait_change('op')
    def update_op(self):
        self.scene.mlab.clf(figure = self.scene.mayavi_scene)
        self.create_scene()

    view = View(Group(Item('scene', height=500, width=500, show_label=False,
                    editor=SceneEditor()), Group('p','q','p2','q2','op'),Item('create_data', show_label=False)),
                resizable=True)

Visualization().configure_traits()
