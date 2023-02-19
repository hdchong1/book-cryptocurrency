import sys
import time
import pybithumb
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidgetItem, QProgressBar
# ----------------- 수 정 ------------------
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPropertyAnimation, pyqtSlot
# ------------------------------------------

class TickerlistWorker(QThread):
    dataSent = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.alive = True

    def run(self):
        while self.alive:
            print("2)")

            all_prices = pybithumb.get_current_price("ALL")
            time.sleep(2)
            if all_prices != None:
                self.dataSent.emit(all_prices)

    def close(self):
        self.alive = False


class TickerlistWidget(QWidget):
    def __init__(self, tickers=[], all_prices={}):
        super().__init__()
        uic.loadUi("resource/tickerlist.ui", self)
        self.all_prices = pybithumb.get_current_price("ALL")
        # self.tickers = pybithumb.get_tickers()
        self.tickers = list(self.all_prices.keys())
        self.current_tickers = []

        print("0)")
        for i in range(len(self.tickers)-1):
            self.tickerTableList.insertRow(1)

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


        for ticker, prices in self.all_prices.items():
            i = self.tickers.index(ticker)

            item_0 = self.tickerTableList.item(i, 0)
            item_0.setText(ticker)
            item_1 = QTableWidgetItem()
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_1.setData(Qt.DisplayRole, float(prices['closing_price'])) #숫자로 설정 (정렬을 위해)
            self.tickerTableList.setItem(i, 1, item_1)
            item_2 = QTableWidgetItem()
            item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_2.setData(Qt.DisplayRole, float(prices['fluctate_rate_24H'])) #숫자로 설정 (정렬을 위해)
            self.tickerTableList.setItem(i, 2, item_2)
            item_3 = QTableWidgetItem()
            item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_3.setData(Qt.DisplayRole, float(prices['acc_trade_value_24H'])) #숫자로 설정 (정렬을 위해)
            self.tickerTableList.setItem(i, 3, item_3)

        print("1)")

    @pyqtSlot(dict)
    def updateData(self, all_prices):

       try: # 윈도우에서 정렬시 변경되는 값과의 매칭이 시간내에 이루어지지 않을 경우 생기는 오류에 대비
            print("3)update")

            # self.all_prices = all_prices
            self.all_prices = pybithumb.get_current_price("ALL")
            self.current_tickers.clear()

            for i in range(self.tickerTableList.rowCount()):
                item_0 = QTableWidgetItem(str(""))
                item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.tickerTableList.setItem(i, 0, item_0)
                item_1 = QTableWidgetItem(int(0))
                item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.tickerTableList.setItem(i, 1, item_1)
                item_2 = QTableWidgetItem(int(0))
                item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.tickerTableList.setItem(i, 2, item_2)
                item_3 = QTableWidgetItem(int(0))
                item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.tickerTableList.setItem(i, 3, item_3)

            # tikcer 순으로 정렬
            self.current_tickers = sorted(list(self.all_prices.keys()))
            # print(self.current_tickers)

            # # 가격 순으로 정렬
            # self.current_tickers = sorted(float(self.all_prices['closing_price']), key=self.all_prices.get)
            # print(self.current_tickers)

            # # 상승률 순으로 정렬
            # self.current_tickers = sorted(float(self.all_prices['fluctate_rate_24H']), key=self.all_prices.get)
            # print(self.current_tickers)

            # # 현재 테이블의 순서 그대로 가져오기
            # for i in range(self.tickerTableList.rowCount()):
            #     self.current_tickers.append(self.tickerTableList.item(i,0).text())

            # 클래스 변수로 사용, 프로그램 다운 오류 해결 exit code -1073740791 (0xc0000409)
            # print(self.all_prices)
            # i = 0
            new_tickers = list(self.all_prices.keys())
            for ticker, prices in self.all_prices.items():
                i = self.current_tickers.index(ticker)
                # i = self.tickers.index(ticker)
                # i = new_tickers.index(ticker)
                # time.sleep(0.1)
                print(str(i)+':'+ ticker)

                item_0 = self.tickerTableList.item(i, 0)
                item_0.setText(str(i)+':'+ ticker)
                print(str(i)+':1')
                # item_1 = QTableWidgetItem()
                # item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                # item_1.setData(Qt.DisplayRole, float(prices['closing_price'])) #숫자로 설정 (정렬을 위해)
                # self.tickerTableList.setItem(i, 1, item_1)
                item_1 = QTableWidgetItem()
                item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_1.setData(Qt.DisplayRole, i) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 1, item_1)
                print(str(i)+':2')
                item_2 = QTableWidgetItem()
                item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_2.setData(Qt.DisplayRole, float(prices['fluctate_rate_24H'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 2, item_2)
                print(str(i)+':3')
                item_3 = QTableWidgetItem()
                item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_3.setData(Qt.DisplayRole, float(prices['acc_trade_value_24H'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 3, item_3)
                print(str(i)+':4')

                if i == 9:
                    break
                # i=i+1
            print("4)updated"+ str(len(list(self.all_prices.keys()))))

       except Exception as e:
            print('exception:', e)
            #
            # # 현재 테이블의 순서 그대로 가져오기
            # ec_ticker = ""
            # ec_current_tickers = []
            # # 현재 테이블의 순서 그대로 가져오기
            # for i in range(self.tickerTableList.rowCount()):
            #     ec_current_tickers.append(self.tickerTableList.item(i,0).text())
            #     ec_ticker = ec_ticker + ',' + str(i)+':'+self.tickerTableList.item(i,0).text()
            #     # print(ticker)
            # print(len(ec_current_tickers))
            # print(ec_ticker)
            #
            # self.current_tickers.clear()
            # e_ticker = ""
            # for ticker in self.all_prices.items():
            #     self.current_tickers.append(ticker)
            #     e_ticker = e_ticker + ',' + ticker
            #     # print(ticker)
            # print(len(self.current_tickers))
            # print(self.current_tickers)
            # print(e_ticker)
            #
            # eu_ticker = ""
            # # 클래스 변수로 사용, 프로그램 다운 오류 해결 exit code -1073740791 (0xc0000409)
            for ticker, prices in self.all_prices.items():
                # i = self.current_tickers.index(ticker)
                # i = self.tickers.index(ticker)
                i = list(self.all_prices.keys()).index(ticker)

                item_0 = self.tickerTableList.item(i, 0)
                item_0.setText(ticker)
                item_1 = QTableWidgetItem()
                item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_1.setData(Qt.DisplayRole, float(prices['closing_price'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 1, item_1)
                item_2 = QTableWidgetItem()
                item_2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_2.setData(Qt.DisplayRole, float(prices['fluctate_rate_24H'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 2, item_2)
                item_3 = QTableWidgetItem()
                item_3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                item_3.setData(Qt.DisplayRole, float(prices['acc_trade_value_24H'])) #숫자로 설정 (정렬을 위해)
                self.tickerTableList.setItem(i, 3, item_3)

                eu_ticker = eu_ticker + ',' + ticker
                # print(ticker)
            #
            # print(len(self.current_tickers))
            # print('initialized')
            # print(eu_ticker)
            pass


    def closeEvent(self, event):
        self.tl.close()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    tl = TickerlistWidget()
    tl.show()
    exit(app.exec_())
