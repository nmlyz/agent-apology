# agent-apology

[![make.fun · u-kiencx-the-ai-agent-apology-one-liner-cfedd447](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![rank](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/nmlyz/agent-apology/rank.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![reward](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/nmlyz/agent-apology/reward.svg)](https://make.fun/bounty/u-kiencx-the-ai-agent-apology-one-liner-cfedd447?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

agent-apology writes one line to a text file: the message an AI agent sends its human right after it emailed the boss a draft marked DO NOT SEND. The line was picked from 36 candidates by pairwise judging against the brief — the agent's literal-minded fix for its own mistake, told in two clauses and closed on its strongest beat. The agent does not explain itself twice.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 95 characters, a single line, and ends on its strongest beat. The program holds the line as one constant and checks it against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-ai-agent-apology-one-liner-cfedd447)</sub>
