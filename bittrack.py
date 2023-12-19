import wx
import os
import sys
import requests
import json
from pubsub import pub
from pubsub.utils.notification import useNotifyByWriteFile
import btmodel
import btview
from datetime import date, datetime, timedelta

# useNotifyByWriteFile(sys.stdout)

# cwd = os.path.abspath(os.curdir)


# --- Controller -------------------------------------------------------------------------------------------------------
class AppController:
    def __init__(self):
        print('Controller:init')

        pub.subscribe(self.selectedChanged, 'msg_selectionChanged')
        pub.subscribe(self.listChanged, 'msg_listChanged')
        pub.subscribe(self.getWalletSums, 'msg_getWalletSums')
        pub.subscribe(self.getPlotdata, 'msg_getPlotdata')

        self.listChanged()
        self.updateTimetable()

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

    def getPlotdata(self):
        startdate = '2020-01-01'
        enddate = '2023-12-31'
        pdlist = app.model.getPlotdata(startdate, enddate)
        pub.sendMessage('msg_newPlotdata', pdlist=pdlist)

    def updateTimetable(self):
        # get last date in timetable and calculation number of new changrates to request
        ttdatestr, btcsum = app.model.getTimetableLast()
        ttdate = date.fromisoformat(ttdatestr)
        newrows = (date.today() - ttdate).days + 1
        resp_cg = requests.get(f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=eur&days={newrows}&interval=daily&precision=0')
        prlist = json.loads(resp_cg.text)['prices']
        if date.fromtimestamp(prlist[-2][0]/1000) == date.fromtimestamp(prlist[-1][0]/1000):
            prlist.pop(-1)
        newtlist = app.model.getNewTransactions(ttdatestr)
        # print('newtlist:', newtlist)
        # print('prlist:', prlist)
        # print(ttdatestr, btcsum)
        ntlrow = 0
        updatelist = []
        for prrow in prlist:
            # print(datetime.fromtimestamp(prrow[0]/1000), ntlrow)
            if ntlrow < len(newtlist):
                if date.fromtimestamp(prrow[0]/1000) == date.fromisoformat(newtlist[ntlrow][0]):
                    btcsum += newtlist[ntlrow][1]
                    # print(ntlrow, btcsum, newtlist[ntlrow][1])
                    ntlrow += 1
            prrow.append(btcsum)
            prrow.append(int(round(prrow[1] * btcsum / 1000000, 0)))
            prrow[0] = str(date.fromtimestamp(prrow[0]/1000))
            # print(date.fromtimestamp(prrow[0]/1000) == date.fromisoformat(newtlist[ntlrow][0]))
            # print(datetime.fromtimestamp(prrow[0]/1000), prrow)
            updatelist.append(tuple(prrow))
        # print(updatelist)
        app.model.updateTimetable(updatelist)




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
    app.MainLoop()
