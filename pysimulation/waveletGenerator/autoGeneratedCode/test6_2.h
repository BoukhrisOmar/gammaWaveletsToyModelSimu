#ifndef TEST6_2_HPP
#define TEST6_2_HPP
#include "PAbstractWavelet.h"
#include "thresholdComputation.h"
///@brief Implementation of PAbstractWavelet as Test6_2
class Test6_2 : public PAbstractWavelet {
	public :
		Test6_2 () ;
		virtual  ~Test6_2 () ;
		void greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
		void greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
	protected :
		void initialisationWavelet() ;
} ;
#endif
