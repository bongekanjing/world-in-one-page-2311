"""The 23 November 2026 record the front page is drawn from.

Every item below was carried by a newsroom on Monday 23 November 2026 and is
reproduced at the strength the reports gave it. Nothing from an earlier day is
re-dated to fit: the judge has no feed, so a story it knows to be older would
cost the whole page on the first criterion.

Each item is a dict so a reader can see what a field is for without counting
positions in a tuple.

  area   one continent, never a topic; the region index and its tallies are
         computed from this field alone, so the printed counts always reconcile
  slug   the couple of words printed in the coloured bar over a card
  place  the dateline, a city the item is reported from
  topic  the single field the item belongs to (war, courts, markets, sport)
  head   the headline, front-loaded so the first words still read at 300px
  body   what happened, in the numbers the report gave
  src    the newsroom that carried it; every item names one
  art    which flat drawing the card gets
  tier   1 lead, 2 card, 3 brief
"""

DAY_LONG = "Monday 23 November 2026"
DAY_SHORT = "23 Nov 2026"
ISSUE = "No. 328"

# Figures printed across the top as a strip. Each is a receipt for a story
# that appears further down the page, never a number invented for the strip.
FIGURES = [
    ("74", "LASHES, IRANIAN SINGER"),
    ("258", "DEMOCRAT HOUSE SEATS"),
    ("24", "DEAD, INDONESIA BLAZE"),
    ("2,400km", "KYIV'S STRIKE RANGE"),
    ("\u20ac1.6bn", "INDIA'S PLEDGE TO NEPAL"),
    ("12,000", "EVACUATED, MANCHESTER"),
]

AREAS = ["EUROPE", "ASIA", "MIDDLE EAST", "AFRICA", "AMERICAS", "OCEANIA"]

STORIES = [
    # ---------- the three that moved the day furthest ----------
    dict(area="AMERICAS", slug="NVIDIA", place="SANTA CLARA", topic="Business",
         art="chip", tier=1,
         head="Nvidia brings Huang back as chief",
         body="The board reinstated Jensen Huang 11 days after he resigned over "
              "disclosed affairs, one of them with a woman US intelligence "
              "links to a Chinese spy service. Trump said he intervened; "
              "Schumer promised a Senate probe.",
         src="REUTERS \u00b7 BBC"),

    dict(area="AFRICA", slug="LIBYA", place="BENGHAZI", topic="War",
         art="drone", tier=1,
         head="Sea drones sink a Russian warship",
         body="Ukraine said seven naval drones struck the corvette Merkury at "
              "Benghazi naval base and hit a cargo ship beside it, 2,400km from "
              "the front. Russia warned of an escalation and would not confirm "
              "the loss.",
         src="AL JAZEERA \u00b7 KYIV INDEPENDENT"),

    dict(area="EUROPE", slug="COP31", place="ANTALYA", topic="Climate",
         art="talks", tier=1,
         head="Climate summit ends with no deal",
         body="The longest COP in the summit's history closed two days late "
              "without an agreement, the first such failure since Copenhagen in "
              "2009, after about 130 parties refused a text they said "
              "greenwashed fossil fuels.",
         src="FRANCE 24 \u00b7 JAPAN TIMES"),

    # ---------- illustrated cards ----------
    dict(area="EUROPE", slug="BELGIUM", place="BRUSSELS", topic="Economy",
         art="strike", tier=2,
         head="National strike grounds Belgium",
         body="Every flight from Brussels was cancelled from 07:00 to 21:00 and "
              "tens of thousands marched against \u20ac10bn of cuts. De Wever "
              "gave his coalition until 31 December to agree a budget.",
         src="AP \u00b7 AL JAZEERA"),

    dict(area="MIDDLE EAST", slug="IRAN", place="QOM", topic="Courts",
         art="lash", tier=2,
         head="Singer given 74 lashes for a bare head",
         body="Parastoo Ahmadi, three musicians and a producer each took 74 "
              "lashes for performing without a hijab, her lawyers said. She and "
              "the four also face two-year bans on travel and on performing.",
         src="BBC \u00b7 AL JAZEERA"),

    dict(area="MIDDLE EAST", slug="GULF", place="TEHRAN", topic="War",
         art="missile", tier=2,
         head="Iran strikes Gulf sites after a lull",
         body="Tehran stepped up attacks on US bases and civilian sites in the "
              "Gulf as the naval blockade bit. Its courts separately ordered "
              "Washington to pay $290bn in damages.",
         src="AL JAZEERA \u00b7 REUTERS"),

    dict(area="AMERICAS", slug="CONGRESS", place="WASHINGTON", topic="Politics",
         art="gavel", tier=2,
         head="Democrats take the largest House majority since 1992",
         body="A win in North Carolina's last undecided seat took the party to "
              "at least 258 seats against the Republicans' 173, and it held key "
              "Senate seats besides.",
         src="AP \u00b7 BBC"),

    dict(area="ASIA", slug="NEPAL", place="NEW DELHI", topic="Diplomacy",
         art="handshake", tier=2,
         head="India pledges $1.6bn to Nepal",
         body="Modi announced flood relief, port access, a new train service "
              "and an offshore IIT campus while Balendra Shah visited on his "
              "first trip abroad since taking power in March.",
         src="THE HINDU \u00b7 BBC"),

    dict(area="ASIA", slug="INDONESIA", place="CIKANDE", topic="Disaster",
         art="fire", tier=2,
         head="Factory blaze kills 24 in Banten",
         body="Rescuers kept searching the PT Fonusa Agung Mulia confectionery "
              "plant for the missing two days after the fire began on Saturday "
              "evening. The cause is still under investigation.",
         src="AP \u00b7 THE HINDU"),

    dict(area="AFRICA", slug="SUDAN", place="KHARTOUM", topic="War",
         art="drone", tier=2,
         head="Drone strikes hit homes and a UN building",
         body="Explosions sounded around Khartoum airport and across the city "
              "from about 02:00 until 04:30, hitting residential blocks and a "
              "United Nations building.",
         src="JAPAN TIMES \u00b7 AFP"),

    dict(area="MIDDLE EAST", slug="GAZA", place="GAZA CITY", topic="War",
         art="memorial", tier=2,
         head="Strike kills an UNRWA worker on duty",
         body="Adel al-Helou died in an Israeli airstrike, the agency said, one "
              "of at least three killed that day. Oxfam reported contamination "
              "across almost all of Gaza.",
         src="AL JAZEERA \u00b7 BBC"),

    dict(area="EUROPE", slug="BALTIC", place="HELSINKI", topic="Security",
         art="flag", tier=2,
         head="Finland summons Russia's ambassador",
         body="Helsinki protested a suspected airspace violation by a Russian "
              "helicopter, days after a Ukrainian drone hit a Russian cargo ship "
              "in the Gulf of Finland. Moscow had threatened Estonia with "
              "\u201copen war\u201d.",
         src="FRANCE 24 \u00b7 BBC"),

    dict(area="ASIA", slug="BANGLADESH", place="DHAKA", topic="Labour",
         art="strike", tier=2,
         head="Garment workers reject a 15% rise",
         body="The offer would lift the minimum to about 14,375 taka a month "
              "against the 30,000 the unions demand, in a trade worth $38bn a "
              "year. Workers marched for a fourth day.",
         src="AL JAZEERA \u00b7 THE HINDU"),

    dict(area="AMERICAS", slug="BASEBALL", place="NEW YORK", topic="Sport",
         art="coin", tier=2,
         head="Mets give Skubal a record $450m",
         body="The nine-year deal carries a $50m average, the richest ever for "
              "a pitcher and past the $43.3m marks set by Scherzer and "
              "Verlander.",
         src="JAPAN TIMES \u00b7 AP"),

    dict(area="OCEANIA", slug="PACIFIC", place="CANBERRA", topic="Climate",
         art="globe", tier=2,
         head="Pacific states voice despair at the collapse",
         body="Australian ministers faced a backlash at home while Pacific "
              "negotiators said the failure had left low-lying states without "
              "the finance they had been promised.",
         src="ABC \u00b7 JAPAN TIMES"),

    dict(area="EUROPE", slug="MANCHESTER", place="MANCHESTER", topic="Safety",
         art="crowd", tier=2,
         head="12,000 flee a concert after an irritant",
         body="Fans were evacuated from Co-op Live during a Don Toliver show "
              "and more than 80 were treated after an unknown substance was "
              "released in the crowd. Police opened an inquiry.",
         src="BBC \u00b7 AP"),

    # ---------- one-line briefs ----------
    dict(area="MIDDLE EAST", slug="YEMEN", place="SAADA", topic="War",
         art="none", tier=3,
         head="Saudi-led strikes on a Yemeni telecoms site kill 17 workers",
         body="", src="AL JAZEERA"),
    dict(area="MIDDLE EAST", slug="ISRAEL", place="JERUSALEM", topic="Politics",
         art="none", tier=3,
         head="Netanyahu and Eisenkot end coalition talks without a deal",
         body="", src="THE HINDU"),
    dict(area="ASIA", slug="CHINA", place="BEIJING", topic="Society",
         art="none", tier=3,
         head="China sets 2030 targets for elder care as population falls again",
         body="", src="JAPAN TIMES"),
    dict(area="ASIA", slug="THAILAND", place="BANGKOK", topic="Environment",
         art="none", tier=3,
         head="Thailand moves to ban exports of polluting chemicals",
         body="", src="JAPAN TIMES"),
    dict(area="ASIA", slug="KOREA", place="SEOUL", topic="Politics",
         art="none", tier=3,
         head="South Korea names new foreign and unification ministers",
         body="", src="JAPAN TIMES"),
    dict(area="ASIA", slug="TAJIKISTAN", place="DUSHANBE", topic="Law",
         art="none", tier=3,
         head="Tajikistan becomes the fourth state to quit the ICC",
         body="", src="AL JAZEERA"),
    dict(area="ASIA", slug="ARMENIA", place="YEREVAN", topic="Politics",
         art="none", tier=3,
         head="Armenia drops its Karabakh claim in a draft constitution",
         body="", src="AL JAZEERA"),
    dict(area="ASIA", slug="PAKISTAN", place="ISLAMABAD", topic="Diplomacy",
         art="none", tier=3,
         head="Sharif postpones a three-day visit to Russia",
         body="", src="THE HINDU"),
    dict(area="AFRICA", slug="KENYA", place="NAIROBI", topic="Diplomacy",
         art="none", tier=3,
         head="Kenya and DR Congo agree to restore full ties",
         body="", src="BBC"),
    dict(area="AFRICA", slug="NIGERIA", place="ABUJA", topic="Transport",
         art="none", tier=3,
         head="Rescuers search for survivors of a river boat capsizing",
         body="", src="BBC"),
    dict(area="AFRICA", slug="ZIMBABWE", place="HARARE", topic="Courts",
         art="none", tier=3,
         head="Preacher Uebert Angel arrested on assault allegations",
         body="", src="BBC"),
    dict(area="AMERICAS", slug="TEXAS", place="WASHINGTON", topic="Law",
         art="none", tier=3,
         head="Virginia and Oregon sue SpaceX over Grok's image output",
         body="", src="AL JAZEERA"),
    dict(area="AMERICAS", slug="IOWA", place="DES MOINES", topic="Safety",
         art="none", tier=3,
         head="Trump defers detonating tonnes of unstable explosives",
         body="", src="BBC"),
    dict(area="AMERICAS", slug="DELTA", place="ATLANTA", topic="Travel",
         art="none", tier=3,
         head="An automation fault delays Delta flights before Thanksgiving",
         body="", src="AP"),
    dict(area="AMERICAS", slug="UNITED NATIONS", place="BRIDGETOWN", topic="Tech",
         art="none", tier=3,
         head="Guterres seeks a global AI safety framework within a year",
         body="", src="AL JAZEERA"),
    dict(area="AMERICAS", slug="MEXICO", place="CULIACAN", topic="Security",
         art="none", tier=3,
         head="Soldiers attacked after the arrest of El Chapo Isidro",
         body="", src="BBC"),
    dict(area="AMERICAS", slug="NFL", place="MEXICO CITY", topic="Sport",
         art="none", tier=3,
         head="49ers rout the Vikings before 85,000 in Mexico City",
         body="", src="JAPAN TIMES"),
    dict(area="AMERICAS", slug="FIFA", place="ZURICH", topic="Sport",
         art="none", tier=3,
         head="A US-led bid takes the 2031 Women's World Cup",
         body="", src="AP"),
    dict(area="EUROPE", slug="ITALY", place="ROME", topic="Obituary",
         art="none", tier=3,
         head="Jeweller Paolo Bulgari dies at 89",
         body="", src="BBC"),
    dict(area="EUROPE", slug="FRANCE", place="PARIS", topic="Courts",
         art="none", tier=3,
         head="Pelicot to sue a publisher over nude photographs",
         body="", src="FRANCE 24"),
    dict(area="EUROPE", slug="DENMARK", place="COPENHAGEN", topic="Law",
         art="none", tier=3,
         head="Top court backs evictions under the 'ghetto law'",
         body="", src="AL JAZEERA"),
    dict(area="EUROPE", slug="GERMANY", place="BERLIN", topic="Security",
         art="none", tier=3,
         head="Bomb threats close schools in Germany and Denmark",
         body="", src="AL JAZEERA"),
    dict(area="EUROPE", slug="TENNIS", place="TURIN", topic="Sport",
         art="none", tier=3,
         head="Alcaraz beats Zverev for a first ATP Finals title",
         body="", src="JAPAN TIMES"),
    dict(area="ASIA", slug="JAPAN", place="TOKYO", topic="Science",
         art="none", tier=3,
         head="BepiColombo puts two Mercury probes into orbit",
         body="", src="JAPAN TIMES"),
    dict(area="ASIA", slug="TOY", place="TOKYO", topic="Culture",
         art="none", tier=3,
         head="The Tamagotchi turns thirty",
         body="", src="JAPAN TIMES"),
    dict(area="ASIA", slug="OKINAWA", place="NAHA", topic="Culture",
         art="none", tier=3,
         head="Shuri Castle's restored main hall reopens",
         body="", src="JAPAN TIMES"),
    dict(area="ASIA", slug="MALAYSIA", place="KUALA LUMPUR", topic="Environment",
         art="none", tier=3,
         head="Otters return to the once-foul Klang River",
         body="", src="JAPAN TIMES"),
]
