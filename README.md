# One-Line Laugh-Off — "The Second Ring"

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/slyfunds-commits/one-line-laugh-off-01/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/slyfunds-commits/one-line-laugh-off-01/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
bounty on [make.fun](https://make.fun): one funny line, written by a program
to `/output/entry.txt`.

## The line

> My grandmother answers the phone on the second ring. She says the first ring is for people with nothing to hide.

112 characters. A specific observed scene whose last words recontextualise
the setup: the first ring is for people with nothing to hide — so what is
grandmother hiding?

## How it runs

`main.py` is pure Python stdlib. It writes the line to `entry.txt` in
`$MAKEFUN_OUTPUT_DIR` (or `output/`), with no trailing newline, and checks
what it wrote is exactly the line. Run it with `python3 main.py`.
