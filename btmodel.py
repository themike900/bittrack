import sqlite3
from datetime import datetime, date, timedelta


# --- Model ------------------------------------------------------------------------------------------------------------
class Model:
    def __init__(self):
        print('Model:init')
        self.dbcon = sqlite3.connect('db/bittrack.db',
                                     detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.dbcur = self.dbcon.cursor()

    def getTransactionList(self):
        tlist = self.dbcon.execute('''
            SELECT t.t_id,t_datetime,t_type, tdi.td_wallet, tdi.td_amount, tdi.td_cur, tdo.td_wallet, tdo.td_amount, tdo.td_cur
            FROM transact t, t_data tdi, t_data tdo
            WHERE t.t_id=tdi.t_id and t.t_id=tdo.t_id and tdi.td_type="in" and tdo.td_type="out"
            ORDER BY t_datetime DESC
            ''').fetchall()
        return tlist

    def getTransactionDetails(self, t_id):
        tdetails = self.dbcon.execute('''
            SELECT t.t_id,t_datetime,t_type, tdi.td_wallet, tdi.td_amount, tdi.td_cur, tdo.td_wallet, tdo.td_amount, tdo.td_cur, t.t_comment
            FROM transact t, t_data tdi, t_data tdo
            WHERE t.t_id=tdi.t_id AND t.t_id=tdo.t_id AND tdi.td_type="in" AND tdo.td_type="out" AND t.t_id=?
            ''', (t_id,)).fetchone()
        return tdetails

    def getTransactionFees(self, t_id):
        tfees = self.dbcon.execute('''
            SELECT t_id, td_type, td_wallet, td_amount, td_cur
            FROM t_data
            WHERE td_type="fee" AND t_id=?
            ''', (t_id,)).fetchone()
        return tfees

    def getWalletSums(self, td_type, changerate):
        walletsums = self.dbcon.execute('''
            SELECT src_name, sum(td_amount) , sum(td_amount)*?/1000000
            FROM walletvalues
            WHERE src_subtype=? GROUP BY src_name
            ''', (changerate, td_type)).fetchall()
        return walletsums

    def getAllSum(self, changerate):
        allsum = self.dbcon.execute('''
            SELECT sum(td_amount), sum(td_amount)*?/1000000
            FROM walletvalues
            WHERE src_type ="wallet"
            ''', (changerate,)).fetchone()
        return allsum

    def getChangerate(self):
        query = '''
            SELECT value, date 
            FROM parameters 
            WHERE name="changerate"
            '''
        changerate = self.dbcon.execute(query).fetchone()
        chdate = datetime.strptime(changerate[1], '%Y-%m-%d %X')
        today = datetime.now()
        age = int((today - chdate).total_seconds()/60)
        return changerate[0], age

    def saveChangerate(self, changerate):
        print(f'rate to save {changerate}')
        chdate = datetime.now().strftime('%Y-%m-%d %X')
        query = '''
            UPDATE parameters
            SET value = ?, date = ?
            WHERE name = "changerate"
            '''
        self.dbcon.execute(query, (changerate, chdate))
        self.dbcon.commit()
        return

    def getPlotdata(self, startdate, enddate):
        print(startdate, enddate)
        query = '''
            SELECT date, btcsum, fiatval
            FROM timetable
            WHERE date >= ? AND date <= ? AND btcsum > 0
            '''
        pdlist = self.dbcon.execute(query, (startdate, enddate)).fetchall()
        return pdlist

    def getTimetableLast(self):
        print('model: getTimetableLast')
        query = 'SELECT max(date) from timetable'
        ttlastdate = self.dbcon.execute(query).fetchone()[0]
        ttlastbtc = date.isoformat(date.fromisoformat(ttlastdate) - timedelta(days=1))
        query = 'SELECT btcsum FROM timetable WHERE date=?'
        ttlastbtcsum = self.dbcon.execute(query, (ttlastbtc, )).fetchone()[0]
        # print('ttlastdate:', ttlastdate, ttlastbtcsum)
        return ttlastdate, ttlastbtcsum

    def updateTimetable(self, ttlist):
        print('model: updateTimetable')
        # print('ttlist:', ttlist)
        query = 'DELETE FROM timetable WHERE date=?'
        self.dbcon.execute(query, (ttlist[0][0],))
        for row in ttlist:
            query = 'INSERT INTO timetable(date,changerate,btcsum,fiatval) VALUES(?,?,?,?)'
            print('row:', row)
            self.dbcon.execute(query, row)
        self.dbcon.commit()

    def getNewTransactions(self, startdate):
        query = 'SELECT tday, sum(td_amount) FROM dayvalues  WHERE tday>=? GROUP BY tday ORDER BY tday'
        newtransactions = self.dbcon.execute(query, (startdate,)).fetchall()
        return newtransactions

    def dbclose(self):
        print('model:dbclose')
        self.dbcur.close()
        self.dbcon.close()

