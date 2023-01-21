labels: Projects
        Blog
created: 2023-01-21T13:15
modified: 2023-01-21T13:15
place: Bangkok, Thailand

# Cipher - a backtesting framework

[GitHub](https://github.com/nanvel/cipher-bt)

[Documentation](https://cipher.nanvel.com/)

A trading strategy backtesting framework with focus on position adjustment and brackets.

It shapes domain models to be more suitable for backtesting. Instead of creating a market order and then position adjustments, the order (transaction) is a side effect of the position change. Limit orders are created and applied (transactions) once the price riches the brackets (stop loss or take profit).
