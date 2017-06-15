import os

class WaveletGenerator:
    def __init__ (self, name) :
        self.name = name
        self.get_param_from_file()

    def write_sourceCode_to_file (self) :
        my_hpp = open("./" + self.name + ".h", "w")
        my_hpp.write(self.get_hpp())
        my_hpp.close()
        my_cpp = open("./" + self.name + ".cpp", "w")
        my_cpp.write(self.get_cpp())
        my_cpp.close()

    def get_hpp (self) :
        hpp_src =  "#ifndef " + self.name.upper() + "_HPP\n"
        hpp_src += "#define " + self.name.upper() + "_HPP\n"
        hpp_src += "#include \"PAbstractWavelet.h\"\n"
        hpp_src += "#include \"thresholdComputation.h\"\n"
        hpp_src += "///@brief Implementation of PAbstractWavelet as " + self.name.title() + "\n"
        hpp_src += "class " + self.name.title() + " : public PAbstractWavelet {\n"
        hpp_src += "\tpublic :\n"
        hpp_src += "\t\t" + self.name.title() + " () ;\n"
        hpp_src += "\t\tvirtual  ~" + self.name.title() + " () ;\n"
        hpp_src += "\t\tvoid greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;\n"
        hpp_src += "\t\tvoid greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) ;\n"
        hpp_src += "\tprotected :\n"
        hpp_src += "\t\tvoid initialisationWavelet() ;\n"
        hpp_src += "} ;\n"
        hpp_src += "#endif\n"
        return hpp_src

    def get_cpp (self) :
        cpp_src =  "#include \"" + self.name + ".h\"\n"
        cpp_src += "#include <string.h>\n"
        cpp_src += "///Constructeur de la classe\n"
        cpp_src += "/**\t@param signalRectIn : signal to clean\n"
        cpp_src += " * \t@param nbRow : row numbers\n"
        cpp_src += " * \t@param nbRow : column numbers\n*/\n"
        cpp_src += self.name.title() + "::" + self.name.title() + "()\n"
        cpp_src += ": PAbstractWavelet() {\n"
        cpp_src += "\tinitialisationWavelet() ;\n"
        cpp_src += "}\n\n"
        cpp_src += "///Destructeur par défaut\n"
        cpp_src += self.name.title() + "::~" + self.name.title() + "() {}\n\n"

        cpp_src += "///Initialisation des paramètres d'ondelette\n"
        cpp_src += "void " + self.name.title() + "::initialisationWavelet (){\n"
        cpp_src += "\tcreateMatrix(" + str(self.size[0]) + ", " + str(self.size[1]) + ") ;\n"

        cpp_src += "\tp_matWavelet = {"
        for i in self.waveletMatrix[:-1] :
            cpp_src += str(i) + ", "
        cpp_src += str(self.waveletMatrix[-1]) + "} ;\n"
        cpp_src += "\tp_matPatch = {"
        for i in self.patch[:-1] :
            cpp_src += str(i) + ", "
        cpp_src += str(self.patch[-1]) + "} ;\n"
        cpp_src += "\tp_pace = " + str(self.pace) + " ;\n"
        cpp_src += "}\n\n"

        cpp_src += "///Greedy wavelet cleaning with neighbours surrounding signal\n"
        cpp_src += "void " + self.name.title() + "::greedyCleaningWithNeighbours (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {\n"

        cpp_src += self.__get_cleaning_mask (neighbours=True)
        #cpp_src += self.__get_neighbours_activation ()
        cpp_src += self.__get_image_reco ()
        cpp_src += self.__get_edge_cutting ()

        cpp_src += "}\n\n"

        cpp_src += "///Greedy wavelet cleaning without neighbours surrounding signal\n"
        cpp_src += "void " + self.name.title() + "::greedyCleaning (std::vector<float> & keepSignalRectOut, const std::vector<float> & signalRectIn, size_t nbRow, size_t nbCol) {\n"

        cpp_src += self.__get_cleaning_mask (neighbours=False)
        cpp_src += self.__get_image_reco ()
        cpp_src += self.__get_edge_cutting ()

        cpp_src += "}\n"
        return cpp_src

    def __get_cleaning_mask (self, neighbours=False, quad=False) :
        cpp_src  = "\t//getting the mask\n"
        cpp_src += "\tstd::vector<float> res = std::vector<float>(nbRow*nbCol, 0.0f) ;\n"
        cpp_src += "\tfor (size_t i (1lu) ; i < nbRow -1 ; i++) {\n"
        cpp_src += "\t\tfor (size_t j (1lu) ; j < nbCol -1 ; j++) {\n"
        cpp_src += "\t\t\tfloat c = 0.0f ;\n"
        for i in range(len(self.waveletMatrix)) :
            if self.waveletMatrix[i] != 0.0 :
                cpp_src += "\t\t\tc += (" + str(self.waveletMatrix[i]) + "* signalRectIn[(i"
                if self.patch[2*i] != 0.0 :
                    cpp_src += "+" + str(self.patch[2*i]) if self.patch[2*i] > 0.0 else str(self.patch[2*i])
                cpp_src += ")*nbCol + (j"
                if self.patch[2*i+1] != 0.0 :
                    cpp_src += "+" + str(self.patch[2*i+1]) if self.patch[2*i+1] > 0.0 else str(self.patch[2*i+1])
                cpp_src += ")]) ;\n"
        if neighbours :
            cpp_src += "\t\t\tfloat my_bool = (c >= p_thresholdWavelet) ;\n"
            cpp_src += "\t\t\tres[(i-1)*nbCol + j] = my_bool || res[(i-1)*nbCol + j] ;\n"
            cpp_src += "\t\t\tres[(i-1)*nbCol + j-1] = my_bool || res[(i-1)*nbCol + j-1] ;\n"
            cpp_src += "\t\t\tres[(i)*nbCol + j-1] = my_bool || res[(i)*nbCol + j-1] ;\n"
            cpp_src += "\t\t\tres[(i)*nbCol + j] = my_bool || res[(i)*nbCol + j] ;\n"
            cpp_src += "\t\t\tres[(i+1)*nbCol + j] = my_bool || res[(i+1)*nbCol + j] ;\n"
            cpp_src += "\t\t\tres[(i+1)*nbCol + j+1] = my_bool || res[(i+1)*nbCol + j+1] ;\n"
            cpp_src += "\t\t\tres[(i)*nbCol + j+1] = my_bool || res[(i)*nbCol + j+1] ;\n"
        else :
            cpp_src += "\t\t\tkeepSignalRectOut[i*nbCol+j] = (c >= p_thresholdWavelet) ;\n"
        cpp_src += "\t\t}\n"
        cpp_src += "\t}\n"
        if neighbours :
            cpp_src += "\tkeepSignalRectOut = res ;\n"
        return cpp_src

    def __get_neighbours_activation (self) :
        cpp_src  = "\t//* Neighbours activation\n"
        cpp_src += "\tstd::vector<float> res = keepSignalRectOut ;\n"
        cpp_src += "\tfor(size_t i(1lu); i < nbRow - 1lu; ++i){\n"
        cpp_src += "\t\tfor(size_t j(1lu); j < nbCol - 1lu; ++j){\n"
        cpp_src += "\t\t\tfloat my_bool = (keepSignalRectOut[i*nbCol + j] != 0.0f) ;\n"
        cpp_src += "\t\t\tres[(i-1)*nbCol + j] = my_bool ;\n"
        cpp_src += "\t\t\tres[(i-1)*nbCol + j-1] = my_bool ;\n"
        cpp_src += "\t\t\tres[(i)*nbCol + j-1] = my_bool ;\n"
        cpp_src += "\t\t\tres[(i+1)*nbCol + j] = my_bool ;\n"
        cpp_src += "\t\t\tres[(i+1)*nbCol + j+1] = my_bool ;\n"
        cpp_src += "\t\t\tres[(i)*nbCol + j+1] = my_bool ;\n"
        cpp_src += "\t\t}\n"
        cpp_src += "\t} //*/\n"
        return cpp_src

    def __get_image_reco (self) :
        cpp_src  = "\t//reconstructing image\n"
        cpp_src += "\tfor (size_t i(1lu); i < nbRow-1; i++){\n"
        cpp_src += "\t\tfor (size_t j(1lu); j < nbCol-1 ; j++) {\n"
        cpp_src += "\t\t\tif (keepSignalRectOut[i*nbCol+j] != 0.0f)\n"
        cpp_src += "\t\t\t\t\tkeepSignalRectOut[i*nbCol+j] = fabs(signalRectIn[i*nbCol+j]) ;\n"
        cpp_src += "\t\t}\n"
        cpp_src += "\t}\n"
        return cpp_src

    def __get_edge_cutting (self) :
        cpp_src  = "\t//cutting edges .. :p\n"
        cpp_src += "\tfor (size_t i(0lu); i < nbRow ; i++) {\n"
        cpp_src += "\t\tkeepSignalRectOut[i*nbCol] = 0. ;\n"
        cpp_src += "\t\tkeepSignalRectOut[i*nbCol+nbCol-1] = 0. ;\n"
        cpp_src += "\t}\n"
        cpp_src += "\tfor (size_t i(0lu); i < nbCol ; i++) {\n"
        cpp_src += "\t\tkeepSignalRectOut[i] = 0. ;\n"
        cpp_src += "\t\tkeepSignalRectOut[(nbRow-1)*nbCol+i] = 0. ;\n"
        cpp_src += "\t}\n"
        return cpp_src

    def get_param_from_file (self) :
        my_file = open("wavelets_cfg/" + self.name + ".cfg", "r")
        self.waveletMatrix = eval(my_file.readline())
        self.patch = eval(my_file.readline())
        self.pace = eval(my_file.readline())
        self.size = eval(my_file.readline())

#"""
class FactoryGenerator:
    def __init__ (self, my_wavelets) :
        self.my_wavelets = my_wavelets

    def build_hpp_factory (self) :
        hpp_src =  "#ifndef WAVELETS_FACTORY_HPP\n"
        hpp_src += "#define WAVELETS_FACTORY_HPP\n"
        for i in self.my_wavelets :
            hpp_src += "#include \"" + i + ".h\"\n"
        hpp_src += "#include \"tailcut.h\"\n"
        hpp_src += "class WaveletsFactory {\n"
        hpp_src += "\tpublic :\n"
        hpp_src += "\t\tWaveletsFactory() ;\n"
        hpp_src += "\t\tPAbstractWavelet* getWaveletByName (std::string name) ;\n"
        hpp_src += "\tprivate :\n"
        for i in self.my_wavelets :
            hpp_src += "\t\t" + i.title() + "* " + i + "_wavelet ;\n"
        hpp_src += "\t\tTailcut* tailcutObj ;\n"
        hpp_src += "} ;\n"
        hpp_src += "#endif\n"
        return hpp_src

    def build_cpp_factory (self) :
        cpp_src =  "#include \"waveletsFactory.h\"\n"
        cpp_src += "WaveletsFactory::WaveletsFactory () {\n"
        for i in self.my_wavelets :
            cpp_src += "\t" + i + "_wavelet = new " + i.title() + "() ;\n"
        cpp_src += "\ttailcutObj = new Tailcut() ;\n"
        cpp_src += "}\n"
        cpp_src += "PAbstractWavelet* WaveletsFactory::getWaveletByName(std::string name) {\n"
        for i in self.my_wavelets :
            cpp_src +=  "\tif (name == \"" + i + "\") return " + i + "_wavelet ;\n"
        cpp_src += "\telse return tailcutObj ;\n"
        cpp_src += "}\n"
        return cpp_src

    def write_sourceCode_to_file (self) :
        my_file = open("./waveletsFactory.h", "w")
        my_file.write(self.build_hpp_factory())
        my_file.close()
        my_file = open("./waveletsFactory.cpp", "w")
        my_file.write(self.build_cpp_factory())
        my_file.close()
#"""
class CompilingScript :
    def __init__ (self, wavelist) :
        self.wavelist = wavelist

    def __getCompilingScript (self) :
        ss  = "#!/bin/bash\n"
        ss += "cp wavelets_collection/* ./\n"
        ss += "g++ -c "
        for wave in self.wavelist :
            ss += wave + ".cpp "
        ss += "PAbstractWavelet.cpp tailcut.cpp waveletsFactory.cpp thresholdComputation.cpp MatrixFileSystem_CPP.cpp\n"
        ss += "g++ "
        for wave in self.wavelist :
            ss += wave + ".o "
        ss += "main.cpp PAbstractWavelet.o tailcut.o waveletsFactory.o thresholdComputation.o MatrixFileSystem_CPP.o -o theCleaner -g\n"
        ss += "rm *.o\nrm *.cpp\nrm *.h\n"
        ss += "mv theCleaner ../\n"
        return ss

    def writeCompilingScript (self) :
        f = open("compile.sh", "w")
        f.write (self.__getCompilingScript())
        f.close()
        os.system("chmod +x compile.sh")

if __name__ == "__main__" :
    t = ["myWave6", "walsh"]
    for i in t :
        wg = WaveletGenerator(i)
        wg.write_sourceCode_to_file()
    fg = FactoryGenerator(t)
    fg.write_sourceCode_to_file()
    comp = CompilingScript(t)
    comp.writeCompilingScript()
