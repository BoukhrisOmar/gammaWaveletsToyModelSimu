
import sys
import numpy  as np
import scripts.HillasData as HillasData

import matplotlib.pyplot as plt

if len(sys.argv) == 6 :
    im_folder="data/im"
    sig_folder="data/sig"
    wavelet_name = sys.argv[1]
    nb_events=int(sys.argv[2])
    fact_sig_noi = (sys.argv[3])
    cam_name = sys.argv[4]
    wavelet_name += "_nei" if sys.argv[5] == "--nei" else ""
elif len(sys.argv) == 8 :
    wavelet_name = sys.argv[1]
    nb_events = int(sys.argv[2])
    fact_sig_noi = (sys.argv[3])
    cam_name = sys.argv[4]
    im_folder = sys.argv[5]
    sig_folder = sys.argv[6]
    wavelet_name += "_nei" if sys.argv[7] == "--nei" else ""
else :
    print ("argv:\n\twavelet_name nbEvent factSignalNoise cam_name --nei|notnei")
    exit()

hillasData = HillasData.HillasData(wavelet_name, nb_events, fact_sig_noi, cam_name, im_folder, sig_folder)
hillasData.save_all ()
