labels: Draft
        Finance
        Crypto
        Trading
created: 2017-11-16T14:08
modified: 2021-10-09T16:53
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
- buy before the pay day (people accumulating from salaries)
- large volumes in ob attracts price (because large amounts can be bought/sold without impacting price)
- identify suply testing
- pullbacks on low volume - pull back if not supported
- two assets correlated, and then not - create short + long positions
- trend trading
- buy and hold
- trade on news
- When the price drops where low and stays there for some time - buy (chances to drop lower are lower then go much higher)
> Buy when there's blood in the streets,
> even if the blood is your own.
>
> Barron Rothschild
After a major decline, the risk of further decline diminishes while the opportunity for maximum profit increases.
- If an asset fails to make a higher high - sign of weakness
- Arbitrage between exchanges
- buy new tokens not yet listed on major exchanges
- use rich lists to understand accumulation/distribution by large accounts
- find sentiment by looking at orderbook - more buy orders/volums = bull (count only long time standing orders)
- identify iceberg / real orders in order books by how they behave when price hit them
- only buy when many other traders are buying (hiding in the crowd)
- if price moves too quickly - stop entering the market
- if the broader market falls quickly - stop buying
- know orders priority - FIFO or by size?
- always keep orders to catch spike
- monitor liquidations

Works:

- Trailing sell (trailing stop)
- Price/volume analysis

## Exchanges

[Local Bitcoins](https://localbitcoins.com/)
[Binance](https://www.binance.com/)
[Pancake Swap](https://pancakeswap.finance/)

## Brokers

[InteractiveBrokers](https://www.interactivebrokers.com/)

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
- [TrendSpider](https://trendspider.com/)

### Scalping

- [CScalp](https://fsr-develop.com/)
- [BookMap](https://bookmap.com/)

### Study

- [The Inner Circle Trader](https://www.youtube.com/user/InnerCircleTrader)
- [Babypips](https://www.babypips.com/)

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

If no weak is created, then this signals strong market sentiment in the direction of the closing price.

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

### Price action

Volume reveals whether the price action is valid or false.

Buying climax - when the market has moved sharply lower in a price waterfall and bearish trend,
supported by masses of volume. Wholesalers are buying and retail traders are panic selling.

Selling climax - at the top of a bull trend, where we see sustained high volumes.
Wholesalers are selling to retail traders and investors.

Phases (Charles Dow):
- accumulation
- public participation
- distribution

Smart money taking profits and selling to an increasingly eager public.

Wyckoff laws:
- The law of supply and demand (when demand is greater than supply, then prices will rise to meet this demand, and conversely when supply is greater than demand then prices will fall, with the over supply being absorbed as a result)
- The law of cause and effect (a small amount of volume activity will only result in a small amount of price action)
- The law of effort vs result (the price action on chart should reflect volume action)

Volume Price Analisys concepts:
- Accumulation
- Distribution
- Testing
- Selling Climax
- Buying Climax

Why markets move sideways:
- pending release of a fundamental news
- selling and buying climax (warehouses are either being filled or emptied by the insiders)
- run into old areas of price, where traders have been locked into weak positions in previous moves

SMA(50, 200) can become a support/resistance.

Divergence between volume and price: the volume of trading stops expanding and starts to shrink as the averages move to their final highs. Normally at the beginning of a move, the volume of trading continually grows. But then, at a certain point, the market makes new highs but the volume contracts.

Fibonacci retracement is a tool used to predict the pull-back of price after a period of growth based on a set of predetermined percentages: 23.6, 38.2, 50, 61.8, 78.6.

Fibonacci extension is a tool used to find targets for growth after a pull-back. Commonly used 161.8, 200.

## Order book

Large volume at price:
- often can be found on significant levels (round prices, support/resistance)
- large numbers of stop orders can be found behind large volumes (that can cause a price spike after the price is broken)
- makes send to put orders before large volumes, so there will be more chances for them to be executed
- makes sense to put stops behind large volumes, so there will be less chances for them to be executed
- price can be moved tovards large volumes by large players, and then they can consume large liquidity at good price and don't cause large price change
- large volumes can be removed or moved a bit (if the intension was just price manipulation without intent to buy/sell)
- large volumes can be executed with market order after removed from order book

## Risk management

Keep account at risk `~3-5%` per trade.
Account at risk = `((entry_price - stop_price) / stop_price) * quantity + fee`.
Sell asset gradually to reduce risk.
Let winners to run and cut losers.
Move stop (towards entry only) to reduce or remove risks later (ladder stop, trailing stop).

## Links

[Evidence-Based Technical Analysis](https://www.amazon.com/Evidence-Based-Technical-Analysis-Scientific-Statistical/dp/0470008741) by David Aronson
[Charting and Technical Analysis](https://www.amazon.com/Charting-Technical-Analysis-Fred-Mcallen/dp/1456468693) by Fred McAllen
[Investopedia](https://www.investopedia.com)
[Trading the Trends](https://www.amazon.com/Trading-Trends-Fred-McAllen/dp/1466323868) by Fred McAllen
[tradingview.com](https://www.tradingview.com/) - Network where active traders echange ideas to maximize profit
[An Altcoin Trader's Handbook](https://www.amazon.com/Altcoin-Traders-Handbook-Nik-Patel/dp/198617011X) by Nik Patel
[A Complete Guide to Volume Price Analysis by Anna Coulling](https://www.amazon.com/Complete-Guide-Price-Analysis-ebook/dp/B00DGA8LZC/)
