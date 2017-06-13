import PCalibRun
import ctadata
import ctawrapper as wrp

import ctapipe.image.toymodel as toy
from ctapipe.instrument import CameraGeometry
from ctapipe.visualization import CameraDisplay
from matplotlib import pyplot as plt
import numpy as np
from astropy import units as u
from math import fabs
#%matplotlib inline

import random
import sys

import scripts.MatrixFileSystem as MatrixFileSystem
import scripts.PyGammaSimulation as PyGammaSimulation
import scripts.MyProgressBar as MyProgressBar

"""
argv :
    wavelet_name, nb_events, sn_fact, cam_name, image_folder, signal_folder, noise_folder, raw_folder
"""

help_msg = "argv :\n\twavelet_name, nb_events, sn_fact, cam_name, image_folder, signal_folder, noise_folder, raw_folder"


if len(sys.argv) == 9 :
    wavelet_name = sys.argv[1]
    nb_events = int(sys.argv[2])
    fact = float(sys.argv[3])
    cam_name = sys.argv[4]
    image_folder = sys.argv[5] + "/" + cam_name + "/" + str(fact)
    signal_folder = sys.argv[6] + "/" + cam_name + "/" + str(fact)
    noise_folder = sys.argv[7] + "/" + cam_name + "/" + str(fact)
    raw_folder = sys.argv[8] + "/" + cam_name + "/" + str(fact)
else :
    print (help_msg)
    exit()

mfs_image = MatrixFileSystem.MatrixFileSystem(image_folder)
mfs_signal = MatrixFileSystem.MatrixFileSystem(signal_folder)
mfs_noise = MatrixFileSystem.MatrixFileSystem(noise_folder)
mfs_raw = MatrixFileSystem.MatrixFileSystem(raw_folder)

cameras = {"dragon" : 0, "flash" : 10, "nectar" : 50, "sct" : 100}
pyGammaSim = PyGammaSimulation.PyGammaSimulation(cameras[cam_name])
progbar = MyProgressBar.MyProgressBar(nb_events)

for i in range(nb_events) :
    (im, sig, noi) = pyGammaSim.generate_signal(sn=fact, threshold=0.04)

    #to n-diagonal matrix
    mat_im = pyGammaSim.sig2matrix(im)
    #change to : store_cpp_mat(im, i, wavelet_name)
    #@store_cpp_mat : mat_im.std() ... ==> im.std()
    mfs_image.store_cpp_mat (mat_im, i, wavelet_name)
    mfs_signal.store_vect (sig, i)
    mfs_noise.store_vect (noi, i)
    mfs_raw.store_vect (im, i)

    progbar.update()
print ("")
