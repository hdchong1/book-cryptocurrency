import sys
import time
import pybithumb
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidgetItem, QProgressBar
# ----------------- 수 정 ------------------
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPropertyAnimation
# ------------------------------------------

class TickerlistWorker(QThread):
    dataSent = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.alive = True

    def run(self):
        while self.alive:
            # data  = pybithumb.get_orderbook(self.ticker, limit=10)

            # tickers = pybithumb.get_tickers()
            all_prices = pybithumb.get_current_price("ALL")
            # print(all_prices)

            # data  = pybithumb.get_tickerlist(self.ticker, limit=10)
            time.sleep(1)
            print("2)")
            if all_prices != None:
                self.dataSent.emit(all_prices)

    def close(self):
        self.alive = False


class TickerlistWidget(QWidget):
    def __init__(self, tickers=[], all_prices=[]):
        super().__init__()
        uic.loadUi("resource/tickerlist.ui", self)
        self.tickers = pybithumb.get_tickers()
        self.current_tickers = []
        self.all_prices = pybithumb.get_current_price("ALL")
        # ----------------- 추 가 ------------------
        # self.asksAnim = [ ]
        # self.bidsAnim = [ ]
        # ------------------------------------------

        # tickers = pybithumb.get_tickers()
        # all_prices = pybithumb.get_current_price("ALL")
        print(all_prices)

        for i in range(len(self.tickers)-1):
            self.tickerTableList.insertRow(1)
        # print("1)", self.tickerTableList.rowCount(), len(tickers))

        for i in range(self.tickerTableList.rowCount()):
            item_0 = QTableWidgetItem(str(""))
            item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 0, item_0)

            item_1 = QTableWidgetItem(int(0))
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 1, item_1)

            item_2 = QTableWidgetItem(int(0))
            item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 2, item_1)
            item_3 = QTableWidgetItem(int(0))
            item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 3, item_3)

        self.tl = TickerlistWorker()
        self.tl.dataSent.connect(self.updateData)
        self.tl.start()


        # print("2)", self.tickerTableList.rowCount())

        # for i, ticker in enumerate(tickers):
        #     # print(i, ticker, all_prices[ticker]['closing_price'], all_prices[ticker]['fluctate_rate_24H'])
        #     item_0 = self.tickerTableList.item(i, 0)
        #     item_0.setText(ticker)
        #     item_1 = QTableWidgetItem()
        #     item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        #     # item_1.setData(Qt.DisplayRole, format(float(all_prices[ticker]['closing_price']),',')) #숫자로 설정 (정렬을 위해)
        #     item_1.setData(Qt.DisplayRole, float(all_prices[ticker]['closing_price'])) #숫자로 설정 (정렬을 위해)
        #     self.tickerTableList.setItem(i, 1, item_1)
        #     item_2 = QTableWidgetItem()
        #     item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        #     item_2.setData(Qt.DisplayRole, float(all_prices[ticker]['fluctate_rate_24H'])) #숫자로 설정 (정렬을 위해)
        #     self.tickerTableList.setItem(i, 2, item_2)
        #     item_3 = QTableWidgetItem()
        #     item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        #     item_3.setData(Qt.DisplayRole, float(all_prices[ticker]['acc_trade_value_24H'])) #숫자로 설정 (정렬을 위해)
        #     self.tickerTableList.setItem(i, 3, item_3)

        for ticker, price in self.all_prices.items():
            # print(i, ticker, self.all_prices[ticker]['closing_price'], all_prices[ticker]['fluctate_rate_24H'])
            i = self.tickers.index(ticker)

            item_0 = self.tickerTableList.item(i, 0)
            item_0.setText(ticker)
            item_1 = QTableWidgetItem()
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_1.setData(Qt.DisplayRole, float(price['closing_price'])) #숫자로 설정 (정렬을 위해)
            self.tickerTableList.setItem(i, 1, item_1)
            item_2 = QTableWidgetItem()
            item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_2.setData(Qt.DisplayRole, float(price['fluctate_rate_24H'])) #숫자로 설정 (정렬을 위해)
            self.tickerTableList.setItem(i, 2, item_2)
            item_3 = QTableWidgetItem()
            item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_3.setData(Qt.DisplayRole, float(price['acc_trade_value_24H'])) #숫자로 설정 (정렬을 위해)
            self.tickerTableList.setItem(i, 3, item_3)




    def updateData(self, all_prices):

       # tradingBidValues = [ ]
        # for v in data['bids']:
        #     tradingBidValues.append(int(v['price'] * v['quantity']))
        # tradingAskValues = [ ]
        # for v in data['asks'][::-1]:
        #     tradingAskValues.append(int(v['price'] * v['quantity']))
        # maxtradingValue = max(tradingBidValues + tradingAskValues)
        # maxtradingValue = max(tradingBidValues)

        # for i, v in enumerate(data['asks'][::-1]):
        #     item_0 = self.tickerTableList.item(i, 0)
        #     item_0.setText(f"{v['price']:,}")
        #     item_1 = self.tickerTableList.item(i, 1)
        #     item_1.setText(f"{v['quantity']:,}")
        #     item_2 = self.tickerTableList.cellWidget(i, 2)
        #     item_2.setRange(0, maxtradingValue)
        #     item_2.setFormat(f"{tradingAskValues[i]:,}")
        #     # item_2.setValue(tradingAskValues[i])
        #     # ----------------- 추 가 ------------------
        #     self.asksAnim[i].setStartValue(item_2.value() if item_2.value() > 0 else 0)
        #     self.asksAnim[i].setEndValue(tradingAskValues[i])
        #     self.asksAnim[i].start()
        #     # ------------------------------------------

        # tickers = pybithumb.get_tickers()
        # all_prices = pybithumb.get_current_price("ALL")


        # i = 0
        # for ticker in tickers:
        #     print(i, ticker, all_prices[ticker]['closing_price'])
        #     item_0 = self.tickerTableList.item(i, 0)
        #     item_0.setText(ticker)
        #     item_1 = self.tickerTableList.item(i, 1)
        #     item_1.setText(all_prices[ticker]['closing_price'])
        #     item_2 = self.tickerTableList.item(i, 2)
        #     item_2.setText(all_prices[ticker]['prev_closing_price'])
        #     item_3 = self.tickerTableList.item(i, 3)
        #     item_3.setText(all_prices[ticker]['fluctate_rate_24H'])
        #
        #     i = i + 1
        #     if i == self.tickerTableList.rowCount() :
        #         print('break')
        #         break

       try: # 윈도우에서 정렬시 변경되는 값과의 매칭이 시간내에 이루어지지 않을경우 생기는 오류에 대비
            self.all_prices = all_prices
            # 클래스 변수로 사용, 프로그램 다운 오류 해결 exit code -1073740791 (0xc0000409)
            for ticker, price in self.all_prices.items():
                i = self.current_tickers.index(ticker)

                item_0 = self.tickerTableList.item(i, 0)
                item_0.setText(ticker)
                item_1 = QTableWidgetItem()
                item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_1.setData(Qt.DisplayRole, float(price['closing_price'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 1, item_1)
                item_2 = QTableWidgetItem()
                item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_2.setData(Qt.DisplayRole, float(price['fluctate_rate_24H'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 2, item_2)
                item_3 = QTableWidgetItem()
                item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_3.setData(Qt.DisplayRole, float(price['acc_trade_value_24H'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 3, item_3)

       except Exception as e:
            print('exception:', e, ticker)

            # self.current_tickers = []
            print("current", self.all_prices)
            for i, ticker in enumerate(self.all_prices):
                print("current", i, self.tickerTableList.item(i,0).text())
                # self.current_tickers.append(self.tickerTableList.item(i,0).text())
            self.all_prices = pybithumb.get_current_price("ALL")
            print('initialize')
            print("new", self.all_prices)
            pass



        # for i, v in enumerate(data['bids']):
        #     item_0 = self.tickerTableList.item(i, 0)
        #     item_0.setText(f"{v['price']:,}")
        #     item_1 = self.tickerTableList.item(i, 1)
        #     item_1.setText(f"{v['quantity']:,}")
        #     item_2 = self.tickerTableList.item(i, 2)
        #     item_2.setText(f"{tradingBidValues[i]:,}")
            # item_2 = self.tickerTableList.cellWidget(i, 2)
            # item_2.setRange(0, maxtradingValue)
            # item_2.setFormat(f"{tradingBidValues[i]:,}")
            # item_2.setValue(tradingBidValues[i])
            # ----------------- 추 가 ------------------
            # self.bidsAnim[i].setStartValue(item_2.value() if item_2.value() > 0 else 0)
            # self.bidsAnim[i].setEndValue(tradingBidValues[i])
            # self.bidsAnim[i].start()
            # ------------------------------------------

    def closeEvent(self, event):
        self.tl.close()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    tl = TickerlistWidget()
    tl.show()
    exit(app.exec_())
