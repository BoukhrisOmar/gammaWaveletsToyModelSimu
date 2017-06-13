#ifndef WAVELETS_FACTORY_HPP
#define WAVELETS_FACTORY_HPP
#include "myWave6.h"
#include "test6.h"
#include "walsh.h"
#include "test6_2.h"
#include "tailcut.h"
class WaveletsFactory {
	public :
		WaveletsFactory() ;
		PAbstractWavelet* getWaveletByName (std::string name) ;
	private :
		Mywave6* myWave6_wavelet ;
		Test6* test6_wavelet ;
		Walsh* walsh_wavelet ;
		Test6_2* test6_2_wavelet ;
		Tailcut* tailcutObj ;
} ;
#endif
