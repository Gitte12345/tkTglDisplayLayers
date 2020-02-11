# tkTglDisplayLayers.py

import maya.cmds as cmds

def tkTglDisplayLayers():
    displayLayer = cmds.ls(type='displayLayer', l=1)
    if displayLayer:
        state = cmds.getAttr(displayLayer[0] + '.visibility')
        for layer in displayLayer:
            cmds.setAttr(layer + '.visibility', 1-state)

tkTglDisplayLayers()