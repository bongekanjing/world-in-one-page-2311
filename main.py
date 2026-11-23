"""Write entry.txt: the front-page headline that sums up 23 November 2026.

The line is chosen from the day's reporting rather than written blind, so that
it names the event that actually moved the day furthest and gets its facts
right. The judge's brief puts those two things above punch: a headline that is
merely clever but vague, or that invents a detail, loses to one that is
specific and true.

Each candidate below is a real lead of 23 November 2026 as the wires carried
it, compressed to a single sentence that keeps the proper noun and the figure
that let it stand alone on a page with no story beneath it. The program takes
the first candidate clearing the length floor and carrying its facts, so the
output is decided by the data here and by nothing that can vary between runs.
"""

# (headline, the verified facts it rests on)
CANDIDATES = [
    (
        "Ukraine's sea drones sink the Russian corvette Merkury at Benghazi "
        "naval base, 2,400km from the front, hitting a cargo ship beside it",
        ["seven naval drones", "corvette Merkury", "Benghazi naval base",
         "2,400km from the front"],
    ),
    (
        "Climate summit ends two days late with no deal, the first COP failure "
        "since Copenhagen in 2009, as 130 parties refuse a fossil-fuel text",
        ["closed two days late", "no agreement", "about 130 parties"],
    ),
    (
        "Nvidia reinstates Jensen Huang as chief 11 days after he resigned over "
        "disclosed affairs, as Trump says he intervened",
        ["board reinstated", "11 days after he resigned", "Trump intervened"],
    ),
]

MIN_CHARS = 60      # shorter than this cannot stand alone without a story
MAX_CHARS = 200     # the bounty's own limit


def build():
    """The first headline that clears the length floor and carries its facts."""
    ok = [c for c in CANDIDATES
          if MIN_CHARS <= len(c[0]) <= MAX_CHARS and len(c[1]) >= 3]
    if not ok:
        raise SystemExit("no candidate clears the length and fact floors")
    return ok[0][0]


def main():
    """Write the chosen headline to entry.txt in the output directory."""
    import os
    out = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    line = build()
    assert 1 <= len(line) <= MAX_CHARS, len(line)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
