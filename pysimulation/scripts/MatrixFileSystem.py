
# coding: utf-8

"""
module contenant des fonctions utiles pour les utilitaires dispos
"""

import os
from math import log2, sqrt, log, exp
import numpy as np
import PMatrixFloat as PMatF

"""
def ensure_path (direc) :
    return None
def read_matrix (self, nEvent) :
    return 2D np.array
def store_cpp_mat (self, mat, id) :
    return None, stores 1 row/line and threshold at 1st line
def save_text2bin (self, nevent) :
    return None, stores a matrix from text to bin file
def read_vect (self, nEvent) :
    return 1D np.array
def store_vect (self, vect, id) :
    return None
def load_rapport (self, vect, fact) :
    return None
def store_rapport (self, vect, fact) :
    return None
"""
class MatrixFileSystem :
    def __init__ (self, dir) :
        self.dir = dir
        self.ensure_path(self.dir)
        self.pmf = PMatF.PMatrixFloat()

    def ensure_path (self, direc) :
        if not os.path.exists(direc):
            os.makedirs(direc)

    def read_matrix (self, nEvent) :
        self.ensure_path(self.dir)
        self.pmf.load (self.dir + "/event" + str(nEvent) + ".tab2d")
        return np.array(self.pmf.getMat())

    def save_text2bin (self, nEvent) :
        f = open(self.dir + "/event" + str(nEvent) + ".tab2d", "r")
        m = eval(f.read())
        f.close()
        self.pmf._mat = np.array(m)
        self.pmf.save(self.dir + "/event" + str(nEvent) + ".tab2d")

    def store_cpp_mat (self, mat, id, thr) :
        """ was store_mat_from_list()"""
        self.ensure_path(self.dir + "/telescope")
        mat_str = str(mat.tolist())
        mat_str = mat_str.replace ("], [", "\n")
        mat_str = mat_str.replace ("[", "")
        mat_str = mat_str.replace ("]", "")
        mat_str = mat_str.replace (",", "")
        f = open (self.dir + "/telescope/event" + str(id) + ".tab2d", "w")
        """
        if thr in ["haar8", "haar8_nei"] :
            #f.write(str((sqrt(log (mat.sum()))/2. * mat.std() + mat.mean())) + "\n")
            f.write(str((sqrt(2*log2 (mat.sum())) * mat.std() + mat.mean())) + "\n")
        elif thr in ["db2", "db2_nei"]:
            f.write(str((sqrt(log2 (mat.sum())) * mat.std()) + mat.mean()**2) + "\n")
        else : #walsh walsh_nei
            f.write(str((sqrt(2*log2 (mat.sum())) * mat.std() + mat.mean())) + "\n")
        #"""
        f.write(mat_str)
        f.close()

    def read_vect (self, nEvent) :
        self.pmf.load (self.dir + "/telescope/event" + str(nEvent) + ".tab1d")
        return np.array(self.pmf.getMat()[0])

    def store_vect (self, vect, id) :
        self.ensure_path(self.dir + "/telescope")
        self.pmf._mat = np.array([vect])
        self.pmf.save (self.dir + "/telescope/event" + str(id) + ".tab1d")

    def store_rapport (self, vect, fname) :
        self.pmf._mat = np.array([vect])
        self.pmf.save (self.dir + "/fact_" + fname + ".tab1d")

    def load_rapport (self, param_name) :
        self.pmf.load (self.dir + "/fact_" + param_name + ".tab1d")
        return np.array(self.pmf.getMat()[0])
