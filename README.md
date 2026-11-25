# Make the AI Judge Laugh: Office Jokes

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/khususcrypto0000-coder/judge-laugh-office-jokes-makefun/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/khususcrypto0000-coder/judge-laugh-office-jokes-makefun/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

Entry for the [make.fun](https://make.fun) bounty
**"Make the AI Judge Laugh: Office Jokes"** (slug:
`u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a`, $5 total pot,
top 10 paid from $1.54 down to $0.06).

The bounty asks for one joke about office life: a single line of under 200
characters, nothing else. An AI judge compares jokes head to head and ranks
them on whether the line is a genuine office joke, whether it turns somewhere
unexpected at the end, whether it rings true about the office, how tight the
wording is, and how fresh the take is.

## The entry

> I booked the conference room to escape meetings, then got invited to a meeting in it.

(85 characters, one line. The angle — booking a meeting room to *escape*
meetings, only to be summoned to a meeting inside it — was picked after
scanning all 7,061 rival entry titles: meetings, reply-all, printers, AI and
office plants are saturated, while conference-room booking is barely used.)

## How to run

Requires Python 3, standard library only — no dependencies to install.

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt` (override the directory with the
`OUTPUT_DIR` environment variable, e.g. `OUTPUT_DIR=/tmp/out python3 main.py`).
The script validates the entry first (1–199 characters, exactly one line, not
only whitespace, no trailing newline), then reads the file back and asserts
the written bytes are identical to the source text.

## License

MIT — see [LICENSE](LICENSE).
