/***************************************
	Auteur : Pierre Aubert
	Mail : aubertp7@gmail.com
	Licence : CeCILL-C
****************************************/


#include "PAbstractWavelet.h"

using namespace std ;

///Default constructeur of PAbstractWavelet
PAbstractWavelet::PAbstractWavelet(){
	initialisationPAbstractWavelet();
	initialisationWavelet();
}

///Destructeur of PAbstractWavelet
PAbstractWavelet::~PAbstractWavelet(){
	/*
	if(p_matWavelet != NULL){
		delete [] p_matWavelet;
	}
	if(p_matPatch != NULL){
		delete [] p_matPatch;
	}
	//*/
}

///Init the wavelet matrix
void PAbstractWavelet::initialisationWavelet(){

}

///set the considered pixel threshold for tailcut cleaning
/**	@param thresholdCenter : considered pixel threshold for tailcut cleaning
*/
void PAbstractWavelet::setThresholdCenter (float thresholdCenter){
	p_thresholdCenter = thresholdCenter;
}

///set the considered pixel neigbour threshold for tailcut cleaning
/**	@param thresholdNeigbour : considered pixel neigbour threshold for tailcut cleaning
*/
void PAbstractWavelet::setThresholdNeigbour (float thresholdNeigbour){
	p_thresholdNeigbour = thresholdNeigbour;
}

///set the considered pixel wavelet threshold
/**	@param thresholdWavelet : considered pixel wavelet threshold
*/
void PAbstractWavelet::setThresholdWavelet (float thresholdWavelet){
	p_thresholdWavelet = thresholdWavelet;
}

///Alocate the wavelet and patch matrix
/**	@param nbRow : number of matrix rows
 * 	@param nbCol : number of matrix column
*/
void PAbstractWavelet::createMatrix(size_t nbRow, size_t nbCol){
	p_nbRow = nbRow;
	p_nbCol = nbCol;
	p_matPatch = vector<float>(2*nbRow*nbCol) ;//new unsigned int[nbRow*nbCol];
	p_matWavelet = vector<float>(nbRow*nbCol) ;//new float[nbRow*nbCol];
}

///Set the wavelet pace
/**	@param pace : wavelet pace
*/
void PAbstractWavelet::setPace (unsigned int pace){
	p_pace = pace;
}

///Get the considered pixel threshold for tailcut cleaning
/**	@return considered pixel threshold for tailcut cleaning
*/
float PAbstractWavelet::getThresholdCenter(){
	return p_thresholdCenter;
}

///Get the considered pixel neigbour threshold for tailcut cleaning
/**	@return considered pixel neigbour threshold for tailcut cleaning
*/
float PAbstractWavelet::getThresholdNeigbour(){
	return p_thresholdNeigbour;
}


///Get the considered pixel wavelet threshold
/**	@return considered pixel wavelet threshold
*/
float PAbstractWavelet::getThresholdWavelet(){
	return p_thresholdWavelet;
}

///Get the matrix number of rows
/**	@return matrix number of rows
*/
size_t PAbstractWavelet::getNbRow(){
	return p_nbRow;
}

///Get the matrix number of cols
/**	@return matrix number of cols
*/
size_t PAbstractWavelet::getNbCol(){
	return p_nbCol;
}

///Get the wavelet matrix
/**	@return wavelet matrix
*/
std::vector<float> & PAbstractWavelet::getMatWavelet(){
	return p_matWavelet;
}

///Get the wavelet matrix pitch
/**	@return wavelet matrix pitch
*/
size_t PAbstractWavelet::getMatWaveletPitch(){
	return p_matWaveletPitch;
}

///Get the patch matrix
/**	@return patch matrix
*/
vector<float> PAbstractWavelet::getMatPatch(){
	return p_matPatch;
}

///Get the patch matrix pitch
/**	@return patch matrix pitch
*/
size_t PAbstractWavelet::getMatPatchPitch(){
	return p_matPatchPitch;
}

///Get the wavelet pace
/**	@return wavelet pace
*/
unsigned int PAbstractWavelet::getPace(){
	return p_pace;
}

///Basic cleaning
/**	@param keepSignalRectOut : true if we keep the signal in the telescope, false if we drop it
 * 	@param signalRectIn : signal in the telescope we want to clean, Must be in the convolution format pixel
 * 	@param nbRow : number of row in the matrix
 * 	@param nbCol : number of columns in the matrix
*/
void PAbstractWavelet::cleaning(std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol){
	float c;
	int shift_x, shift_y;
	for (size_t i(0lu); i < nbRow/p_nbRow; i++){
		for (size_t j(0lu); j < nbCol/p_nbCol; j++){
			c = 0.0f;
			for (size_t k(0lu); k < p_nbCol*p_nbRow; k++){
				shift_x = (p_pace*i + p_matPatch[k<<1]);
				shift_y = (p_pace*j + p_matPatch[(k<<1)+1]);
				c += signalRectIn[shift_x*nbCol + shift_y] * p_matWavelet[k];
			}
			for (size_t k(0lu); k < p_nbCol*p_nbRow ; k++) {
				shift_x = (p_pace*i + p_matPatch[k<<1]);
				shift_y = (p_pace*j + p_matPatch[(k<<1)+1]);
				keepSignalRectOut[shift_x*nbCol + shift_y] = (c > p_thresholdWavelet) ? 1.0f : 0.0f;
			}
		}
	}
	for (size_t i(0lu); i < nbRow*nbCol; i++){
		if (keepSignalRectOut[i] != 0.0f)
				keepSignalRectOut[i] = signalRectIn[i] ;
	}
}
///Greedy cleaning
/**	@param keepSignalRectOut : true if we keep the signal in the telescope, false if we drop it
 * 	@param signalRectIn : signal in the telescope we want to clean, Must be in the convolution format pixel
 * 	@param nbRow : number of row in the matrix
 * 	@param nbCol : number of columns in the matrix
*/
void PAbstractWavelet::greedyCleaning(std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol){
	float c;
	int shift_x, shift_y;
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1; j++){
			c = 0.0f;
			for (size_t k(0lu); k < p_nbCol*p_nbRow; k++){
				shift_x = (i + p_matPatch[k<<1]);
				shift_y = (j + p_matPatch[(k<<1)+1]);
				c += signalRectIn[shift_x*nbCol + shift_y] * p_matWavelet[k];
			}
			keepSignalRectOut[i*nbCol + j] = (c > p_thresholdWavelet) ? 1.0f : 0.0f;
		}
	}
	//reconstructing image
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1 ; j++) {
			if (keepSignalRectOut[i*nbCol+j] != 0.0f)
					keepSignalRectOut[i*nbCol+j] = signalRectIn[i*nbCol+j] ;
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
///Greedy cleaning that keeps neighbours surrounding signal
/**	@param keepSignalRectOut : true if we keep the signal in the telescope, false if we drop it
 * 	@param signalRectIn : signal in the telescope we want to clean, Must be in the convolution format pixel
 * 	@param nbRow : number of row in the matrix
 * 	@param nbCol : number of columns in the matrix
*/
void PAbstractWavelet::greedyCleaningWithNeighbours(std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol){
	float c;
	int shift_x, shift_y;
	//* cleaning loop
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1; j++){
			c = 0.0f;
			for (size_t k(0lu); k < p_nbCol*p_nbRow; k++){
				shift_x = (i + p_matPatch[k<<1]);
				shift_y = (j + p_matPatch[(k<<1)+1]);
				c += signalRectIn[shift_x*nbCol + shift_y] * p_matWavelet[k];
			}
			keepSignalRectOut[i*nbCol + j] = (c > p_thresholdWavelet) ? 1.0f : 0.0f;
		}
	} //*/
	//* Neighbours activation
	std::vector<float> res = keepSignalRectOut ;
	float my_bool ;
	for(size_t i(1lu); i < nbRow - 1lu; ++i){
		for(size_t j(1lu); j < nbCol - 1lu; ++j){
			my_bool = (keepSignalRectOut[i*nbCol + j] != 0.0f) ;
			res[(i-1)*nbCol + j] = my_bool ;
			res[(i-1)*nbCol + j-1] = my_bool ;
			res[(i)*nbCol + j-1] = my_bool ;
			res[(i+1)*nbCol + j] = my_bool ;
			res[(i+1)*nbCol + j+1] = my_bool ;
			res[(i)*nbCol + j+1] = my_bool ;
		}
	} //*/
	//reconstructing image
	for (size_t i(1lu); i < nbRow-1; i++){
		for (size_t j(1lu); j < nbCol-1 ; j++) {
			if (keepSignalRectOut[i*nbCol+j] != 0.0f || res[i*nbCol+j] != 0.0f)
					keepSignalRectOut[i*nbCol+j] = signalRectIn[i*nbCol+j] ;
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

///Default init of PAbstractWavelet
void PAbstractWavelet::initialisationPAbstractWavelet(){
	p_thresholdCenter = 0.0f;
	p_thresholdNeigbour = 0.0f;
	p_thresholdWavelet = 0.0f;
	p_nbRow = 0lu;
	p_nbCol = 0lu;
	p_matWavelet = vector<float>();
	p_matWaveletPitch = 0lu;
	p_matPatch = vector<float>();
	p_matPatchPitch = 0lu;
	p_pace = 0lu;
}
