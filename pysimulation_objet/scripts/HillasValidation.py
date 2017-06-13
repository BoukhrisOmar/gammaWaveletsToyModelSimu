

import ctapipe.image.hillas as hillas
import scripts.MatrixFileSystem as MatrixFileSystem
import scripts.Transforms as Transforms

from math import sqrt, degrees


class HillasValidation (Transforms.Transforms):
    def __init__ (self, wavelet_name, fact, cam_name, dir_clean="data/im", dir_sim="data/sig") :
        cameras = {"dragon" : 0, "flash" : 10, "nectar" : 50, "sct" : 100} #telescope id by name
        super().__init__(cameras[cam_name])
        self.load_telescope()
        self.clean_mfs = MatrixFileSystem.MatrixFileSystem(dir_clean + "/" + cam_name + "/" + fact + "/" + wavelet_name + "/cleaned_telescope")
        self.sim_mfs = MatrixFileSystem.MatrixFileSystem(dir_sim + "/" + cam_name + "/" + fact)

    def load_data (self, nEvent) :
        self.sig_clean = self.matrix2sig(self.clean_mfs.read_matrix(nEvent))
        self.sig_sim = self.sim_mfs.read_vect(nEvent)

    def save_data (self) :
        hillas1 = hillas.hillas_parameters(self.tabx, self.taby, self.sig_clean)
        hillas2 = hillas.hillas_parameters(self.tabx, self.taby, self.sig_sim)
        return [hillas1, hillas2]
