#include "tailcut.h"
#include <string.h>
///Constructeur de la classe
/**	@param signalRectIn : signal to clean
 * 	@param nbRow : row numbers
 * 	@param nbRow : column numbers
*/
Tailcut::Tailcut()
: PAbstractWavelet() {
	initialisationWavelet() ;
}

///Destructeur par défaut
Tailcut::~Tailcut() {}

///Initialisation des paramètres d'ondelette
void Tailcut::initialisationWavelet (){
	;
}

void Tailcut::greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
	//* auto calc threshold
	bool cond, cond2;
	size_t shift;
	std::vector<float> res = std::vector<float> (nbRow*nbCol, 0.0f) ;
	for(size_t i(1lu); i < nbRow - 1lu; ++i){
		for(size_t j(1lu); j < nbCol - 1lu; ++j){
			shift = i*nbCol + j;
			cond = ((signalRectIn[(i)*nbCol + j] > this->p_thresholdCenter) &&
					((signalRectIn[(i-1)*nbCol + j] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i-1)*nbCol + j-1] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i)*nbCol + j-1] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i+1)*nbCol + j] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i+1)*nbCol + j+1] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i)*nbCol + j+1] >= this->p_thresholdNeigbour)));

			cond2 =	((signalRectIn[(i)*nbCol + j] >= this->p_thresholdNeigbour) &&
					((signalRectIn[(i-1)*nbCol + j] >= this->p_thresholdCenter) ||
					(signalRectIn[(i-1)*nbCol + j-1] >= this->p_thresholdCenter) ||
					(signalRectIn[(i)*nbCol + j-1] >= this->p_thresholdCenter) ||
					(signalRectIn[(i+1)*nbCol + j] >= this->p_thresholdCenter) ||
					(signalRectIn[(i+1)*nbCol + j+1] >= this->p_thresholdCenter) ||
					(signalRectIn[(i)*nbCol + j+1] >= this->p_thresholdCenter)));
			//keepSignalRectOut[i*nbCol + j] = (cond || cond2) ? signalRectIn[i*nbCol + j] : 0.0f ;
			float my_bool = (cond||cond2) ;
			res[(i)*nbCol + j] = my_bool || res[(i)*nbCol + j] ;
			res[(i-1)*nbCol + j] = my_bool || res[(i-1)*nbCol + j] ;
			res[(i-1)*nbCol + j-1] = my_bool || res[(i-1)*nbCol + j-1] ;
			res[(i)*nbCol + j-1] = my_bool || res[(i)*nbCol + j-1] ;
			res[(i+1)*nbCol + j] = my_bool || res[(i+1)*nbCol + j] ;
			res[(i+1)*nbCol + j+1] = my_bool || res[(i+1)*nbCol + j+1] ;
			res[(i)*nbCol + j+1] = my_bool || res[(i)*nbCol + j+1] ;
		}
	}
	keepSignalRectOut = res ;
	//* image reconstruction from mask
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1 ; j++) {
			if (keepSignalRectOut[i*nbCol+j] != 0.0f)
					keepSignalRectOut[i*nbCol+j] = signalRectIn[i*nbCol+j] ;
		}
	} //*/
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
void Tailcut::greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {
	//* auto calc threshold
	bool cond, cond2;
	size_t shift;
	for(size_t i(1lu); i < nbRow - 1lu; ++i){
		for(size_t j(1lu); j < nbCol - 1lu; ++j){
			shift = i*nbCol + j;
			cond = ((signalRectIn[(i)*nbCol + j] > this->p_thresholdCenter) &&
					((signalRectIn[(i-1)*nbCol + j] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i-1)*nbCol + j-1] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i)*nbCol + j-1] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i+1)*nbCol + j] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i+1)*nbCol + j+1] >= this->p_thresholdNeigbour) ||
					(signalRectIn[(i)*nbCol + j+1] >= this->p_thresholdNeigbour)));

			cond2 =	((signalRectIn[(i)*nbCol + j] >= this->p_thresholdNeigbour) &&
					((signalRectIn[(i-1)*nbCol + j] >= this->p_thresholdCenter) ||
					(signalRectIn[(i-1)*nbCol + j-1] >= this->p_thresholdCenter) ||
					(signalRectIn[(i)*nbCol + j-1] >= this->p_thresholdCenter) ||
					(signalRectIn[(i+1)*nbCol + j] >= this->p_thresholdCenter) ||
					(signalRectIn[(i+1)*nbCol + j+1] >= this->p_thresholdCenter) ||
					(signalRectIn[(i)*nbCol + j+1] >= this->p_thresholdCenter)));
			keepSignalRectOut[i*nbCol + j] = (cond || cond2) ? signalRectIn[i*nbCol + j] : 0.0f ;
		}
	}
	//* image reconstruction from mask
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1 ; j++) {
			if (keepSignalRectOut[i*nbCol+j] != 0.0f)
					keepSignalRectOut[i*nbCol+j] = signalRectIn[i*nbCol+j] ;
		}
	} //*/
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
