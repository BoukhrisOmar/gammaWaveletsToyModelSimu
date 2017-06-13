class DiffHillasPlotter :
  def __init__ (self, wave_list, fact, cam_name)
  def get_cen_x (self)
  def get_cen_y (self)
  def get_length (self)
  def get_width (self)
  def get_psi (self)
  def get_phi (self)
  def get_skewness (self)
  def get_kurtosis (self)
  def print_eps (self)
  def plot_all (self)

class ErrorCalc(Transforms)
  def __init__ (self, wavelet_name, nbEvent, fact, cam_name, im_folder, sig_folder)
  def get_shape_err (self)
  def get_intensity_err (self)

class HillasData (HillasValidation.HillasValidation)
  def __init__ (self, wavelet_name, nbEvent, fact, cam_name, im_folder, sig_folder)
  def __load_data (self, nbEvent)
  def __do_calc (self, nbEvent)
  def save_cen_x (self)
  def save_cen_y (self)
  def save_length (self)
  def save_width (self)
  def save_psi (self)
  def save_phi (self)
  def save_skewness (self)
  def save_kurtosis (self)
  def save_eps_shape (self)
  def save_eps_intensity (self)
  def save_all(self)

class HillasPlotter :
  def __init__ (self, cam_name, wavelet_name, list_fact)
  def get_cen_x (self)
  def get_cen_y (self)
  def get_length (self)
  def get_width (self)
  def get_psi (self)
  def get_phi (self)
  def get_skewness (self)
  def get_kurtosis (self)
  def plot_all (self)

class HillasValidation (Transforms.Transforms):
  def __init__ (self, wavelet_name, fact, cam_name, dir_clean="data/im", dir_sim="data/sig")
  def load_data (self, nEvent)
  def save_data (self)

class MatrixFileSystem :
  def __init__ (self, dir)
  def ensure_path (self, direc)
  def read_matrix (self, nEvent)
  def save_text2bin (self, nEvent)
  def store_cpp_mat (self, mat, id, thr)
  def read_vect (self, nEvent)
  def store_vect (self, vect, id)
  def store_rapport (self, vect, fname)
  def load_rapport (self, param_name)

class MyProgressBar :
  def __init__ (self, nb_element=100, width=100)
  def update (self)

class PlotHillasParamErr :
  def __init__ (self, wave_list, fact_list, cam_name)
  def get_cen_x (self)
  def get_cen_y (self)
  def get_length (self)
  def get_width (self)
  def get_psi (self)
  def get_phi (self)
  def get_skewness (self)
  def get_kurtosis (self)
  def plot_all (self)

class Plotter :
  def __init__ (self, wavelet_name, nbEvent, fact, cam_name)
  def subplot_raw (self)
  def subplot_clean (self)
  def subplot_sig (self)
  def plot_all (self)

class PyGammaSimulation (Transforms) :
  def __init__ (self, nTel=0, centroid=(-0.5, 0.5), length=(0.005, 0.09), width=(0.0005, 0.003), psi=(0, 360), nsb=(10, 60))
  def generate_signal (self, sn=1, threshold=0.05)
  def get_camera_geometry(self, pixel_area=3., pixel_type='hexagonal')

class Transforms :
  def __init__ (self, nTel)
  def load_telescope (self)
  def sig2matrix (self, sig)
  def matrix2sig (self, mat)
