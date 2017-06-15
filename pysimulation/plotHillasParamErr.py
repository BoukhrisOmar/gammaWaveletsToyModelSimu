import scripts.HillasPlotter as HillasPlotter
import scripts.DiffHillasPlotter as DiffHillasPlotter
import scripts.PlotHillasParamErr as PlotHillasParamErr
import sys

if len(sys.argv) >= 3 :
    cam_name = sys.argv[1]
    fact = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    wave_list = [sys.argv[i] for i in range(2, len(sys.argv))]
    hillasErrPlot = PlotHillasParamErr.PlotHillasParamErr (wave_list, fact, cam_name)
    hillasErrPlot.plot_all()
else :
    print ("argv :\n\tcam_name and wavelets list as arguments")
