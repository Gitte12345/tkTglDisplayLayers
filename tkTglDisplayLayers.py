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


def tkTglDisplayLayersDetail(state):
    layerList = []
    if state < 2:
        displayLayer = cmds.ls(sl=1, type='displayLayer', l=1)
        for layer in displayLayer:
            cmds.setAttr(layer + '.levelOfDetail', state)

    if state == 2:
        displayLayer = cmds.ls(type='displayLayer', l=1)
        if displayLayer:
            for layer in displayLayer:
                split = layer.split(':')
                if len(split) == 1 and layer != 'defaultLayer':
                    layerList.append(layer)

    if layerList:
        levelOfDetail = cmds.getAttr(layerList[0] + '.levelOfDetail')
        for layer in layerList:
            cmds.setAttr(layer + '.levelOfDetail', 1-levelOfDetail)





# tkTglDisplayLayers()
# tkTglDisplayLayersDetail(1)
# tkTglDisplayLayersDetail(2)