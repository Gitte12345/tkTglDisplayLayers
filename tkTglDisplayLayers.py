# tkTglDisplayLayers.py

import maya.cmds as cmds
import maya.mel as mel

def tkTglDisplayLayers():
    displayLayer = cmds.ls(type='displayLayer', l=1)
    if displayLayer:
        for layer in displayLayer:
            split = layer.split(':')
            if len(split) == 1 and layer != 'defaultLayer':
                state = cmds.getAttr(layer + '.visibility')

    for layer in displayLayer:
        split = layer.split(':')
        if len(split) == 1 and layer != 'defaultLayer':
            layerState = 1-(state*1)
            cmd2 = 'setDisplayLayerVisibility("' + str(layer) + '", ' + str(layerState) + ')'
            mel.eval(cmd2)

tkTglDisplayLayers()

