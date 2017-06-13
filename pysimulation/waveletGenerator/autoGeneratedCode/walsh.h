#ifndef WALSH_HPP
#define WALSH_HPP
#include "PAbstractWavelet.h"
#include "thresholdComputation.h"
///@brief Implementation of PAbstractWavelet as Walsh
class Walsh : public PAbstractWavelet {
	public :
		Walsh () ;
		virtual  ~Walsh () ;
		void greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
		void greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
	protected :
		void initialisationWavelet() ;
} ;
#endif
