class WaveletGenerator:
  def __init__ (self, name)
  def get_param_from_file (self)
  def get_hpp (self)
  def get_cpp (self)
  def __get_cleaning_mask
  def __get_neighbours_activation
  def __get_image_reco (self, neighbours=True)
  def __get_edge_cutting (self)
  def write_sourceCode_to_file (self)

class FactoryGenerator:
  def __init__ (self, my_wavelets)
  def build_hpp_factory (self) :
  def build_cpp_factory (self)
  def write_sourceCode_to_file (self)

class CompilingScript :
  def __init__ (self, wavelist)
  def __getCompilingScript (self)
  def writeCompilingScript (self)
