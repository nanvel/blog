labels: Projects
        Rust
        Blog
created: 2026-01-18T14:26
modified: 2026-01-18T14:26
place: Bangkok, Thailand

# Scalper-rs: a desktop app for scalping (trading) written in Rust

Repository: [https://github.com/nanvel/scalper-rs](https://github.com/nanvel/scalper-rs)

![scalper-rs ui](scalper-rs.png)

Usage:

- `Esc` - exit the app
- `Shift + Up/Down` - scale in/out
- `Shift + Left/Right` - change interval
- `1, 2, 3, 4` - choose lot multiplier
- `N` - reset aggressive volume and volume scale
- `+`` - submit a market buy order (use lot size * multiplier)
- `-`` - submit a marker sell order
- `0` (zero) - flat current position
- `C` - cancel all open orders
- `R` - reverse current position
- `Ctrl + LBC (Left Button Click)` - submit a limit order
- `Ctrl + Shift + LBC` - submit a stop order
- `Shift + LBC` - add a price alert (enable sound in config)
