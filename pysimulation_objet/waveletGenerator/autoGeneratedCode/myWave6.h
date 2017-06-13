#ifndef MYWAVE6_HPP
#define MYWAVE6_HPP
#include "PAbstractWavelet.h"
#include "thresholdComputation.h"
///@brief Implementation of PAbstractWavelet as Mywave6
class Mywave6 : public PAbstractWavelet {
	public :
		Mywave6 () ;
		virtual  ~Mywave6 () ;
		void greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
		void greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
	protected :
		void initialisationWavelet() ;
} ;
#endif
