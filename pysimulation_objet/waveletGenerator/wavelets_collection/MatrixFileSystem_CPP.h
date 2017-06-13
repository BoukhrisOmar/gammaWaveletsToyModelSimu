#ifndef MATRIXFILESYSTEM_CPP_HPP
#define MATRIXFILESYSTEM_CPP_HPP

#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cmath>

#include <algorithm>

typedef std::vector<std::vector<float> >  mat;
typedef std::vector<float> vect;

class MatrixFileSystem_CPP {
  public:
    MatrixFileSystem_CPP(const std::string & path, const int & nEvent) ;

    void load_mat () ;
    void store_mat () ;
    void store_mat (const std::string & path) ;

    void set_nbcol (int col) ;
    void set_nbrow (int row)  ;
    int get_nbcol () ;
    int get_nbrow () ;

    vect get_signal_matrix () ;
    void set_signal_matrix (const vect & m) ;
    float get_threshold () ;

    ~MatrixFileSystem_CPP() ;

  private:
    std::string path ;
    int nEvent ;
    float mat_thr ;
    int nbcol, nbrow ;
    mat m ;

    vect vect_m ;

    vect split2float(std::string str, char delimiter) ;
} ;

#endif
