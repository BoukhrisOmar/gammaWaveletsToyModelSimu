#include "waveletsFactory.h"
WaveletsFactory::WaveletsFactory () {
	myWave6_wavelet = new Mywave6() ;
	test6_wavelet = new Test6() ;
	walsh_wavelet = new Walsh() ;
	test6_2_wavelet = new Test6_2() ;
	tailcutObj = new Tailcut() ;
}
PAbstractWavelet* WaveletsFactory::getWaveletByName(std::string name) {
	if (name == "myWave6") return myWave6_wavelet ;
	if (name == "test6") return test6_wavelet ;
	if (name == "walsh") return walsh_wavelet ;
	if (name == "test6_2") return test6_2_wavelet ;
	else return tailcutObj ;
}
