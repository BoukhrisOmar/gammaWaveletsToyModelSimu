#ifndef TEST6_HPP
#define TEST6_HPP
#include "PAbstractWavelet.h"
#include "thresholdComputation.h"
///@brief Implementation of PAbstractWavelet as Test6
class Test6 : public PAbstractWavelet {
	public :
		Test6 () ;
		virtual  ~Test6 () ;
		void greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
		void greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
	protected :
		void initialisationWavelet() ;
} ;
#endif
