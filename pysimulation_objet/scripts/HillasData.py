
import scripts.MatrixFileSystem as MatrixFileSystem
import scripts.HillasValidation as HillasValidation
import scripts.MyProgressBar as MyProgressBar
import scripts.ErrorCalc as ErrorCalc
from math import pi

def fmod (x, y) :
    while x <= -y : x += y
    while x >= y : x -= y
    return x


class HillasData (HillasValidation.HillasValidation) :

    def __init__ (self, wavelet_name, nbEvent, fact, cam_name, im_folder, sig_folder) :
        super().__init__ (wavelet_name, fact, cam_name, im_folder, sig_folder)
        self.eps_calc = ErrorCalc.ErrorCalc (wavelet_name, nbEvent, fact, cam_name, im_folder, sig_folder)
        self.t = []
        self.fact = fact
        self.path = "validation_data/" + cam_name + "/" + wavelet_name + "/rapport" + str(self.fact)
        self.cen_x_tab = []
        self.cen_y_tab = []
        self.length_tab = []
        self.width_tab = []
        self.psi_tab = []
        self.phi_tab = []
        self.skewness_tab = []
        self.kurtosis_tab = []
        self.__load_data (nbEvent)
        self.__do_calc (nbEvent)

    def __load_data (self, nbEvent) :
        print ("Loading data ...")
        self.progbar = MyProgressBar.MyProgressBar(nbEvent, 100)
        for i in range (nbEvent) :
            self.load_data(i)
            self.t.append(self.save_data())
            self.progbar.update()
        print ("")

    def __do_calc (self, nbEvent) :
        print ("Calculation in progress ...")
        self.progbar = MyProgressBar.MyProgressBar(nbEvent, 100)
        for el in self.t :
            self.cen_x_tab.append((el[0].cen_x-el[1].cen_x) if el[1].cen_x < 0.01 else (el[0].cen_x/el[1].cen_x*1.0 - 1))
            self.cen_y_tab.append((el[0].cen_y-el[1].cen_y) if el[1].cen_y < 0.01 else (el[0].cen_y/el[1].cen_y*1.0 - 1))
            self.length_tab.append((el[0].length-el[1].length) if el[1].length < 0.01 else (el[0].length/el[1].length*1.0 - 1))
            self.width_tab.append((el[0].width-el[1].width) if el[1].width < 0.01 else (el[0].width/el[1].width*1.0 - 1))
            psi_0, psi_1 = fmod(float(str(el[0].psi)[:-3]), pi/2), fmod(float(str(el[1].psi)[:-3]), pi/2)
            phi_0, phi_1 = fmod(float(str(el[0].phi)[:-3]), pi/2), fmod(float(str(el[1].phi)[:-3]), pi/2)
            psi, phi = 0.0, 0.0
            if psi_1 < 0.1 : psi = psi_0 - psi_1 if psi_0 - psi_1 < psi_1 - psi_0 else psi_1 - psi_0
            else : psi = psi_0/psi_1 - 1
            if phi_1 < 0.1 : phi = phi_0 - phi_1 if phi_0 - phi_1 < phi_1 - phi_0 else phi_1 - phi_0
            else : phi = phi_0/phi_1 - 1
            self.psi_tab.append(psi)
            self.phi_tab.append(phi)
            self.skewness_tab.append((el[0].skewness-el[1].skewness) if el[1].skewness < 0.01 else (el[0].skewness/el[1].skewness*1.0 - 1))
            self.kurtosis_tab.append((el[0].kurtosis-el[1].kurtosis) if el[1].kurtosis < 0.01 else (el[0].kurtosis/el[1].kurtosis*1.0 - 1))
            self.progbar.update()
        print ("")

    def save_cen_x (self) :
        cen_x_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        cen_x_mfs.store_rapport(self.cen_x_tab, "cen_x")
    def save_cen_y (self) :
        cen_y_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        cen_y_mfs.store_rapport(self.cen_y_tab, "cen_y")

    def save_length (self) :
        length_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        length_mfs.store_rapport(self.length_tab, "length")
    def save_width (self) :
        width_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        width_mfs.store_rapport(self.width_tab, "width")

    def save_psi (self) :
        psi_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        psi_mfs.store_rapport(self.psi_tab, "psi")
    def save_phi (self) :
        phi_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        phi_mfs.store_rapport(self.phi_tab, "phi")

    def save_skewness (self) :
        skewness_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        skewness_mfs.store_rapport(self.skewness_tab, "skewness")
    def save_kurtosis (self) :
        kurtosis_mfs = MatrixFileSystem.MatrixFileSystem(self.path)
        kurtosis_mfs.store_rapport(self.kurtosis_tab, "kurtosis")

    def save_eps_shape (self) :
        eps_mfs = MatrixFileSystem.MatrixFileSystem (self.path)
        eps_mfs.store_rapport(self.eps_calc.get_shape_err (), "eps_shape")
    def save_eps_intensity (self) :
        eps_mfs = MatrixFileSystem.MatrixFileSystem (self.path)
        eps_mfs.store_rapport(self.eps_calc.get_intensity_err (), "eps_intensity")



    def save_all(self) :
        print ("Storing data in progress...")
        self.progbar = MyProgressBar.MyProgressBar(10, 100)
        self.save_cen_x ()
        self.progbar.update()
        self.save_cen_y ()
        self.progbar.update()
        self.save_length ()
        self.progbar.update()
        self.save_width ()
        self.progbar.update()
        self.save_psi ()
        self.progbar.update()
        self.save_phi ()
        self.progbar.update()
        self.save_skewness ()
        self.progbar.update()
        self.save_kurtosis ()
        self.progbar.update()
        #self.save_eps_shape ()
        self.progbar.update()
        #self.save_eps_intensity ()
        self.progbar.update()
        print ("")
