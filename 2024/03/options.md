labels: Draft
        Finance
        Crypto
        Trading
created: 2024-03-18T19:39
modified: 2024-03-18T19:39
place: Bangkok, Thailand
comments: true

# Options

[TOC]

[Binance EU Options API](https://binance-docs.github.io/apidocs/voptions/en/#change-log)

Eutopean Style Options: can be exercised only at expiration.
American Style Options: can be exercised at any time prior to expiration.

Calls - options to buy.
Puts - options to sell.
Writing options = selling options.

Fees:

- transaction fee
- excercise fee

Strategies:

- Bying calls: bullish
- Selling calls: bearish (reading of position and receiving premium)
- Buying puts: bearish
- Selling puts: receiving premium and accumulating position in the asset
- Straddle: buying a Call and a Put Options of the same asset with identical Strike Prices and expiration dates
- Strangle: same as straddle, but Call and Put Options do not have the same Strike Prices
- Iron Condor
- [Butterfly](https://3commas.io/blog/butterfly-option-strategy)

Straddles work well when a trader believes an asset's price will move but is unsure in which direction so that they are protected regardless of the outcome. A strangle works well when an investor is certain of the direction of an asset's movement but would still like to hedge their position.

Spreads:
- Vertical spread - different strike price
- Horizontal spread - different expiration date
- Diagonal spread - both strike price and expiration dates are different
- bull call (basic vertical) - multi-leg call option strategy with both a right to buy and obligation to sell with the same expiration but different strikes
- bear put

Different strike price -> vertical spread.
Different expiration date -> horizontal spread.
Both -> diagonal spread.

## Greeks

**Delta**: the rate of change of the option’s price attributable to a given change in the price of the underlying instrument.
Positiove for calls (`0..1`) and negative for puts (`-1..0`).

**Gamma**: the rate of change of portfolio delta with a change in the underlying price.
A high value of gamma means that the delta is more sensitive to the share price changes and vice versa.
Gamma is always positive, and its value is highest when the option is near the money and close to expiration.
Puts and calls have equal gamma.

**Theta**: measures the sensitivity of the option value to a small change in calendar time.
Theta is usually negative for both a call and a put option as the expiration date gets nearer.

**Vega**: the sensitivity of a portfolio to a given small change in the assumed level of volatility.
The vega of both call and put options are equal and always positive.

**Rho**: the change in a portfolio with respect to a small change in the risk-free rate of interest.
Therefore, rho is positive for a call option and negative for a put option.

## Strategies

Variants:
- Long Call
- Covered Call
- Bull Call Spread
- Bear Put Spread
- Long Put
- Long Call (or Put) Batterfly
- Short Call (or Put) Batterfly
- Iron Condor
- Long Straddle
- Short Straddle
- Long Strangle
- Short Strangle
- Broken Wing Batterfly

[Options Trading Cheat-Sheet](https://www.valueray.com/cheatsheet/options)

### Novice

BASIC:
- Long Call
- Long Put

INCOME:
- Covered Call
- Cash-Secured Put

OTHER:
- Protective Put

### Intermediate

CREDIT SPREADS:
- Bull Put Spread
- Bear Call Spread

NEUTRAL:
- Iron Butterfly
- Iron Condor
- Long Put Butterfly
- Long Call Butterfly

CALENDAR SPREADS:
- Calendar Call Spread
- Calendar Put Spread
- Diagonal Call Spread
- Diagonal Put Spread

DEBIT SPREADS:
- Bull Call Spread
- Bear Put Spread

DIRECTIONAL:
- Inverse Iron Butterfly
- Inverse Iron Condor
- Short Put Butterfly
- Short Call Butterfly
- Straddle
- Strangle

OTHER:
- Collar

### Advanced

NAKED:
- Short Put
- Short Call

NEUTRAL:
- Short Straddle
- Short Strangle
- Long Call Condor
- Long Put Condor

RATIO SPREADS:
- Call Ratio Backspread
- Put Broken Wing
- Inverse Call Broken Wing
- Put Ratio Backspread
- Call Broken Wing
- Inverse Put Broken Wing

INCOME:
- Covered Short Straddle
- Covered Short Strangle

DIRECTIONAL:
- Short Call Condor
- Short Put Condor

LADDERS:
- Bull Call Ladder
- Bear Call Ladder
- Bull Put Ladder
- Bear Put Ladder

OTHER:
- Jade Lizard
- Reverse Jade Lizard

### Expert

RATIO SPREADS:
- Call Ratio Spread
- Put Ratio Spread

SYNTHETIC:
- Long Synthetic Future
- Short Synthetic Future
- Synthetic Put

ARBITRAGE:
- Long Combo
- Short Combo

OTHER:
- Strip
- Strap
- Guts
- Short Guts
- Double Diagonal

### Butterfly spreads

4 calls with the same expiry day:
- Higher OTM strike (buy)
- Middle ATM trike x2 (sell)
- Lower OTM strike (buy)

## Vocabulary

**Open interest**: most often associated with the futures and options markets, where the number of open contracts changes daily. Open interest is the number of options or futures contracts held by traders in active positions. These positions have been opened, but have not been closed out, expired, or exercised.

## Sources

- [Binance Options Trading Tutorial (Full Guide for Beginners)](https://www.youtube.com/watch?v=ZRr3Iest-6c)
- [Binance Options FAQ](https://www.binance.com/en/support/faq/crypto-derivatives?c=4&navId=4#19-43)
- [Visualizing Option Trading Strategies in Python](https://medium.datadriveninvestor.com/visualizing-option-trading-strategies-in-python-35bfa61151d9)
- [psstrat on GitHub](https://github.com/hashabcd/opstrat)
- [Binance contract specification](https://www.binance.com/kk-KZ/support/faq/binance-options-contract-specifications-cdee5d43b70d4d2386980d41786a8533)
- [OptionStrat](https://optionstrat.com/)
- [OptionStrat](https://www.youtube.com/@OptionStrat) on YouTube
