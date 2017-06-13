/***************************************
	Auteur : Pierre Aubert
	Mail : aubertp7@gmail.com
	Licence : CeCILL-C
****************************************/


#include "thresholdComputation.h"

using namespace std ;

float get_mu (const vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
  return get_sum(signalRectIn, nbRow, nbCol)/(float)(nbRow*nbCol) ;
}

float get_sigma (const vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
  float s = 0.0f, si = 0.0f ;
  float mu = get_mu(signalRectIn, nbRow, nbCol) ;
  for (size_t i(0lu) ; i < nbRow ; i++) {
    for (size_t j(0lu) ; j < nbCol ; j++) {
      //if (signalRectIn[i*nbCol + j] == 0.) continue ;
      si = (signalRectIn[i*nbCol + j] - mu) ;
      s += si*si ;
    }
  }
  return sqrt((1.0/(float)nbRow*nbCol)*s) ;
}

float get_sum (const vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
  float s = 0.0f ;
  for (size_t i(0lu) ; i < nbRow ; i++) {
    for (size_t j(0lu) ; j < nbCol ; j++) {
      //if (signalRectIn[i*nbCol + j] == 0.) continue ;
      s += signalRectIn[i*nbCol + j] ;
    }
  }
  return s ;
}

float get_threshold (const vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
  float
    sum = 0.0f,
    sigm = 0.0f ;
  for (size_t i(0lu) ; i < nbRow ; i++) {
    for (size_t j(0lu) ; j < nbCol ; j++) {
      float c = signalRectIn[i*nbCol + j] ;
      sum += c ;
    }
  }
  size_t matSize = nbRow*nbCol ;
  float mu = sum/(matSize) ;
  for (size_t i(0lu) ; i < nbRow ; i++) {
    for (size_t j(0lu) ; j < nbCol ; j++) {
      float c = signalRectIn[i*nbCol + j] ;
      sigm += (c - mu)*(c - mu) ;
    }
  }
  sigm = sqrt((sigm/matSize) - mu*mu) ;
  return
    sqrt(2 * log2(sum)) * sigm + mu ;
}
