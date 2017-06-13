#ifndef TAILCUT_HPP
#define TAILCUT_HPP
#include "PAbstractWavelet.h"
#include "thresholdComputation.h"
///@brief Implementation of PAbstractWavelet as Tailcut
class Tailcut : public PAbstractWavelet {
	public :
		Tailcut () ;
		virtual  ~Tailcut () ;
		virtual void greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
		virtual void greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
	protected :
		void initialisationWavelet() ;
} ;
#endif
