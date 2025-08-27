labels: Projects
        Blog
created: 2023-01-21T13:15
modified: 2025-08-27T10:56
place: Bangkok, Thailand

# Cipher - a backtesting framework

![cipher bt](cipher_wide.jpeg)

[GitHub](https://github.com/nanvel/cipher-bt)

[Documentation](https://cipher.nanvel.com/)

A trading strategy backtesting framework with focus on position adjustment and brackets.

It shapes domain models to be more suitable for backtesting. Instead of creating a market order and then position adjustments, the order (transaction) is a side effect of the position change. Limit orders are created and applied (transactions) once the price riches the brackets (stop loss or take profit).

## Backtest.sh

Generate cipher backtests for text prompts: [https://github.com/nanvel/backtestsh](https://github.com/nanvel/backtestsh)

![Demo](https://github.com/nanvel/backtestsh/releases/download/0.1.0/backtestsh.gif)


