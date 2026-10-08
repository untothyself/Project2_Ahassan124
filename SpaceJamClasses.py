from typing import cast

from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import Loader
from panda3d.core import *


# planet model and texture
class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath,
                 nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = cast(NodePath, loader.loadModel(modelPath))
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = cast(Texture, loader.loadTexture(texPath))
        self.modelNode.setTexture(tex, 1)


# universe model and texture
class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath,
                 nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = cast(NodePath, loader.loadModel(modelPath))
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = cast(Texture, loader.loadTexture(texPath))
        self.modelNode.setTexture(tex, 1)


# space station model and texture
class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath,
                 nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = cast(NodePath, loader.loadModel(modelPath))
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = cast(Texture, loader.loadTexture(texPath))
        self.modelNode.setTexture(tex, 1)


# spaceship model and texture
class Spaceship(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath,
                 nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = cast(NodePath, loader.loadModel(modelPath))
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = cast(Texture, loader.loadTexture(texPath))
        # replace the ship texture
        self.modelNode.clearTexture()
        self.modelNode.setTexture(tex, 1)


# player ship
class Player(Spaceship):
    pass


# drone model and texture
class Drone(ShowBase):
    # counts the drones
    droneCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath,
                 nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        Drone.droneCount += 1
        self.modelNode = cast(NodePath, loader.loadModel(modelPath))
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName + str(Drone.droneCount))
        tex = cast(Texture, loader.loadTexture(texPath))
        self.modelNode.setTexture(tex, 1)
