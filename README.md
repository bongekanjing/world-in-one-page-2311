# 23 November 2026, in one page

[![Competition](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![Rank](https://make.fun/badge/news-image-20261123/bongekanjing/world-in-one-page-2311/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![Reward](https://make.fun/badge/news-image-20261123/bongekanjing/world-in-one-page-2311/reward.svg)](https://make.fun/bounty/news-image-20261123)

A front page for Monday 23 November 2026, drawn from that day's reporting.
Entered in the [make.fun bounty](https://make.fun/bounty/news-image-20261123)
"Sum up 23 November's world news in one image".

`record.py` holds the day's stories, each checked against a newsroom's own
copy for 23 November 2026, and `render.py` draws them: a masthead that names
the day, six figures across the top, one dominant lead, two subordinate leads,
and a grid of stories whose row count is measured against the pixels left
before anything is painted, so the page cannot overrun.

Every number on the page is counted from the stories that are actually
printed. The region index is computed from what the grid accepted, so it can
never claim a story the paper does not carry, and breadth across all six
regions is enforced when the grid selects.

`page.png` is the rendered result; `main.py` copies it to `/output/entry.png`.
The program is deliberately a copy: the image is already decided, so no clock,
random seed or font fallback can make the two runs differ.
