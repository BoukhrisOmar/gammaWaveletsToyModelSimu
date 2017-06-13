
import numpy as np
from scripts.MatrixFileSystem import MatrixFileSystem
from scripts.Transforms import Transforms
from math import fabs

class ErrorCalc(Transforms) :
    """loading data in __init__"""
    def __init__ (self, wavelet_name, nbEvent, fact, cam_name, im_folder, sig_folder) :
        path2cpp = im_folder + "/" + cam_name + "/" + fact + "/" + wavelet_name + "/cleaned_telescope"
        path2sig = sig_folder + "/" + cam_name + "/" + fact
        cameras = {"dragon" : 0, "flash" : 10, "nectar" : 50, "sct" : 100} #telescope id by name
        super().__init__(cameras[cam_name])
        self.load_telescope()
        self.cpp_mfs = MatrixFileSystem (path2cpp)
        self.sig_mfs = MatrixFileSystem (path2sig)
        self.nbEvent = nbEvent

    def get_shape_err (self) :
        t = []
        for i in range (self.nbEvent) :
            cpp_mat = self.cpp_mfs.read_matrix (i)
            sig_mat = self.sig2matrix(self.sig_mfs.read_vect(i))
            sum_s = cpp_mat.sum()
            sum_s_star = sig_mat.sum()
            eps_shape = 0
            for cpp_row, sig_row in zip (cpp_mat, sig_mat) :
                for x, y in zip (cpp_row, sig_row) :
                    eps_shape += fabs((x/sum_s)-(y/sum_s_star))
            t.append(eps_shape)
        return np.array(t)

    def get_intensity_err (self) :
        t = []
        for i in range(self.nbEvent) :
            cpp_mat = self.cpp_mfs.read_matrix (i)
            sig_mat = self.sig2matrix(self.sig_mfs.read_vect(i))
            sum_s = cpp_mat.sum()
            sum_s_star = sig_mat.sum()
            eps_intensity = fabs(sum_s - sum_s_star)/sum_s_star
            t.append(eps_intensity)
        return np.array(t)
