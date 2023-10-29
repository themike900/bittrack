import wx
import gettext
import os

import MyFrame1

cwd = os.path.abspath(os.curdir)

class BittrackApp(wx.App):
    def OnInit(self):
        gettext.install("app")

        # Set Current directory to the one containing this file.
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        wx.InitAllImageHandlers()
        self.SetAppName('Sqlite3 Creator')

        # Create the main window.
        frame_1 = MyFrame1.MyFrame1(None)
        self.SetTopWindow(frame_1)
        frame_1.Show()

        return True


# ---------------------------------------------------------------------------
if __name__ == '__main__':
    app = BittrackApp()
    app.MainLoop()