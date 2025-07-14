# zm00 

Small commands that make my life better.

## Tools 

### Calendar

```
❯ zm c

      2025年7月

Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31   
```

### Stats (Japanese government)


```
❯ zm00 r                          
                                           直近の政府統計公表スケジュール                                           
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ 日付             ┃ 所管             ┃ 統計                                                          ┃ 統計コード ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 2025-07-14 08:50 │ 内閣府           │ 機械受注統計調査 令和7年(5月実績)                             │ 00100401   │
│ 2025-07-14 13:30 │ 経済産業省       │ 経済産業省生産動態統計調査 ２０２５年( ５月分 確報)           │ 00550200   |
```

### Math tools

❯ zm00 is-prime 123
False

zm00 on  master [!?] is 📦 v0.1.1 via 🐍 v3.13.5 
❯ zm00 is-prime 127
True


## Install

### Try without really installing it

```
uvx git+https://github.com/kenjisato/zm00 c
```


### Ready to install?

Install it with [uv](https://docs.astral.sh/uv/) 

```
uv tool install git+https://github.com/kenjisato/zm00 --reinstall
```

or with [pipx](https://pipx.pypa.io/stable/).

### Uninstall

```
uv tool uninstall zm00
```

