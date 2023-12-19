import wx
from pubsub import pub
import numpy as np
import wxmplot
from datetime import date


class plotDialog (wx.Dialog):

    def __init__(self, parent):
        print('plotDialog:init')

        super().__init__(parent, id=wx.ID_ANY, title='btc/fiat plots', pos=wx.DefaultPosition, size=wx.Size(1200, 700), style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        dialogSizer = wx.BoxSizer(wx.VERTICAL)

        self.plotPanel = wxmplot.PlotPanel(self, dpi=100, fontsize=9)
        dialogSizer.Add(self.plotPanel, 1, wx.EXPAND |wx.ALL, 5)

        self.m_ok = wx.Button(self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_ok.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Verdana"))
        dialogSizer.Add(self.m_ok, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(dialogSizer)
        self.Layout()
        self.Centre(wx.BOTH)

        pub.subscribe(self.plotHistory, 'msg_newPlotdata')
        pub.sendMessage('msg_getPlotdata')

    def plotHistory(self, pdlist):
        print('plot pdlist')
        tlist = [date.fromisoformat(row[0]) for row in pdlist]
        btclist = [row[1]/100000000 for row in pdlist]
        fiatlist = [row[2]/100000 for row in pdlist]
        self.plotPanel.plot(tlist,  btclist,  use_dates=True, ylabel='BTC',   linewidth=1, labelfontsize=9)
        self.plotPanel.oplot(tlist, fiatlist, use_dates=True, y2label='kEUR', linewidth=1, labelfontsize=9, side='right')

    def __del__(self):
        pass
