/***************************************
	Auteur : Pierre Aubert
	Mail : aubertp7@gmail.com
	Licence : CeCILL-C
****************************************/

#ifndef __PABSTRACTWAVELET_H__
#define __PABSTRACTWAVELET_H__

#include <iostream>
#include "thresholdComputation.h"

///@brief Abstract wavelet cleaning class
class PAbstractWavelet{
	public:
		PAbstractWavelet();
		virtual ~PAbstractWavelet();

		virtual void cleaning(std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol);
		virtual void greedyCleaning(std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol);

		virtual void greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;

		float getThresholdCenter();
		float getThresholdNeigbour();
		float getThresholdWavelet();
		size_t getNbRow();
		size_t getNbCol();
		std::vector<float> & getMatWavelet();
		size_t getMatWaveletPitch();
		std::vector<float> getMatPatch();
		size_t getMatPatchPitch();
		unsigned int getPace();

		void setThresholdCenter (float thresholdCenter);
		void setThresholdNeigbour (float thresholdNeigbour);
		void setThresholdWavelet (float thresholdWavelet);

		void createMatrix(size_t nbRow, size_t nbCol);

		void setPace (unsigned int pace);

	protected:
		virtual void initialisationWavelet();

		///threshold of the minimal signal we want to have in the current pixel
		float p_thresholdCenter;
		///threshold of the minimal signal we want to have in a neigbours of the current pixel
		float p_thresholdNeigbour;
		///threshold of the wavelet cut
		float p_thresholdWavelet; //alpha

		///Mat wavelet and mat patch Number of rows
		size_t p_nbRow;
		///Mat wavelet and mat patch Number of cols
		size_t p_nbCol;
		///Mat of wavelet
		std::vector<float> p_matWavelet;
		///Mat of wavelet pitch
		size_t p_matWaveletPitch;
		///Mat of patch
		std::vector<float> p_matPatch;
		///Mat of patch pitch
		size_t p_matPatchPitch;
		///pace
		unsigned int p_pace;

	private:
		void initialisationPAbstractWavelet();

};



#endif
