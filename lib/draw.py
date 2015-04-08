import sys
import os
import pandas.tools.plotting as plotting
import matplotlib.pyplot as plt
from matplotlib import font_manager
p = os.path.dirname(os.path.abspath(__file__))
if p in sys.path:
    pass
else:
    sys.path.append(p)
from ohlc_plot import OhlcPlot

class Draw():

    def __init__(self, stock, name, **kwargs):
        self.stock = stock
        self.name = name
        self.fontprop = font_manager.FontProperties(
            fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")

    def plot(self, stock_d, ewma, bbands,
             ret, rsi, mfi, ultosc,
             stoch, vr):

        plotting._all_kinds.append('ohlc')
        plotting._common_kinds.append('ohlc')
        plotting._plot_klass['ohlc'] = OhlcPlot

        fig = plt.figure(figsize=(10.24, 7.68))

        ax1 = fig.add_subplot(2, 1, 1)
        ret['ret_index'].plot(label="RET_INDEX",
                              color="b", ax=ax1)
        rsi['rsi9'].plot(label="RSI9",
                         color="g", ax=ax1)
        rsi['rsi14'].plot(label="RSI14",
                          color="r", ax=ax1)
        rsi['mfi'].plot(label="MFI",
                        color="c", ax=ax1)
        rsi['ultosc'].plot(label="UTLOSC",
                           color="m", ax=ax1)
        stoch['slowk'].plot(label="SLOWK",
                            color="y", ax=ax1)
        stoch['slowd'].plot(label="SLOWD",
                            color="k", ax=ax1)
        vr['v_ratio'].plot(label="VOLUME", kind='area',
                           color="#DDFFFF", ax=ax1)
        # stochf['fastk'].plot(label="FASTK")
        # stochf['fastd'].plot(label="FASTD")
        plt.legend(loc="best")

        ax2 = fig.add_subplot(2, 1, 2)
        stock_d.plot(kind='ohlc',
                     colorup='r', colordown='b',
                     ax=ax2)
        # sma['sma5'].plot(label="SMA5")
        # sma['sma25'].plot(label="SMA25")
        # sma['sma75'].plot(label="SMA75")
        ewma['ewma5'].plot(label="EWMA5",
                           color="k", ax=ax2)
        ewma['ewma25'].plot(label="EWMA25",
                            color="g", ax=ax2)
        ewma['ewma75'].plot(label="EWMA75",
                            color="r", ax=ax2)
        bbands['upperband'].plot(label="UPPER",
                                 color="c", ax=ax2)
        bbands['middleband'].plot(label="MIDDLE",
                                  color="m", ax=ax2)
        bbands['lowerband'].plot(label="LOWER",
                                 color="y", ax=ax2)
        plt.legend(loc="best")

        ret_index = round(ret.ix[-1, 'ret_index'])
        closed = int(stock_d.ix[-1, 'Adj Close'])
        open = int(stock_d.ix[-1, 'Open'])
        high = int(stock_d.ix[-1, 'High'])
        low = int(stock_d.ix[-1, 'Low'])
        stock_max = int(stock_d.ix[:, 'High'].max())
        stock_min = int(stock_d.ix[:, 'Low'].min())

        plt.xlabel("".join(
                   [self.name, '(', self.stock, ') ',
                    ' 初:',
                    str(open),
                    ' 高:',
                    str(high),
                    ' 安:',
                    str(low),
                    ' 終:',
                    str(closed),
                    ' 最高:',
                    str(stock_max),
                    ' 最低:',
                    str(stock_min),
                    ' リターン:',
                    str(ret_index)
                    ]),
                   fontdict={"fontproperties": self.fontprop})
        plt.legend(loc="best")
        plt.show()
        plt.savefig("".join(["chart_", self.stock, ".png"]))
        plt.close()
