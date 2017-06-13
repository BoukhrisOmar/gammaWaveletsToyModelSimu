/***************************************
	Auteur : Pierre Aubert
	Mail : aubertp7@gmail.com
	Licence : CeCILL-C
****************************************/

#ifndef __THRESHOLDCOMPUTATION_H__
#define __THRESHOLDCOMPUTATION_H__

#include <math.h>
#include <stdio.h>
#include <iostream>
#include <vector>

float get_mu (const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
float get_sigma (const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
float get_sum (const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;
float get_threshold (const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;

#endif
