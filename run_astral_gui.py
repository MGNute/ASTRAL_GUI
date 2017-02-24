import astral_gui_class
import sys


if __name__ == '__main__':
    sys.stderr=open('stderr.txt','w')

    app = astral_gui_class.MyApp()
    # top = main.gui_manager.gui_manager(None)
    # top.Show(True)
    # print wx.GetTopLevelWindows()
    app.MainLoop()
    # print wx.GetTopLevelWindows()