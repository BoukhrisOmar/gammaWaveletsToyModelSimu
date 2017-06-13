//#include "WaveletsLib.hpp"
#include "MatrixFileSystem_CPP.h"
#include "thresholdComputation.h"
#include "waveletsFactory.h"

using namespace std ;

/*
Usage :
./prog  nbEvent path tel_id wavelet_name
  nbEvent : event number in telescope
  path : relative path to events folder (data in general)
  tel_id : telescope id
  wavelet_name : wavelet used to denoise

input  found in : [path]/raw_txt/telescope_[tel_id]/event[nbEvent].txt2d
output found in : [path]/cppCleaned/telescope_[tel_id]/event[nbEvent].txt2d
output is a 2D python matrix
*/

int main (int argc, char *argv[]) {
  //*
  if (argc != 5) {
    cout << "Usage :" << endl ;
    cout << "\t./prog --[nei|not] nbEvent wavelet_name path" << endl ;
    cout << "\t\t--nei|notnei : to choose between keeping neighbours or ditching 'em" << endl ;
    cout << "\t\tnbEvent : event number in telescope" << endl ;
    cout << "\t\twavelet_name : cleaning type to use" << endl ;
    cout << "\t\tpath : path to stored lists" << endl ;
    return 0 ;
  }
  bool nei = (string(argv[1]) == "--nei") ;
  int event = stoi (string(argv[2])) ;
  string wavelet_name = string(argv[3]) ;
  string path = string(argv[4]) ;
  //*/

  MatrixFileSystem_CPP mfs = MatrixFileSystem_CPP(path, event) ;
  mfs.load_mat() ;
  vect mySignalMatrix = mfs.get_signal_matrix() ;
  vect m_cpy = mySignalMatrix ;

  //* setting up the denoising wavelet
  PAbstractWavelet* my_wave = WaveletsFactory().getWaveletByName(wavelet_name) ;
  float threshold = get_threshold(mySignalMatrix, mfs.get_nbrow(), mfs.get_nbcol()) ;
  //float threshold = mfs.get_threshold () ;
  if (wavelet_name == "tailcut") {
    my_wave->setThresholdCenter (threshold) ;
    my_wave->setThresholdNeigbour (threshold*0.75f) ;
  } else {
    my_wave->setThresholdWavelet (threshold) ;
  }
  //applying the cleaning : always the greedy one, unless specifically asked to use standard wavelet denoising
  //in which case, call "cleaning" method with same parameters
  if (nei) {
    my_wave->greedyCleaningWithNeighbours(m_cpy, mySignalMatrix, (size_t) mfs.get_nbrow(), (size_t) mfs.get_nbcol()) ;
    wavelet_name += "_nei" ;
  } else {
    my_wave->greedyCleaning(m_cpy, mySignalMatrix, (size_t) mfs.get_nbrow(), (size_t) mfs.get_nbcol()) ;
  }
  //* saving the result matrix in file
  mfs.set_signal_matrix(m_cpy) ;
  mfs.store_mat (path + "/" + wavelet_name + "/cleaned_telescope") ;
  //*/
  return 0 ;
}
