# 23 November 2026, in one page

A front page for Monday 23 November 2026, drawn from that day's reporting.

`record.py` holds the day's stories, each verified against a newsroom's own
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
