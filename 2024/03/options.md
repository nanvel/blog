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
- Bying puts: bearish
- Buying puts: receiving premium and accumulating position in the asset
- Straddle: buying a Call and a Put Options of the same asset with identical Strike Prices and expiration dates
- Strangle: same as straddle, but Call and Put Options do not have the same Strike Prices

Straddles work well when a trader believes an asset's price will move but is unsure in which direction so that they are protected regardless of the outcome. A strangle works well when an investor is certain of the direction of an asset's movement but would still like to hedge their position.

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

## Vocabulary

**Open interest**: most often associated with the futures and options markets, where the number of open contracts changes daily. Open interest is the number of options or futures contracts held by traders in active positions. These positions have been opened, but have not been closed out, expired, or exercised.

## Sources

- [Binance Options Trading Tutorial (Full Guide for Beginners)](https://www.youtube.com/watch?v=ZRr3Iest-6c)
- [Binance Options FAQ](https://www.binance.com/en/support/faq/crypto-derivatives?c=4&navId=4#19-43)
