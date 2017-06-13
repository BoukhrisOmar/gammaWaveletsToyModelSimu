
import sys, os
import scripts.MatrixFileSystem as MatrixFileSystem
import scripts.MyProgressBar as MyProgressBar

"""
cleaning command :
    python file.py wavelet_name nbEventToClean fact pathToEvents
event generator command :
    python generate_events.py nbEvent data/image data/signal data/noise fact wavelet
"""

help_msg = "usage\n\tpython file.py wavelet_name --nei|notnei nbEventToClean fact cam_name pathToEvents"

if len(sys.argv) == 7 :
    wavelet_name = sys.argv[1]
    keepNei = "--nei" if sys.argv[2] == "--nei" else "--notnei"
    nb_events = int(sys.argv[3])
    fact = sys.argv[4]
    cam_name = sys.argv[5]
    path = sys.argv[6]
else :
    print (help_msg)
    exit ()

cameras = {"dragon" : 0, "flash" : 10, "nectar" : 50, "sct" : 100}

path = path + "/" + cam_name + "/" + str(fact)
if keepNei == "--notnei" :
    cleaned_sig = MatrixFileSystem.MatrixFileSystem (path + "/" + wavelet_name + "/cleaned_telescope")
else :
    cleaned_sig = MatrixFileSystem.MatrixFileSystem (path + "/" + wavelet_name + "_nei/cleaned_telescope")

#dwt_sig = MatrixFileSystem.MatrixFileSystem (path + "/" + wavelet_name + "/dwt")
#dwt_shrunk_sig = MatrixFileSystem.MatrixFileSystem (path + "/" + wavelet_name + "/dwt_shrunk")

progbar = MyProgressBar.MyProgressBar(nb_events)
for i in range (nb_events) :
    os.system ("./theCleaner " + keepNei + " " + str(i) + " " + wavelet_name + " " + path)
    cleaned_sig.save_text2bin (i)
    #dwt_sig.save_text2bin (i)
    #dwt_shrunk_sig.save_text2bin (i)
    progbar.update()
print("")
