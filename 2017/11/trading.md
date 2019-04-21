labels: Draft
        Finance
        Crypto
        Trading
created: 2017-11-16T14:08
modified: 2019-04-21T14:28
place: Phuket, Thailand
comments: true

# Trading

> The market does not run on chance or luck.
> Like the battlefield, it runs on probabilities and odds.
>
> David Dreman

[TOC]

[Trading vocabulary](/2018/07/trading-vocabulary)
[Cryptocurrency exchanges](/2018/07/cryptocurrency-exchanges)

## Ideas

Doesn't work:

- Buy while price moves down and sell when moves up (
  some times doesn't move up, takes long time,
  requires a lot of base currency that will be locked most of time,
  small profit as trade small pieces)

To try:

- Buy on surges
- Bollinger Band (deviation from moving averages)
- Volume-price charts
- watchers on rich list

Works:

- Trailing sell (trailing stop)
- Price/volume analysis

## Statistics sources

[Coinmarketcap](https://coinmarketcap.com)
[CoinGecko](https://www.coingecko.com/en)
[BitScreener](https://bitscreener.com) - further chart analysis, recent related news.
[AtomSignal](https://www.atomsignal.com) - excanges monitiring, tracking buy and sell walls.
[WenMoon](http://wenmoon.com) - useful for research.
[BitcoinTalk](https://bitcointalk.org) - new altcoin announcements, fundamental analysis.

## Instruments

### Charting

- [Coinigy](https://www.coinigy.com/) - great number of cryptocurrency exchanges
- [TradingView](https://uk.tradingview.com/)
- [BitcoinWisdom](https://bitcoinwisdom.com/) - clear and user-friendly

## TA categories

TA categories:

- Objective
- Subjective

Subjective:

- classical chart pattern analysis
- hand-drawn trend lines
- Elliott Wave principle
- Gann patterns
- Magic T's

## Using bots

Finding patterns (chart formations).
Finding a better pair/a chain of pairs.
Placing forward.
Relying on signals.
Notifying of changes.
Using higher hights and higher lows to find primary trend.
If thend brokes, probably, something changed and we need to correct the strategy.

Bot trading strategies:

- Scalping strategy
- MACD strategy
- Stick it on rise

Bot examples:

- https://github.com/gazbert/bxbot
- Gunbot
- Leonardo (simpler than Gunbot)
- DA POWERPLAY

> Let’s say I bought 10 bitcoins, and I want to sell them if the price reaches $1200. This can be done at exchanges already, of course. But using the bot, I can set it up to sell at $1200, buy back at $1000 and sell it all again at $1100. So I am building up a sequence of ordering events that must take place, and I define the exact target prices on it.

[Open source trading platforms](http://www.traderslaboratory.com/forums/tools-trade/11086-open-source-trading-platforms-master-list.html).

Sources:

- [The Bots That Make Money (Or Lose It) for You While You Sleep](https://bitcoinmagazine.com/articles/the-bots-that-make-money-or-lose-it-for-you-while-you-sleep-1483555808/)
- https://medium.com/@joeldg/an-advanced-tutorial-a-new-crypto-currency-trading-bot-boilerplate-framework-e777733607ae

### Why bot trading doesn't work well

Short - because of exchange fees.

If trade fast - there are small margins.
So if we sell with 0.6% profit, and pay 2 * 0.25% (for Bittrex), we have only 0.1% left.
That is the case when the trade was profitable.
In case of negative result: 2 * 0.25% + 0.6% - 1.1% lost.
So roughly for each fail we should have 11 wins at least to be profitable.

### Projects on GitHub

- https://github.com/deependersingla/deep_trader - uses ml
- https://github.com/pirate/bitcoin-trader - nice idea about small buys
- https://github.com/CryptoSignal/crypto-signal

## Testing

Backtest - test on historical data.

> Historical success is a necessary but not a sufficient condition for concluding that a method has predictive power and, therefore, is likely to be profitable in the future.
>
> Evidence-Based Technical Analysis by David Aronson

## Technical Analysis

> The charts don't lie.
>
> Charts really are the "foot-print of money". What some talking head on a financial news network might say becomes immaterial when you can look at a chart and see what the "money" is saying.
>
> Charting and Technical Analysis by Fred McAllen

Charts allow to see:

- past performance
- highs
- lows
- trends
- moving averages
- trading volume
- and more

Chart types:

- single line chart
- bar chart

### Candles

Shooting star candle - potential weakness. If see a few close - increasing bearish sentiment.

A long legged doji candle should always be validated by average, preferably high or ultra high volume.

If many people believe shooting star is bullish candle, it will be.

### Market rotation

More risky stocks are sold and the money is moved into safer stocks.
Is is not because the safer stocks have room to advance, but because they are likely to hold their value better in an economic down-turn. 

### Market weakness signs

Early signs:

- Lower volume on advances
- Higher volume on declines
- Inability to make higher highs
- Primary trend line broken
- DMA broken

Trend change signs:

- Lower highs, lower lows
- Higher volume on declines
- Low volume on advances

## Links

[Evidence-Based Technical Analysis](https://www.amazon.com/Evidence-Based-Technical-Analysis-Scientific-Statistical/dp/0470008741) by David Aronson
[Charting and Technical Analysis](https://www.amazon.com/Charting-Technical-Analysis-Fred-Mcallen/dp/1456468693) by Fred McAllen
[Investopedia](https://www.investopedia.com)
[Trading the Trends](https://www.amazon.com/Trading-Trends-Fred-McAllen/dp/1466323868) by Fred McAllen
[tradingview.com](https://www.tradingview.com/) - Network where active traders echange ideas to maximize profit
[An Altcoin Trader's Handbook](https://www.amazon.com/Altcoin-Traders-Handbook-Nik-Patel/dp/198617011X) by Nik Patel
