import wx
import os
import requests
import json
from pubsub import pub
# from pubsub.utils.notification import useNotifyByWriteFile
import btmodel
import btview

# useNotifyByWriteFile(sys.stdout)

# cwd = os.path.abspath(os.curdir)


# --- Controller -------------------------------------------------------------------------------------------------------
class AppController:
    def __int__(self):
        print('Controller:init')

        pub.subscribe(self.selectedChanged, 'msg_selectionChanged')
        pub.subscribe(self.listChanged, 'msg_listChanged')
        pub.subscribe(self.getWalletSums, 'msg_getWalletSums')

        self.listChanged()

    def listChanged(self):
        tlist = app.model.getTransactionList()
        pub.sendMessage('msg_tlist_changed', tlistdata=tlist)

    def selectedChanged(self, selected):
        tdetails = app.model.getTransactionDetails(selected)
        tfees = app.model.getTransactionFees(selected)
        if tfees:
            tdetails = (tdetails + tfees[3:])
        else:
            tdetails = (tdetails + (0, 'BTC'))
        # print(tdetails)
        pub.sendMessage('msg_tdetails_changed', tdata=tdetails)

    def getWalletSums(self):
        print('cntrl:getWalletSums')
        changerate = self.getChangerate()
        nc_walletSums = app.model.getWalletSums('nc', changerate)
        c_walletSums = app.model.getWalletSums('c', changerate)
        ln_walletSums = app.model.getWalletSums('ln', changerate)
        allsum = app.model.getAllSum(changerate)
        pub.sendMessage('msg_newWalletSums', ncsums=nc_walletSums, csums=c_walletSums, lnsums=ln_walletSums, allsum=allsum)

    def getChangerate(self):
        rate, age = app.model.getChangerate()
        if age > 10:
            resp_kraken = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTEUR')
            jdata = json.loads(resp_kraken.text)
            rate = jdata["result"]["XXBTZEUR"]["a"][0][:-6]
            app.model.saveChangerate(rate)
            age = 0
        return rate


# ---------------------------------------------------------------------------------------------------------------------
class BittrackApp(wx.App):
    def OnInit(self):

        # Set Current directory to the one containing this file.
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        wx.InitAllImageHandlers()
        self.SetAppName('BitTrack')

        # Initialise model
        self.model = btmodel.Model()

        # Initialise main window.
        self.baseFrame = btview.Frame()
        self.SetTopWindow(self.baseFrame)
        self.baseFrame.Show()

        return True

    def OnExit(self):
        self.model.dbclose()
        return True


# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = BittrackApp()
    c = AppController()
    c.__int__()
    app.MainLoop()
