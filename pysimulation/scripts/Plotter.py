import matplotlib.pyplot as plt
import scripts.MatrixFileSystem as MatrixFileSystem
import scripts.PyGammaSimulation as PyGammaSimulation

class Plotter :
    def __init__ (self, wavelet_name, nbEvent, fact, cam_name) :
        cameras = {"dragon" : 0, "flash" : 10, "nectar" : 50, "sct" : 100}
        self.cam_name = cam_name
        self.nbEvent = nbEvent
        self.wavelet_name = wavelet_name
        self.fact = fact
        self.pyGammaSim = PyGammaSimulation.PyGammaSimulation (cameras[cam_name])
        plt.figure (figsize=(17, 12))

    def subplot_raw (self) :
        plt.subplot2grid((2, 3), (1, 0))
        raw_mfs = MatrixFileSystem.MatrixFileSystem ("data/raw/" + self.cam_name + "/" + self.fact)
        raw_sig = raw_mfs.read_vect (self.nbEvent)
        raw_mat = self.pyGammaSim.sig2matrix(raw_sig)
        plt.imshow(raw_mat)
        plt.colorbar()
        plt.xlabel("raw signal")

        plt.subplot2grid((2, 3), (0, 0))
        self.disp = PyGammaSimulation.CameraDisplay(self.pyGammaSim.get_camera_geometry())
        self.disp.cmap = plt.cm.terrain
        self.disp.add_colorbar()
        self.disp.image = raw_sig
        plt.xlabel("raw signal")
        plt.ylabel("")


    def subplot_clean (self) :
        plt.subplot2grid((2, 3), (0, 1))
        clean_mfs = MatrixFileSystem.MatrixFileSystem ("data/im/" + self.cam_name + "/" + self.fact + "/" + self.wavelet_name + "/cleaned_telescope")
        cleaned_mat = clean_mfs.read_matrix (self.nbEvent)
        cleaned_sig = self.pyGammaSim.matrix2sig (cleaned_mat)
        self.disp = PyGammaSimulation.CameraDisplay(self.pyGammaSim.get_camera_geometry())
        self.disp.cmap = plt.cm.terrain
        self.disp.add_colorbar()
        self.disp.image = cleaned_sig
        plt.xlabel("cpp cleaned")
        plt.ylabel("")

        plt.subplot2grid((2, 3), (1, 1))
        plt.imshow(cleaned_mat)
        plt.xlabel("cpp cleaned")
        plt.colorbar()

    def subplot_sig (self) :
        plt.subplot2grid((2, 3), (0, 2))
        #plt.subplot(232)
        sig_mfs = MatrixFileSystem.MatrixFileSystem ("data/sig/" + self.cam_name + "/" + self.fact)
        sig = sig_mfs.read_vect (self.nbEvent)
        self.disp = PyGammaSimulation.CameraDisplay(self.pyGammaSim.get_camera_geometry())
        self.disp.cmap = plt.cm.terrain
        self.disp.add_colorbar()
        self.disp.image = sig
        plt.xlabel("sim clean")
        plt.ylabel("")

        plt.subplot2grid((2, 3), (1, 2))
        sig_mat = self.pyGammaSim.sig2matrix(sig)
        plt.imshow(sig_mat)
        plt.xlabel("sim clean")
        plt.colorbar()
    """
    def subplot_dwt (self) :
        plt.subplot2grid((2, 4), (1, 1))
        dwt_mfs = MatrixFileSystem.MatrixFileSystem ("data/im/" + self.cam_name + "/" + self.fact + "/" + self.wavelet_name + "/dwt")
        dwt_mat = dwt_mfs.read_matrix (self.nbEvent)
        plt.imshow(dwt_mat)
        plt.xlabel("ondelettes")
        plt.colorbar()

        plt.subplot2grid((2, 4), (1, 2))
        dwt_mfs = MatrixFileSystem.MatrixFileSystem ("data/im/" + self.cam_name + "/" + self.fact + "/" + self.wavelet_name + "/dwt_shrunk")
        dwt_mat = dwt_mfs.read_matrix (self.nbEvent)
        plt.imshow(dwt_mat)
        plt.xlabel("ondelettes")
        plt.colorbar()
    """

    def plot_all (self) :
        self.subplot_raw ()
        self.subplot_clean ()
        self.subplot_sig ()
        #self.subplot_dwt ()
        plt.show()
