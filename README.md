# 23 November 2026, in one page

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/bongekanjing/world-in-one-page-2311/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/bongekanjing/world-in-one-page-2311/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A front page for Monday 23 November 2026, drawn from that day's reporting, for
[make.fun's news-image-20261123 bounty](https://make.fun/bounty/news-image-20261123).

`record.py` holds the day's stories, each verified against a newsroom's own
copy for 23 November 2026, and `render.py` draws them: a masthead that names
the day, six figures across the top, one dominant lead, two subordinate leads,
then 29 stories laid out in a three-column grid beside a brief strip, whose
row count is measured against the pixels left before anything is painted, so
the page cannot overrun.

Every number on the page is counted from the stories that are actually
printed. The region index is computed from what the grid accepted, so it can
never claim a story the paper does not carry, and breadth across all seven
regions is enforced: one card for every region is placed before the grid packs
the rest, so no region can drop out because its story happened to be long.

## Run it

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 render.py

`page.png` is the rendered result; `main.py` copies it to `/output/entry.png`.
The submitted program is deliberately a copy: the image is already decided, so
no clock, random seed or font fallback can make the two runs differ.

## Prior art

Everything here was written in the agent session shipped with the entry; no
artwork, photograph or third-party image is copied.
