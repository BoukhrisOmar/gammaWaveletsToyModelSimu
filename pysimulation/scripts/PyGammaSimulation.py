
from scripts.Transforms import *

"""
randomly generates gamma showers
ex :
py_gamma_sim = PyGammaSimulation()
(image, signal, noise) = py_gamma_sim.generate_signal()

def __init__ (self, nTel=0, centroid=(-0.5, 0.5), length=(0.005, 0.01), width=(0.0005, 0.003), psi=(0, 360), nsb=(12, 25)) :
def generate_signal (self, sn=1, threshold=0.3) :
def get_camera_geometry(tel, pixel_area=3., pixel_type='hexagonal'):
"""
class PyGammaSimulation (Transforms) :

    def __init__ (self, nTel=0, centroid=(-0.5, 0.5), length=(0.005, 0.09), width=(0.0005, 0.003), psi=(0, 360), nsb=(10, 60)) :
        """
        nTel=0
        centroid=(-0.5, 0.5)
        length=(0.005, 0.05)
        width=(0.0005, 0.003)
        psi=(0, 360)
        nsb=(12, 25)
        """
        super().__init__ (nTel)
        self.centroid =  [centroid, centroid]
        self.length, self.width = length,  width
        self.psi = psi
        self.nsb = nsb
        self.tab_inj, self.mat_event, self.geom = None, None, None
        self.load_telescope()

    def generate_signal (self, sn=1, threshold=0.05) :
        """
        sn : signal/noise factor
        threshold : for sn values

        RM : intensity always @ 3 (change... or not)
        """
        self.geom = self.get_camera_geometry()
        while True :
            centroid =  [random.uniform(self.centroid[0][0], self.centroid[0][1]), random.uniform(self.centroid[1][0], self.centroid[1][1])]
            length, width = random.uniform(self.length[0], self.length[1]),  random.uniform(self.width[0], self.width[1])
            psi = str(random.randint(self.psi[0], self.psi[1])) + "d"
            nsb = random.randint(self.nsb[0], self.nsb[1])
            #nsb = random.randint(int(self.nsb[0]*(1-sn**2)), int(self.nsb[1]*(1-sn**2)))

            showermodel = toy.generate_2d_shower_model(centroid=centroid, length=length,width=width, psi=psi)
            image, signal, noise = toy.make_toymodel_shower_image(self.geom, showermodel.pdf, intensity=int(3*(1+sn**2)), nsb_level_pe=nsb)
            ks = []
            for s in signal :
                if s != 0. :
                    ks.append(s)
            ks = np.array(ks)
            noise = np.array(noise)
            k = ks.mean()/noise.mean()
            #print (k)
            if k >= sn-threshold and k <= sn+threshold :
                return (image, signal, noise)

    def get_camera_geometry(self, pixel_area=3., pixel_type='hexagonal'):
        """
        Parameters
        ----------
        tel: PRun.PTelescope or PCalibRun.PCalibTel
        pixel_area: array(float)
            surface area of each pixel
        pix_type: string
            either 'rectangular' or 'hexagonal'
        Returns:
        --------
        CameraGeometry
        """
        tab_xy = self.nTel.getTabPos().getTabPixelPosXY()
        nb_pixel = int(len(tab_xy) / 2)
        pix_x = plibs_8.array(np.array([tab_xy[i] for i in range(tab_xy.shape[0]) if i % 2 == 0]))
        pix_y = plibs_8.array(np.array([tab_xy[i] for i in range(tab_xy.shape[0]) if i % 2 == 1]))
        pix_x = pix_x * u.meter
        pix_y = pix_y * u.meter
        pix_id = np.arange(1,nb_pixel+1)
        pix_area = np.full(nb_pixel, pixel_area/1000, dtype=np.float32)
        geom = CameraGeometry(self.nTel.getTelescopeId(), pix_id, pix_x, pix_y, pix_area, pixel_type)
        return geom
