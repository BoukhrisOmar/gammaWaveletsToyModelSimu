#include "test6_2.h"
#include <string.h>
///Constructeur de la classe
/**	@param signalRectIn : signal to clean
 * 	@param nbRow : row numbers
 * 	@param nbRow : column numbers
*/
Test6_2::Test6_2()
: PAbstractWavelet() {
	initialisationWavelet() ;
}

///Destructeur par défaut
Test6_2::~Test6_2() {}

///Initialisation des paramètres d'ondelette
void Test6_2::initialisationWavelet (){
	createMatrix(2, 2) ;
	p_matWavelet = {0.4, 0.26666666666666666, 0.26666666666666666, 0.26666666666666666, 0.0, 0.26666666666666666, 0.26666666666666666, 0.26666666666666666, 0.0} ;
	p_matPatch = {0, 0, 0, 1, 1, 0, 1, 1, 1, -1, 0, -1, -1, -1, -1, 0, -1, 1} ;
	p_pace = 1 ;
}

///Greedy wavelet cleaning with neighbours surrounding signal
void Test6_2::greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
	//getting the mask
	std::vector<float> res = std::vector<float>(nbRow*nbCol, 0.0f) ;
	for (size_t i (1lu) ; i < nbRow -1 ; i++) {
		for (size_t j (1lu) ; j < nbCol -1 ; j++) {
			float c = 0.0f ;
			c += (0.4* signalRectIn[(i)*nbCol + (j)]) ;
			c += (0.26666666666666666* signalRectIn[(i)*nbCol + (j+1)]) ;
			c += (0.26666666666666666* signalRectIn[(i+1)*nbCol + (j)]) ;
			c += (0.26666666666666666* signalRectIn[(i+1)*nbCol + (j+1)]) ;
			c += (0.26666666666666666* signalRectIn[(i)*nbCol + (j-1)]) ;
			c += (0.26666666666666666* signalRectIn[(i-1)*nbCol + (j-1)]) ;
			c += (0.26666666666666666* signalRectIn[(i-1)*nbCol + (j)]) ;
			float my_bool = (c >= p_thresholdWavelet) ;
			res[(i-1)*nbCol + j] = my_bool || res[(i-1)*nbCol + j] ;
			res[(i-1)*nbCol + j-1] = my_bool || res[(i-1)*nbCol + j-1] ;
			res[(i)*nbCol + j-1] = my_bool || res[(i)*nbCol + j-1] ;
			res[(i)*nbCol + j] = my_bool || res[(i)*nbCol + j] ;
			res[(i+1)*nbCol + j] = my_bool || res[(i+1)*nbCol + j] ;
			res[(i+1)*nbCol + j+1] = my_bool || res[(i+1)*nbCol + j+1] ;
			res[(i)*nbCol + j+1] = my_bool || res[(i)*nbCol + j+1] ;
		}
	}
	keepSignalRectOut = res ;
	//reconstructing image
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1 ; j++) {
			if (keepSignalRectOut[i*nbCol+j] != 0.0f)
					keepSignalRectOut[i*nbCol+j] = fabs(signalRectIn[i*nbCol+j]) ;
		}
	}
	//cutting edges .. :p
	for (size_t i(0lu); i < nbRow ; i++) {
		keepSignalRectOut[i*nbCol] = 0. ;
		keepSignalRectOut[i*nbCol+nbCol-1] = 0. ;
	}
	for (size_t i(0lu); i < nbCol ; i++) {
		keepSignalRectOut[i] = 0. ;
		keepSignalRectOut[(nbRow-1)*nbCol+i] = 0. ;
	}
}

///Greedy wavelet cleaning without neighbours surrounding signal
void Test6_2::greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
	//getting the mask
	std::vector<float> res = std::vector<float>(nbRow*nbCol, 0.0f) ;
	for (size_t i (1lu) ; i < nbRow -1 ; i++) {
		for (size_t j (1lu) ; j < nbCol -1 ; j++) {
			float c = 0.0f ;
			c += (0.4* signalRectIn[(i)*nbCol + (j)]) ;
			c += (0.26666666666666666* signalRectIn[(i)*nbCol + (j+1)]) ;
			c += (0.26666666666666666* signalRectIn[(i+1)*nbCol + (j)]) ;
			c += (0.26666666666666666* signalRectIn[(i+1)*nbCol + (j+1)]) ;
			c += (0.26666666666666666* signalRectIn[(i)*nbCol + (j-1)]) ;
			c += (0.26666666666666666* signalRectIn[(i-1)*nbCol + (j-1)]) ;
			c += (0.26666666666666666* signalRectIn[(i-1)*nbCol + (j)]) ;
			keepSignalRectOut[i*nbCol+j] = (c >= p_thresholdWavelet) ;
		}
	}
	//reconstructing image
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1 ; j++) {
			if (keepSignalRectOut[i*nbCol+j] != 0.0f)
					keepSignalRectOut[i*nbCol+j] = fabs(signalRectIn[i*nbCol+j]) ;
		}
	}
	//cutting edges .. :p
	for (size_t i(0lu); i < nbRow ; i++) {
		keepSignalRectOut[i*nbCol] = 0. ;
		keepSignalRectOut[i*nbCol+nbCol-1] = 0. ;
	}
	for (size_t i(0lu); i < nbCol ; i++) {
		keepSignalRectOut[i] = 0. ;
		keepSignalRectOut[(nbRow-1)*nbCol+i] = 0. ;
	}
}
