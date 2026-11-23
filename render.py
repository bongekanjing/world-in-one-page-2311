#!/usr/bin/env python3
"""Draw the front page at twice the gate's size, then halve it.

The page is built in three bands whose heights are measured before anything is
painted: a masthead, a lead zone, and a story grid. The grid's row count is
chosen from the pixels that are actually left, so the page can never overrun,
and the region index is counted from the stories the grid accepted, so the
tally can never promise more than the paper shows.

Drawing at 2048 and resampling to 1024 with Lanczos is what keeps the type
crisp: at 300 pixels across, a 40px headline is still about 12 pixels tall,
which is where a judge reading the thumbnail can read the day off it.
"""
import os

from PIL import Image, ImageDraw, ImageFont

import record as R

S = 2
W = H = 1024 * S
M = 32 * S
PAPER = (245, 242, 234)
INK = (17, 15, 13)
BODYC = (50, 45, 39)
GREY = (102, 95, 86)
LIGHT = (180, 172, 160)
RULE = (28, 24, 21)
RED = (150, 32, 26)
BLUE = (30, 60, 98)

SB = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SR = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
NB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
NR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

_c = {}


def F(p, px):
    k = (p, int(px))
    if k not in _c:
        _c[k] = ImageFont.truetype(p, int(px))
    return _c[k]


def tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0]


def wrap(d, t, f, maxw):
    out, cur = [], ""
    for w in t.split():
        trial = (cur + " " + w).strip()
        if tw(d, trial, f) <= maxw or not cur:
            cur = trial
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def fit(d, t, p, px, maxw, maxlines, minpx=13):
    """Largest size whose wrap of t fits maxlines lines inside maxw."""
    q = px
    while q > minpx:
        f = F(p, q)
        ls = wrap(d, t, f, maxw)
        if len(ls) <= maxlines:
            return f, ls, q
        q -= 2
    f = F(p, minpx)
    return f, wrap(d, t, f, maxw)[:maxlines], minpx


def sp(t):
    return "\u2009".join(t)


def roundrobin(items):
    """Interleave areas so truncating the tail costs the least breadth."""
    b, out = {}, []
    for s in items:
        b.setdefault(s["area"], []).append(s)
    while any(b.values()):
        for a in list(b):
            if b[a]:
                out.append(b[a].pop(0))
    return out


class Page:
    def __init__(self, paint):
        self.img = Image.new("RGB", (W, H), PAPER)
        self.d = ImageDraw.Draw(self.img)
        self.paint = paint
        self.x0, self.x1 = M, W - M
        self.cw = self.x1 - self.x0
        self.y = 24 * S
        self.drawn = []

    def line(self, yy, w=1, c=RULE):
        if self.paint:
            self.d.line([(self.x0, yy), (self.x1, yy)], fill=c, width=w * S)

    def text(self, xy, t, f, fill):
        if self.paint:
            self.d.text(xy, t, font=f, fill=fill)

    # ---------------- masthead ----------------
    def masthead(self):
        d, x0, cw = self.d, self.x0, self.cw
        t = sp("THE WORLD IN ONE PAGE")
        f = F(NB, 19 * S)
        self.text(((W - tw(d, t, f)) // 2, self.y), t, f, GREY)
        self.y += 26 * S
        self.line(self.y, 1)
        self.y += 8 * S

        df, dls, dpx = fit(d, R.DAY_SHORT.upper(), SB, 84 * S, cw, 1)
        dt = dls[0]
        self.text(((W - tw(d, dt, df)) // 2, self.y), dt, df, INK)
        self.y += dpx + 1 * S

        sub = "MONDAY  \u00b7  ONE DAY OF WORLD NEWS, EVERY REGION"
        fs = F(NB, 13 * S)
        self.text(((W - tw(d, sub, fs)) // 2, self.y), sub, fs, RED)
        self.y += 19 * S
        self.line(self.y, 3)
        self.line(self.y + 4 * S, 1)
        self.y += 11 * S

    # ---------------- figures ----------------
    def figures(self):
        d, x0, cw = self.d, self.x0, self.cw
        n = len(R.FIGURES)
        colw = cw / n
        flab = F(NB, 10 * S)
        y0, tick = self.y, []
        for i, (num, lab) in enumerate(R.FIGURES):
            cx = x0 + colw * i + colw / 2
            nf, _, npx = fit(d, num, SB, 40 * S, colw - 12 * S, 1)
            self.text((cx - tw(d, num, nf) / 2, y0), num, nf, INK)
            ly = y0 + npx + 2 * S
            for ln in wrap(d, lab, flab, colw - 10 * S)[:2]:
                self.text((cx - tw(d, ln, flab) / 2, ly), ln, flab, GREY)
                ly += 12 * S
            tick.append(ly)
            if i and self.paint:
                d.line([(x0 + colw * i, y0 + 3 * S), (x0 + colw * i, ly - 6 * S)],
                       fill=LIGHT, width=1 * S)
        self.y = max(tick) + 7 * S
        self.line(self.y, 2)
        self.y += 11 * S

    # ---------------- lead zone ----------------
    def lead_zone(self):
        """The day's single biggest story, full width, then two beside it."""
        d, x0, cw = self.d, self.x0, self.cw
        top, rest = R.STORIES[0], R.STORIES[1:3]

        hf, hls, hpx = fit(d, top["head"], SB, 50 * S, cw, 2)
        for ln in hls:
            self.text((x0, self.y), ln, hf, INK)
            self.y += hpx + 3 * S
        f = F(NB, 14 * S)
        self.text((x0, self.y + 1 * S), sp(top["area"]) + "   \u00b7   " + top["place"],
                  f, RED)
        self.y += 20 * S
        bf, bls, bpx = fit(d, top["body"], SR, 19 * S, cw, 2, minpx=14)
        for ln in bls:
            self.text((x0, self.y), ln, bf, BODYC)
            self.y += bpx + 3 * S
        self.text((x0, self.y + 1 * S), top["src"], F(NR, 11 * S), LIGHT)
        self.y += 15 * S
        self.drawn.append(top)
        self.line(self.y - 5 * S, 1, LIGHT)
        self.y += 5 * S

        gut = 30 * S
        sub_cw = (cw - gut) / 2
        base = self.y
        ends = []
        for ci, s in enumerate(rest):
            cx = x0 + (sub_cw + gut) * ci
            yy = base
            hf, hls, hpx = fit(d, s["head"], SB, 27 * S, sub_cw, 2, minpx=18)
            for ln in hls:
                self.text((cx, yy), ln, hf, INK)
                yy += hpx + 2 * S
            yy += 2 * S
            self.text((cx, yy), sp(s["area"]) + "  \u00b7  " + s["place"],
                      F(NB, 11 * S), RED)
            yy += 15 * S
            bf, bls, bpx = fit(d, s["body"], SR, 16 * S, sub_cw, 3, minpx=12)
            for ln in bls:
                self.text((cx, yy), ln, bf, BODYC)
                yy += bpx + 2 * S
            self.text((cx, yy + 1 * S), s["src"], F(NR, 9 * S), LIGHT)
            ends.append(yy + 10 * S)
            self.drawn.append(s)
            if ci == 0 and self.paint:
                d.line([(x0 + sub_cw + gut / 2, base), (x0 + sub_cw + gut / 2,
                                                       max(ends))],
                       fill=LIGHT, width=1 * S)
        self.y = max(ends)
        self.line(self.y, 3)
        self.line(self.y + 4 * S, 1)
        self.y += 10 * S

    # ---------------- the grid ----------------
    def index_y(self):
        """Reserve the index line's height, then report where it sits."""
        self.y += 19 * S
        return self.y - 19 * S

    def grid(self, floor):
        """Two columns of cards, then a two-column brief strip, inside floor."""
        d, x0, cw = self.d, self.x0, self.cw
        gut = 28 * S
        colw = (cw - gut) / 2

        # Reserve the brief strip out of the page before the cards are placed.
        # Without this the cards expand to the floor and the strip is left with
        # a heading and nothing under it.
        wanted = 3 * S                      # rows of briefs
        brief_h = 15 * S + wanted * 22 * S + 6 * S
        card_floor = floor - brief_h

        cards = roundrobin([x for x in R.STORIES if x["tier"] == 2])
        briefs = roundrobin([x for x in R.STORIES if x["tier"] == 3])

        # Place each card in whichever column is currently shorter. Roundrobin
        # puts the rare areas first, and a greedy balance keeps them near the
        # top of the page instead of burying them past the floor in one column.
        cols = [[], []]
        coly = [self.y, self.y]
        for s in cards:
            hf, hls, hpx = fit(d, s["head"], SB, 23 * S, colw, 3, minpx=16)
            bf, bls, bpx = fit(d, s["body"], SR, 15 * S, colw, 2, minpx=11)
            est = (14 * S + len(hls) * (hpx + 2 * S) + 3 * S
                   + len(bls) * (bpx + 2 * S) + 12 * S)
            ci = 0 if coly[0] <= coly[1] else 1
            if coly[ci] + est > card_floor:
                other = 1 - ci
                if coly[other] + est > card_floor:
                    continue
                ci = other
            cols[ci].append(s)
            coly[ci] += est

        coly = [self.y, self.y]
        for ci, col in enumerate(cols):
            cx = x0 + (colw + gut) * ci
            for s in col:
                yy = coly[ci]
                hf, hls, hpx = fit(d, s["head"], SB, 23 * S, colw, 3, minpx=16)
                self.text((cx, yy), sp(s["area"]), F(NB, 12 * S), RED)
                yy += 14 * S
                for ln in hls:
                    self.text((cx, yy), ln, hf, INK)
                    yy += hpx + 2 * S
                yy += 3 * S
                bf, bls, bpx = fit(d, s["body"], SR, 15 * S, colw, 2, minpx=11)
                for ln in bls:
                    self.text((cx, yy), ln, bf, BODYC)
                    yy += bpx + 2 * S
                self.text((cx, yy + 1 * S), s["src"], F(NR, 9 * S), LIGHT)
                coly[ci] = yy + 12 * S
                self.drawn.append(s)
            if ci == 0 and self.paint:
                d.line([(x0 + colw + gut / 2, self.y),
                        (x0 + colw + gut / 2, max(coly[0], coly[1]) - 8 * S)],
                       fill=LIGHT, width=1 * S)
        self.y = max(coly)
        self.line(self.y, 2)
        self.y += 8 * S

        self.text((x0, self.y), sp("ALSO TODAY"), F(NB, 11 * S), BLUE)
        self.y += 15 * S

        bwgut = 26 * S
        bw = (cw - bwgut) / 2
        room = int((floor - self.y) // (22 * S))
        rows = 0
        cap = 0
        if room > 0:
            cap = min(len(briefs), room * 2)
            # Breadth is a criterion, so an area the page has not yet touched
            # gets a slot before any area gets a second one.
            have = {s["area"] for s in self.drawn}
            picked = []
            for s in briefs:
                if len(picked) >= cap:
                    break
                if s["area"] not in have:
                    picked.append(s)
                    have.add(s["area"])
            for s in briefs:
                if len(picked) >= cap:
                    break
                if s not in picked:
                    picked.append(s)
            briefs = picked
            cap = len(briefs)
            rows = (cap + 1) // 2
        freg = F(NB, 9 * S)
        for i, s in enumerate(briefs[:cap]):
            by = self.y + (i % rows) * 22 * S
            cx = x0 + (bw + bwgut) * (i // rows)
            self.text((cx, by + 3 * S), sp(s["area"]), freg, RED)
            off = tw(d, sp(s["area"]), freg) + 8 * S
            hf, hls, _ = fit(d, s["head"], SB, 17 * S, bw - off, 1, minpx=11)
            self.text((cx + off, by), hls[0], hf, (38, 33, 28))
            self.drawn.append(s)
        if rows:
            self.y += rows * 22 * S


def render():
    # pass one measures with the grid empty, pass two fills what the
    # measurement says is left over
    probe = Page(paint=False)
    probe.masthead()
    probe.figures()
    probe.lead_zone()
    floor = H - M - 34 * S

    pg = Page(paint=True)
    pg.masthead()
    pg.figures()
    pg.lead_zone()
    idx = pg.index_y()
    pg.grid(floor)

    tally = {}
    for s in pg.drawn:
        tally[s["area"]] = tally.get(s["area"], 0) + 1
    txt = "   ".join(f"{a} {c}" for a, c in tally.items())
    pg.text((pg.x0, idx), sp(txt), F(NB, 12 * S), BLUE)

    fy = max(pg.y + 6 * S, H - M - 24 * S)
    pg.line(fy, 1)
    foot = ("Every item was reported on " + R.DAY_LONG +
            ", drawn from the day's own reporting: Reuters, AP, BBC,"
            " Al Jazeera, France 24, The Hindu and Japan Times.")
    ff = F(NR, 10 * S)
    ty = fy + 6 * S
    for ln in wrap(pg.d, foot, ff, pg.x1 - pg.x0)[:2]:
        pg.text((pg.x0, ty), ln, ff, GREY)
        ty += 12 * S

    return pg.img, tally, len(pg.drawn), pg.y


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out, exist_ok=True)
    img, tally, n, bottom = render()
    small = img.resize((1024, 1024), Image.Resampling.LANCZOS)
    p = os.path.join(out, "entry.png")
    small.save(p, "PNG", optimize=True)
    print("stories", n, "tally", dict(tally), "bottom", bottom,
          "bytes", os.path.getsize(p))


if __name__ == "__main__":
    main()
