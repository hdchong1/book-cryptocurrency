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

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True

    def run(self):
        while self.alive:
            data  = pybithumb.get_orderbook(self.ticker, limit=10)

            # tickers = pybithumb.get_tickers()
            # all_prices = pybithumb.get_current_price("ALL")
            # for ticker in tickers:
            #     print(ticker, all_prices[ticker]['closing_price'])

            # data  = pybithumb.get_tickerlist(self.ticker, limit=10)
            time.sleep(0.05)
            self.dataSent.emit(data)

    def close(self):
        self.alive = False


class TickerlistWidget(QWidget):
    def __init__(self, ticker="BTC"):
        super().__init__()
        uic.loadUi("resource/tickerlist.ui", self)
        self.ticker = ticker

        # ----------------- 추 가 ------------------
        # self.asksAnim = [ ]
        # self.bidsAnim = [ ]
        # ------------------------------------------

        for i in range(self.tickerTableList.rowCount()):
            # 매도호가
            # print(self.tickerTableList.rowCount())
            item_0 = QTableWidgetItem(str(""))
            item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 0, item_0)

            item_1 = QTableWidgetItem(str(""))
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 1, item_1)

            item_2 = QTableWidgetItem(str(""))
            item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 2, item_2)

            item_3 = QTableWidgetItem(str(""))
            item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tickerTableList.setItem(i, 3, item_3)
            # item_2 = QProgressBar(self.tickerTableList)
            # item_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            # item_2.setStyleSheet("""
            #     QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
            #     QProgressBar::Chunk {background-color : rgba(255, 0, 0, 50%);border : 1}
            # """)
            # self.tickerTableList.setCellWidget(i, 2, item_2)
            # ----------------- 추 가 ------------------
            # anim = QPropertyAnimation(item_2, b"value")
            # anim.setDuration(200)
            # self.asksAnim.append(anim)
            # ------------------------------------------

            # # 매수호가
            # item_0 = QTableWidgetItem(str(""))
            # item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            # self.tickerTableList.setItem(i, 0, item_0)
            #
            # item_1 = QTableWidgetItem(str(""))
            # item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            # self.tickerTableList.setItem(i, 1, item_1)
            #
            # item_2 = QProgressBar(self.tickerTableList)
            # item_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            # item_2.setStyleSheet("""
            #     QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
            #     QProgressBar::Chunk {background-color : rgba(0, 255, 0, 40%);border : 1}
            # """)
            # self.tickerTableList.setCellWidget(i, 2, item_2)
            # # ----------------- 추 가 ------------------
            # anim = QPropertyAnimation(item_2, b"value")
            # anim.setDuration(200)
            # self.bidsAnim.append(anim)
            # # ------------------------------------------
        self.tl = TickerlistWorker(self.ticker)
        self.tl.dataSent.connect(self.updateData)
        # self.tl.start()

        tickers = pybithumb.get_tickers()
        all_prices = pybithumb.get_current_price("ALL")
        i = 0
        for ticker in tickers:
            print(i, ticker, all_prices[ticker]['closing_price'])
            item_0 = self.tickerTableList.item(i, 0)
            item_0.setText(ticker)
            item_1 = self.tickerTableList.item(i, 1)
            item_1.setText(all_prices[ticker]['closing_price'])
            item_2 = self.tickerTableList.item(i, 2)
            item_2.setText(all_prices[ticker]['fluctate_rate_24H'])
            item_3 = self.tickerTableList.item(i, 3)
            item_3.setText(all_prices[ticker]['acc_trade_value_24H'])

            i = i + 1
            if i == self.tickerTableList.rowCount() :
                print('break')
                break





    def updateData(self, data):
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

        tickers = pybithumb.get_tickers()
        all_prices = pybithumb.get_current_price("ALL")
        i = 0
        for ticker in tickers:
            print(i, ticker, all_prices[ticker]['closing_price'])
            item_0 = self.tickerTableList.item(i, 0)
            item_0.setText(ticker)
            item_1 = self.tickerTableList.item(i, 1)
            item_1.setText(all_prices[ticker]['closing_price'])
            item_2 = self.tickerTableList.item(i, 2)
            item_2.setText(all_prices[ticker]['prev_closing_price'])
            item_3 = self.tickerTableList.item(i, 3)
            item_3.setText(all_prices[ticker]['fluctate_rate_24H'])

            i = i + 1
            if i == self.tickerTableList.rowCount() :
                print('break')
                break

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
