import PCalibRun
import ctadata
import ctawrapper as wrp

import plibs_8
import ctapipe.image.toymodel as toy
from ctapipe.instrument import CameraGeometry
from ctapipe.visualization import CameraDisplay
from matplotlib import pyplot as plt
import numpy as np
from astropy import units as u
#%matplotlib inline

import random

"""
                   __
              __ /    \ __
            /    \ __ /    \
            \ __ /    \ __ /
            /    \ __ /    \
            \ __ /    \ __ /
                 \ __ /
                   ||
                  _||_
                  \  /
                   \/
            +----+----+
            |    |    |
            +----+----+----+
            |    |    |    |
            +----+----+----+
                 |    |    |
                 +----+----+
"""
class Transforms :

    def __init__ (self, nTel) :
        self.nTel = nTel

    def load_telescope (self) :
        """
        Sets tab_inj, mat_event (@0), camera geometry (geom)
        """
        num_tel = self.nTel
        self.nTel = PCalibRun.PCalibTel()
        self.nTel.load("data/prun/telescope_" + str(num_tel) + ".pcalibrun")
        tabPos = self.nTel.getTabPos()
        tabPix = tabPos.getTabPixelPosXY()

        self.tabx = [tabPix[i] for i in range(len(tabPix)) if i % 2 == 0]
        self.taby = [tabPix[i] for i in range(len(tabPix)) if i % 2 == 1]
        self.tab_inj, self.nbr, self.nbc = wrp.createAutoInjunctionTable(tabPix)

        self.mat_event = np.zeros((self.nbr, self.nbc))
        self.sig_event = np.zeros(len(self.tabx))

    def sig2matrix (self, sig) :
        return ctadata.telescope2matrix(self.mat_event, sig, self.tab_inj)

    def matrix2sig (self, mat) :
        return ctadata.matrix2telescope(self.sig_event, mat, self.tab_inj)
