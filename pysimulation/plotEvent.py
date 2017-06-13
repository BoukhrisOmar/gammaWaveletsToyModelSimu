import scripts.Plotter as Plotter
import sys

#$1 : wavelet name
#$2 : nbevent
#$3 : s/n coef
#$4 : camera to use

if len(sys.argv) == 5 :
    wavelet_name = sys.argv[1]
    nbevent = sys.argv[2]
    fact = sys.argv[3]
    cam_name = sys.argv[4]
    p = Plotter.Plotter (wavelet_name, nbevent, fact, cam_name)
    p.plot_all()
else :
    print ("argv :\n\twavelet_name event_number fact(s/n) cam_name")
    exit()
