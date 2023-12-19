import wx
import wxframes
import btplotview
from pubsub import pub


def formatValue(val, cur):
    strval = ''
    if cur == 'BTC':
        strval = f"{val:,}".replace(',', '.')
    if cur == 'EUR':
        val = val * 10
        strval = f"{val:,}".replace(',', '.')
        strval = strval[:-4] + ',' + strval[-3:-1]
    return strval


# --- View -------------------------------------------------------------------------------------------------------------
class Frame(wxframes.BaseFrame):
    def __init__(self):
        super().__init__(parent=None)
        print('Frame:init')
        pub.subscribe(self.setTransactionlist, "msg_tlist_changed")
        pub.subscribe(self.setTransactionDetails, "msg_tdetails_changed")

    def setTransactionlist(self, tlistdata):
        for row in tlistdata:
            rlist = list(row)
            rlist[4] = formatValue(rlist[4], rlist[5])
            rlist[3] = f'{rlist[3]} > {rlist[6]}'
            rlist[5] = 'sats' if rlist[5] == 'BTC' else rlist[5]
            rlist[8] = 'sats' if rlist[8] == 'BTC' else rlist[8]
            self.transactionList.AppendItem(rlist)

    def setTransactionDetails(self, tdata):
        print('Frame: setTransactionDetails')
        print(tdata)
        self.fd_datetime.SetValue(tdata[1])
        self.fd_type.SetValue(tdata[2])
        self.fd_comment.SetValue(tdata[9])
        self.fd_input.SetValue(tdata[3])
        self.fd_inputval.SetValue(formatValue(tdata[4], tdata[5]))
        self.fd_output.SetValue(tdata[6])
        self.fd_outputval.SetValue(formatValue(tdata[7], tdata[8]))
        self.ld_inputval.SetLabelText(tdata[5])
        self.ld_outputval.SetLabelText(tdata[8])
        self.fd_fee.SetValue(formatValue(tdata[10], tdata[11]))
        self.ld_fee.SetLabelText(tdata[11])
        fractionBase = tdata[4] if tdata[5] == 'BTC' else tdata[7]
        self.ld_fraction.SetLabelText(f'{tdata[10]/fractionBase*100:.1f}%')
        # set background colors
        if tdata[5] == 'BTC':
            self.fd_inputval.SetBackgroundColour(wx.Colour(254, 234, 214))
        else:
            self.fd_inputval.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        if tdata[8] == 'BTC':
            self.fd_outputval.SetBackgroundColour(wx.Colour(254, 234, 214))
        else:
            self.fd_outputval.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

    def onSelectionChanged(self, event):
        selectedRow = self.transactionList.SelectedRow
        print(self.transactionList.GetValue(selectedRow, 0))
        pub.sendMessage("msg_selectionChanged", selected=self.transactionList.GetValue(selectedRow, 0))

    def aboutaction(self, event):
        print('about pressed')
        wxframes.AboutDialog(self).ShowModal()

    def onOpenWalletSums(self, event):
        print('onOpenWalletSums')
        sumDialog = WalletSums(self)
        sumDialog.ShowModal()
        print('onOpenWalletSums:end')

    def onOpenPlots(self, event):
        print('onOpenPlots')
        plotDialog = btplotview.plotDialog(self)
        plotDialog.ShowModal()
        print('onOpenPlots:end')

    def closeaction(self, event):
        self.Close(True)


class WalletSums(wxframes.sumDialog):
    def __init__(self, parent):
        print('WalletSum:init')
        super().__init__(parent)

        pub.subscribe(self.setWalletLists, 'msg_newWalletSums')
        pub.sendMessage('msg_getWalletSums')

    def setWalletLists(self, ncsums, csums, lnsums, allsum):
        print('setWalletSums')
        for row in ncsums:
            if row[1] != 0:
                wlist = list(row)
                wlist[1] = formatValue(wlist[1], 'BTC')
                wlist[2] = formatValue(wlist[2], 'EUR')
                self.ncWalletList.AppendItem(wlist)
        for row in csums:
            if row[1] != 0:
                wlist = list(row)
                wlist[1] = formatValue(wlist[1], 'BTC')
                wlist[2] = formatValue(wlist[2], 'EUR')
                self.cWalletList.AppendItem(wlist)
        for row in lnsums:
            if row[1] != 0:
                wlist = list(row)
                wlist[1] = formatValue(wlist[1], 'BTC')
                wlist[2] = formatValue(wlist[2], 'EUR')
                self.lnWalletList.AppendItem(wlist)
        self.fd_allsum.SetValue(formatValue(allsum[0], 'BTC'))
        self.fd_allsumfiat.SetValue(formatValue(allsum[1], 'EUR'))


