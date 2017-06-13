#include "MatrixFileSystem_CPP.h"

/**
split str en fonction du delimiter, convertit en float et push dans un vect
return : vector<float> = vect
*/
using namespace std ;

MatrixFileSystem_CPP::MatrixFileSystem_CPP (const string & path, const int & nEvent) {
  this->path = path ;
  this->nEvent = nEvent ;
  mat_thr = 0.0 ;
}

MatrixFileSystem_CPP::~MatrixFileSystem_CPP() {;}

void MatrixFileSystem_CPP::set_nbcol (int col) {
  this->nbcol = col ;
}
void MatrixFileSystem_CPP::set_nbrow (int row) {
  this->nbrow = row ;
}
int MatrixFileSystem_CPP::get_nbcol () {
  return this->nbcol ;
}
int MatrixFileSystem_CPP::get_nbrow () {
  return this->nbrow ;
}


vect MatrixFileSystem_CPP::get_signal_matrix () {
  return this->vect_m ;
}
void MatrixFileSystem_CPP::set_signal_matrix (const vect & my_vect) {
  mat mat_sig ;
  for (int i = 0 ; i < this->nbrow ; i++) {
    vect line ;
    for (int j = 0 ; j < this->nbcol ; j++) {
      line.push_back(my_vect[i*nbcol+j]) ;
    }
    mat_sig.push_back(line) ;
  }
  this->m = mat_sig ;
}

float MatrixFileSystem_CPP::get_threshold () {
  return this->mat_thr ;
}

vect MatrixFileSystem_CPP::split2float(string str, char delimiter) {
  vect internal;
  stringstream ss(str);
  string tok;
  float temp ;
  while(getline(ss, tok, delimiter)) {
    temp = stof (tok) ;
    internal.push_back(temp);
  }
  return internal;
}

/**
Charge l'event nEvent et push dans la matrice m
mat_thr représente le seuil calculé, présent sur la première ligne de chaque fichier représentant un event
return : None
*/
void MatrixFileSystem_CPP::load_mat () {
  string
    filename (path + "/telescope/event" + to_string(nEvent) + ".tab2d"),
    line ;
  //cout << path + "/event" + to_string(nEvent) + ".txt2d" << endl ;
  vect v_line ;
  ifstream event_file (filename) ;
  this->nbrow = 0 ; this->nbcol = 0 ;
  if (event_file.is_open()) {
    /*
    getline(event_file, line) ;
    mat_thr = stof (line) ;
    //*/
    while (getline(event_file, line)) {
      v_line = this->split2float(line, ' ') ;
      vect_m.insert(vect_m.end(), v_line.begin(), v_line.end()) ;
      this->nbrow ++ ;
    }
    this->nbcol = v_line.size() ;
    event_file.close() ;
  }
}

void MatrixFileSystem_CPP::store_mat () {
  store_mat (path) ;
}

void MatrixFileSystem_CPP::store_mat (const string & path) {
  //string filename ("./data/matrices/cleaned_telescope_" + to_string(nTel) + "/event" + to_string(nEvent) + ".tab2d") ;
  string filename (path + "/event" + to_string(nEvent) + ".tab2d") ;
  ofstream clean_event_file (filename) ;
  if (clean_event_file.is_open()) {
    clean_event_file << "[" ;
    for (unsigned int i = 0 ; i < m.size() ; i++) {
      clean_event_file << "[" ;
      unsigned int j ;
      for (j = 0 ; j < m[i].size()-1 ; j++) {
        clean_event_file << m[i][j] << ", " ;
      }
      clean_event_file << m[i][j] << "]" ;
      if (i < m.size()-1) clean_event_file << ", " ;
    }
    clean_event_file << "]" ;
    clean_event_file.close();
  }
}
