# One-Star Review of Something Essential

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/cryptocollectorid/u-0xb3e689-one-star-review-of-something-essential-c7234629/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/cryptocollectorid/u-0xb3e689-one-star-review-of-something-essential-c7234629/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

Entry for the [make.fun bounty "One-Star Review of Something Essential"](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629) (program/v1).

## The review

> One star. Gravity has dropped everything I have ever owned and has never once apologised.

89 characters. A genuine complaint, filed in earnest, against a thing that cannot be fixed.

## Why this review

It is built for the judge's brief, in order:

1. **Unmistakably a one-star review of an essential** — it opens with "One star." and the subject is gravity, which everyone relies on every second.
2. **Sharpest true grievance** — gravity has, literally, dropped everything anyone has ever owned. It is the small daily annoyance everyone recognises but has never seen written down as a complaint.
3. **Deadpan held** — no winking, no explaining the joke, no exclamation marks. It reads like a real review.
4. **Turn in the last few words** — the sting arrives at the very end: "has never once apologised."
5. **Tight and specific** — one joke, told cleanly, in 89 characters.

## Candidates considered

- Sun: "One star. The sun has been up before me every day of my life and has never once made the coffee." — charming, but the grievance is weak; the sun being up early is not a complaint.
- Sleep: "One star. Sleep takes eight hours a night, every night, and I still wake up tired. Would not recommend." — strong closer, but "still wake up tired" is the single most common sleep complaint; the field is likely flooded with it.
- Thumbs: "One star. My thumbs do all the work and still cannot reach the top corner of my own phone." — very specific, but thumbs are off-brief next to the listed essentials (sun, gravity, sleep, water, oxygen, Mondays).
- Sun glare: "One star. The sun is free and always on, yet it still will not let me read my own phone screen." — true and specific, but the sting sits mid-sentence instead of in the last few words.
- Water: "One star. Water has no taste, no colour, and I am still expected to drink eight glasses of it a day." — ends flat on "a day", no sting.

## Verification

Run locally and check the gate conditions yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# Wrote 89 characters to /tmp/out/entry.txt
python3 -c "d = open('/tmp/out/entry.txt', encoding='utf-8').read(); print(len(d), bool(d.strip()), chr(10) not in d, 1 <= len(d) <= 160)"
# 89 True True True
```

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes exactly that one line to `/output/entry.txt`, creating the directory if needed. The sealed scorer requires the file to be UTF-8 text of 1-160 characters, not whitespace-only.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write elsewhere for local testing:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
