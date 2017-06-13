
import matplotlib.pyplot as plt
import scripts.MatrixFileSystem as MatrixFileSystem


class HillasPlotter :
    def __init__ (self, cam_name, wavelet_name, list_fact) :
        self.list_fact = list_fact
        self.path = "validation_data/" + cam_name + "/" + wavelet_name + "/rapport"
        self.color = ["red", "blue", "pink", "green", "orange"]


    def get_cen_x (self) :
        plt.subplot2grid((2, 4), (0, 0))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("cen_x")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), range=(-0.1, 0.1), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("cen_x")



    def get_cen_y (self) :
        plt.subplot2grid((2, 4), (0, 1))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("cen_y")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), range=(-0.1, 0.1), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("cen_y")

    def get_length (self) :
        plt.subplot2grid((2, 4), (0, 2))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("length")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("length")

    def get_width (self) :
        plt.subplot2grid((2, 4), (0, 3))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("width")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("width")

    def get_psi (self) :
        plt.subplot2grid((2, 4), (1, 0))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("psi")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), range=(-0.1, 0.1), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("psi")

    def get_phi (self) :
        plt.subplot2grid((2, 4), (1, 1))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("phi")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), range=(-0.1, 0.1), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("phi")

    def get_skewness (self) :
        plt.subplot2grid((2, 4), (1, 2))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("skewness")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), range=(-2, 2), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("skewness")

    def get_kurtosis (self) :
        plt.subplot2grid((2, 4), (1, 3))
        alpha = 0.66
        tab_to_hist = []
        for i, c in zip(self.list_fact, self.color) :
            rapport_mfs = MatrixFileSystem.MatrixFileSystem(self.path + str(i))
            tab_to_hist=rapport_mfs.load_rapport("kurtosis")
            plt.hist(tab_to_hist, bins=100, alpha=alpha, label=str(i), color=c)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("kurtosis")

    def plot_all (self) :
        self.get_cen_x ()
        self.get_cen_y ()
        self.get_length ()
        self.get_width ()
        self.get_psi ()
        self.get_phi ()
        self.get_skewness ()
        self.get_kurtosis ()
        plt.show()
