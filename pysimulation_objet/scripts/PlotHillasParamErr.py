import matplotlib.pyplot as plt
import scripts.MatrixFileSystem as MatrixFileSystem

class PlotHillasParamErr :
    def __init__ (self, wave_list, fact_list, cam_name) :
        self.factL = fact_list
        self.waveL = wave_list
        self.cam_name   = cam_name
        self.color = ["red", "blue", "pink", "green", "orange"]

    def get_cen_x (self) :
        plt.subplot2grid((2, 4), (0, 0))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("cen_x")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("cen_x")
    def get_cen_y (self) :
        plt.subplot2grid((2, 4), (0, 1))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("cen_y")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("cen_y")
    def get_length (self) :
        plt.subplot2grid((2, 4), (0, 2))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("length")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("length")
    def get_width (self) :
        plt.subplot2grid((2, 4), (0, 3))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("width")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("width")
    def get_psi (self) :
        plt.subplot2grid((2, 4), (1, 0))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("psi")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("psi")
    def get_phi (self) :
        plt.subplot2grid((2, 4), (1, 1))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("phi")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("phi")
    def get_skewness (self) :
        plt.subplot2grid((2, 4), (1, 2))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("skewness")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
        plt.legend()
        #plt.yscale("log")
        plt.xlabel("skewness")
    def get_kurtosis (self) :
        plt.subplot2grid((2, 4), (1, 3))
        alpha = 0.66
        for i in self.waveL :
            paramTab, y, err = [], [], []
            for j in self.factL :
                rapport_mfs = MatrixFileSystem.MatrixFileSystem("validation_data/" + self.cam_name + "/" + i + "/rapport" + str(j))
                paramTab = rapport_mfs.load_rapport("kurtosis")
                y.append (paramTab.mean())
                err.append (paramTab.std())
            plt.errorbar(self.factL, y, yerr=err, fmt='--o', alpha=alpha, label=str(i), capthick=2, capsize=5)
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
