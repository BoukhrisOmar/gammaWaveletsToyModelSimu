#!/bin/bash
cp wavelets_collection/* ./
g++ -c myWave6.cpp walsh.cpp PAbstractWavelet.cpp tailcut.cpp waveletsFactory.cpp thresholdComputation.cpp MatrixFileSystem_CPP.cpp
g++ myWave6.o walsh.o main.cpp PAbstractWavelet.o tailcut.o waveletsFactory.o thresholdComputation.o MatrixFileSystem_CPP.o -o theCleaner -g
rm *.o
rm *.cpp
rm *.h
mv theCleaner ../
