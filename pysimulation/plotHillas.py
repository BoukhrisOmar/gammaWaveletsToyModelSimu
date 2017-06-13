import scripts.HillasPlotter as HillasPlotter
import scripts.DiffHillasPlotter as DiffHillasPlotter
import scripts.PlotHillasParamErr as PlotHillasParamErr
import sys

if len(sys.argv) == 3 :
    cam = sys.argv[1]
    wavelet_name = sys.argv[2]
    histplotter = HillasPlotter.HillasPlotter(cam, wavelet_name, ["0.2", "0.3", "0.4", "0.5", "0.6"])
    #histplotter = HillasPlotter.HillasPlotter(cam, wavelet_name, [ "0.3"])
    histplotter.plot_all()
elif len(sys.argv) >= 4 :
    cam_name = sys.argv[1]
    fact = sys.argv[2]
    wave_list = [sys.argv[i] for i in range(3, len(sys.argv))]
    histplotter = DiffHillasPlotter.DiffHillasPlotter(wave_list, fact, cam_name)
    #histplotter.print_eps()
    histplotter.plot_all()
else :
    print ("argv :\n\t cam_name wavelet_name\n\t[*] cam_name factSignalNoise wavelet_list")
