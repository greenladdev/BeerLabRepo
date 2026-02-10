"""Static off-flavor dataset for the Beer Fault Finder app."""

OFF_FLAVORS = [
    {
        "slug": "acetaldehyde",
        "name": "Acetaldehyde",
        "nickname": "Green Apple",
        "description": "Fresh-cut green apple, raw pumpkin, or latex paint aroma from immature beer.",
        "common_styles": ["American Light Lager", "Cream Ale", "Kellerbier"],
        "avoidance": "Allow complete fermentation, avoid oxygen pickup post-fermentation, and give lager beers proper conditioning time.",
    },
    {
        "slug": "acetic-acid",
        "name": "Acetic Acid",
        "nickname": "Vinegar",
        "description": "Sharp vinegar-like sourness caused by oxidation and acetic bacteria.",
        "common_styles": ["Flanders Red", "Lambic", "Sour Blonde"],
        "avoidance": "Minimize oxygen exposure, sanitize cold-side equipment thoroughly, and keep sour and clean beer pipelines separate.",
    },
    {
        "slug": "solventy-esters",
        "name": "Solventy Esters",
        "nickname": "Nail Polish",
        "description": "Hot, solvent-like fruity notes often linked to stressed yeast and high fermentation temperature.",
        "common_styles": ["Belgian Golden Strong", "Saison", "High-Gravity Ale"],
        "avoidance": "Pitch healthy yeast at correct rates, control fermentation temperature ramps, and ensure adequate oxygen at pitch.",
    },
    {
        "slug": "diacetyl",
        "name": "Diacetyl",
        "nickname": "Buttery",
        "description": "Butter or butterscotch flavor from incomplete yeast cleanup or bacterial contamination.",
        "common_styles": ["English Bitter", "Czech Pilsner", "Scotch Ale"],
        "avoidance": "Use a diacetyl rest, avoid crashing too early, and maintain yeast health and sufficient contact time.",
    },
    {
        "slug": "dimethyl-sulfide",
        "name": "Dimethyl Sulfide",
        "nickname": "Cooked Corn",
        "description": "Sweet corn or cooked cabbage aroma from SMM conversion and weak boil-off.",
        "common_styles": ["American Lager", "Cream Ale", "Pale Lager"],
        "avoidance": "Maintain a vigorous uncovered boil, chill wort quickly, and avoid long hot-side stands after flameout.",
    },
    {
        "slug": "hydrogen-sulfide",
        "name": "Hydrogen Sulfide",
        "nickname": "Rotten Egg",
        "description": "Sulfur gas aroma that can linger from yeast stress or under-conditioned lager fermentation.",
        "common_styles": ["Helles", "Pilsner", "Schwarzbier"],
        "avoidance": "Use healthy lager yeast, control nutrient levels, and allow conditioning so sulfur can scrub out.",
    },
    {
        "slug": "mercaptan",
        "name": "Mercaptan",
        "nickname": "Burnt Rubber",
        "description": "Skunky rubber-like sulfur compounds from severe reduction stress or light damage.",
        "common_styles": ["Light-Struck Lager", "Old Kegged Beer", "Stressed Lager"],
        "avoidance": "Protect packaged beer from light, avoid prolonged yeast stress, and purge oxygen before packaging.",
    },
    {
        "slug": "oxidation",
        "name": "Oxidation",
        "nickname": "Papery",
        "description": "Stale cardboard, sherry, or honey-like aging notes from oxygen ingress.",
        "common_styles": ["Barleywine", "Old Ale", "Packaged IPA"],
        "avoidance": "Purge tanks and packages with CO2, avoid splashing during transfers, and keep dissolved oxygen low at packaging.",
    },
    {
        "slug": "lightstruck",
        "name": "Lightstruck",
        "nickname": "Skunky",
        "description": "Skunk-like thiol aroma produced when UV light reacts with hop compounds.",
        "common_styles": ["Green-Bottle Lager", "Pale Lager", "Dry-Hopped Pils"],
        "avoidance": "Use brown bottles, avoid direct sunlight and fluorescent exposure, and keep finished beer in darkness.",
    },
    {
        "slug": "astringency",
        "name": "Astringency",
        "nickname": "Tannic",
        "description": "Harsh mouth-drying sensation from husk tannins, high pH sparging, or over-extraction.",
        "common_styles": ["Over-Sparged IPA", "Strong Ale", "Lightly Hopped Blonde"],
        "avoidance": "Keep mash and sparge pH in range, avoid oversparging, and monitor grain bed temperatures.",
    },
    {
        "slug": "chlorophenol",
        "name": "Chlorophenol",
        "nickname": "Band-Aid",
        "description": "Medicinal plastic-like flavor from chlorine/chloramine reacting with phenols.",
        "common_styles": ["Wheat Beer", "Belgian Blonde", "Pale Ale"],
        "avoidance": "Treat brewing water with Campden tablets and avoid chlorine-based cleaners on cold-side gear.",
    },
    {
        "slug": "phenolic-smoke",
        "name": "Phenolic Smoke",
        "nickname": "Ashy",
        "description": "Ashtray or smoky medicinal notes from wild yeast, scorched material, or contamination.",
        "common_styles": ["Contaminated Saison", "Farmhouse Ale", "Smoked Porter"],
        "avoidance": "Deep-clean heat surfaces, verify yeast purity, and separate intentionally funky fermentations.",
    },
    {
        "slug": "isoamyl-acetate",
        "name": "Isoamyl Acetate",
        "nickname": "Banana Candy",
        "description": "Strong banana esters that become an off-note when out of balance.",
        "common_styles": ["Hefeweizen", "Belgian Dubbel", "High-Temp Ale"],
        "avoidance": "Control temperature and pitch rate to style targets; avoid underpitching high-gravity wort.",
    },
    {
        "slug": "ethyl-acetate",
        "name": "Ethyl Acetate",
        "nickname": "Pear Drops",
        "description": "Sweet solventy fruity note from stressed yeast or acetic acid bacteria.",
        "common_styles": ["Belgian Strong Ale", "Sour Ale", "Warm-Fermented IPA"],
        "avoidance": "Keep fermentations in temperature range and prevent oxygen ingress where bacteria can thrive.",
    },
    {
        "slug": "ethyl-hexanoate",
        "name": "Ethyl Hexanoate",
        "nickname": "Anise Apple",
        "description": "Apple/anise fruity ester that can dominate delicate beer profiles.",
        "common_styles": ["Belgian Blonde", "German Ale", "Session IPA"],
        "avoidance": "Use yeast strains matched to style and avoid unnecessary temperature spikes in early fermentation.",
    },
    {
        "slug": "ethyl-octanoate",
        "name": "Ethyl Octanoate",
        "nickname": "Waxy Fruit",
        "description": "Perfumed waxy fruit character from high ester expression.",
        "common_styles": ["Belgian Tripel", "Fruit-Forward IPA", "Strong Golden Ale"],
        "avoidance": "Provide sufficient oxygen and nutrients and avoid over-warm fermentation starts.",
    },
    {
        "slug": "fusel-alcohol",
        "name": "Fusel Alcohol",
        "nickname": "Hot Alcohol",
        "description": "Warming harsh spirit-like alcohol from yeast stress and excessive fermentation temperature.",
        "common_styles": ["Double IPA", "Imperial Stout", "Belgian Strong"],
        "avoidance": "Start cool, oxygenate properly, and use staged feeding for very high gravity ferments.",
    },
    {
        "slug": "autolysis",
        "name": "Autolysis",
        "nickname": "Meaty",
        "description": "Soy sauce or meaty rubber notes from yeast breakdown after long warm contact.",
        "common_styles": ["Aged Strong Ale", "Warm-Stored Homebrew", "Bottle-Conditioned Ale"],
        "avoidance": "Avoid prolonged warm storage on yeast cake and transfer or cool beer once fermentation is complete.",
    },
    {
        "slug": "metallic",
        "name": "Metallic",
        "nickname": "Coin-Like",
        "description": "Blood/iron or tinny flavor from equipment contact and water chemistry issues.",
        "common_styles": ["Pale Lager", "Blonde Ale", "Pilsner"],
        "avoidance": "Use passivated stainless equipment, avoid scratched non-food-safe metals, and evaluate source water.",
    },
    {
        "slug": "salty",
        "name": "Salty",
        "nickname": "Briny",
        "description": "Noticeable saltiness from high sodium brewing liquor or process additions.",
        "common_styles": ["Gose", "Experimental Sour", "Water-Adjusted Lager"],
        "avoidance": "Measure sodium contribution from all salts and avoid over-correction during water adjustments.",
    },
    {
        "slug": "soapy",
        "name": "Soapy",
        "nickname": "Dish Soap",
        "description": "Soap-like slick flavor from fatty acid breakdown, poor rinsing, or old hops.",
        "common_styles": ["Low-IBU Blonde", "Light Ale", "Aged Homebrew"],
        "avoidance": "Rinse cleaning agents fully, use fresh hops, and avoid long warm aging before consumption.",
    },
    {
        "slug": "caprylic",
        "name": "Caprylic Acid",
        "nickname": "Goaty",
        "description": "Waxy, goaty fatty-acid note from yeast stress and fatty acid accumulation.",
        "common_styles": ["Strong Ale", "Warm Lager", "Bottle-Aged Beer"],
        "avoidance": "Improve yeast nutrition and oxygen management and avoid prolonged warm maturation.",
    },
    {
        "slug": "isovaleric",
        "name": "Isovaleric Acid",
        "nickname": "Cheesy",
        "description": "Old cheese or sweaty aroma from oxidized aged hops.",
        "common_styles": ["Old IPA", "Stale Pale Ale", "Aged Hop Tea Beer"],
        "avoidance": "Store hops cold and oxygen-free, and rotate inventory aggressively.",
    },
    {
        "slug": "butyric",
        "name": "Butyric Acid",
        "nickname": "Rancid Butter",
        "description": "Rancid vomit-like aroma commonly linked to anaerobic bacterial contamination.",
        "common_styles": ["Contaminated Sour", "Improperly Purged Kettle Sour", "Spoiled Cask"],
        "avoidance": "Sanitize thoroughly, monitor souring pH progression, and avoid oxygen-starved contamination niches.",
    },
    {
        "slug": "lactic-overload",
        "name": "Lactic Overload",
        "nickname": "Yogurt Sour",
        "description": "Overly creamy yogurt-like acidity that masks malt and hop structure.",
        "common_styles": ["Berliner Weisse", "Kettle Sour", "Pastry Sour"],
        "avoidance": "Control souring duration and pH endpoint, and balance with fermentation attenuation and carbonation.",
    },
    {
        "slug": "enteric",
        "name": "Enteric",
        "nickname": "Fecal",
        "description": "Fecal or sewage note from coliform contamination in early souring or poor sanitation.",
        "common_styles": ["Raw Ale", "Unboiled Wort Sour", "Wild Ales"],
        "avoidance": "Boil wort when appropriate, sanitize equipment, and rapidly acidify souring wort to safe pH.",
    },
    {
        "slug": "acetoin",
        "name": "Acetoin",
        "nickname": "Creamy",
        "description": "Mild creamy/buttery note associated with diacetyl pathways and young fermentation.",
        "common_styles": ["Amber Lager", "English Ale", "Cream Ale"],
        "avoidance": "Allow full maturation and healthy yeast cleanup before crashing or packaging.",
    },
    {
        "slug": "thd",
        "name": "Trans-2-Nonenal",
        "nickname": "Wet Cardboard",
        "description": "Classic stale paper flavor created by oxidation of lipids.",
        "common_styles": ["Packaged Lager", "Old Pale Ale", "Shelf-Worn IPA"],
        "avoidance": "Reduce oxygen at every transfer and keep packaged beer cold through distribution.",
    },
    {
        "slug": "geraniol-overload",
        "name": "Geraniol Overload",
        "nickname": "Perfumy Floral",
        "description": "Perfume-like floral intensity from aggressive late hopping and biotransformation.",
        "common_styles": ["New England IPA", "Hazy Pale Ale", "Dry-Hopped Wheat"],
        "avoidance": "Calibrate dry-hop rates and timing and blend varieties for layered, not singular, aroma.",
    },
    {
        "slug": "grassiness",
        "name": "Grassiness",
        "nickname": "Fresh-Cut Grass",
        "description": "Green grassy, chlorophyll-like flavor from overlong contact with hops or vegetal matter.",
        "common_styles": ["Cold-Hopped Lager", "Hazy IPA", "Fresh Hop Ale"],
        "avoidance": "Limit hop contact time and separate beer from trub and hop sediment promptly.",
    },
    {
        "slug": "vegetal",
        "name": "Vegetal",
        "nickname": "Cooked Vegetables",
        "description": "Pea or mixed-vegetable notes from poor fermentation vigor or old hops.",
        "common_styles": ["Pale Lager", "Blonde Ale", "Session IPA"],
        "avoidance": "Use fresh ingredients, improve yeast vitality, and avoid warm storage of hops.",
    },
    {
        "slug": "sulfur-burn",
        "name": "Sulfur Burn",
        "nickname": "Matchstick",
        "description": "Struck match aroma from sulfur compounds that fail to dissipate.",
        "common_styles": ["Young Lager", "Cold-Fermented Pils", "Sparkling Ale"],
        "avoidance": "Provide adequate lagering time and venting where process allows sulfur release.",
    },
    {
        "slug": "smoke-creosote",
        "name": "Smoke Creosote",
        "nickname": "Tar",
        "description": "Tar-like harsh smoke from over-smoked malt or process contamination.",
        "common_styles": ["Rauchbier", "Smoked Porter", "Wood-Aged Stout"],
        "avoidance": "Moderate smoked malt percentages and keep direct combustion byproducts away from wort.",
    },
    {
        "slug": "overcarbonation-bite",
        "name": "Overcarbonation Bite",
        "nickname": "Carbonic",
        "description": "Sharp carbonic acid prickliness that reads as harshness.",
        "common_styles": ["Bottle-Conditioned Saison", "German Wheat", "Kegged IPA"],
        "avoidance": "Calibrate priming sugar and force-carb pressure with temperature-corrected carbonation targets.",
    },
    {
        "slug": "underattenuated-sweetness",
        "name": "Underattenuated Sweetness",
        "nickname": "Worty",
        "description": "Cloying wort-like sweetness from stalled fermentation.",
        "common_styles": ["Milk Stout", "Strong Ale", "NEIPA"],
        "avoidance": "Manage mash fermentability, pitch enough healthy yeast, and verify complete terminal gravity before packaging.",
    },
    {
        "slug": "harsh-bitterness",
        "name": "Harsh Bitterness",
        "nickname": "Rough Hop Bite",
        "description": "Coarse lingering bitterness often from over-sparging, hop burn, or polyphenol extraction.",
        "common_styles": ["West Coast IPA", "Double IPA", "Imperial Pils"],
        "avoidance": "Balance sulfate levels, avoid overloading early kettle additions, and reduce excessive dry-hop carryover.",
    },
    {
        "slug": "hop-burn",
        "name": "Hop Burn",
        "nickname": "Tongue Scrape",
        "description": "Raw particulate harshness from suspended hop matter in very fresh dry-hopped beers.",
        "common_styles": ["Hazy IPA", "Double Dry-Hopped Pale", "Triple IPA"],
        "avoidance": "Allow hop material to settle, use fining or centrifugation, and package after particulate reduction.",
    },
    {
        "slug": "yeasty",
        "name": "Yeasty",
        "nickname": "Bread Dough",
        "description": "Excessive yeast flavor and turbidity beyond style intent.",
        "common_styles": ["Bottle-Conditioned Ale", "Hefeweizen", "Unfiltered Lager"],
        "avoidance": "Improve clarification, cold-crash as appropriate, and avoid disturbing settled yeast at service.",
    },
    {
        "slug": "moldy",
        "name": "Moldy",
        "nickname": "Musty Basement",
        "description": "Damp mold character from contaminated grain, cork, or storage environments.",
        "common_styles": ["Barrel-Aged Sour", "Cellared Ale", "Corked Specialty Beer"],
        "avoidance": "Inspect raw materials, control cellar humidity, and retire contaminated porous packaging.",
    },
    {
        "slug": "earthy-dirt",
        "name": "Earthy Dirt",
        "nickname": "Damp Soil",
        "description": "Dirty earth-like notes from geosmin contamination or poor ingredient handling.",
        "common_styles": ["Farmhouse Ale", "Unfiltered Lager", "Well-Water Brew"],
        "avoidance": "Filter and test source water, store grains dry, and keep cold-side equipment sanitary.",
    },
    {
        "slug": "plastic",
        "name": "Plastic",
        "nickname": "Toy-Like",
        "description": "Plastic resin note from chlorophenols or packaging contamination.",
        "common_styles": ["Pale Ale", "Wheat Beer", "Blonde Ale"],
        "avoidance": "Dechlorinate water, use food-safe tubing only, and prevent sanitizer residue in finished beer paths.",
    },
    {
        "slug": "rubbery",
        "name": "Rubbery",
        "nickname": "Inner Tube",
        "description": "Rubber-like aroma from sulfur compounds or aging on unhealthy yeast.",
        "common_styles": ["Strong Lager", "Old Ale", "Bottle-Aged Stout"],
        "avoidance": "Avoid extended warm aging on yeast and improve fermentation health and conditioning schedules.",
    },
    {
        "slug": "medicinal",
        "name": "Medicinal",
        "nickname": "Antiseptic",
        "description": "Hospital-like medicinal flavor usually tied to phenolic contamination.",
        "common_styles": ["Pale Lager", "Belgian Ale", "Wheat Beer"],
        "avoidance": "Sanitize effectively, avoid chlorinated water, and isolate phenolic wild yeast from clean brewing lines.",
    },
    {
        "slug": "smoky-phenol",
        "name": "Smoky Phenol",
        "nickname": "Burnt Plastic",
        "description": "Burnt plastic and smoke character from phenolic contamination or scorched residues.",
        "common_styles": ["Dark Lager", "Smoked Ale", "Contaminated Strong Ale"],
        "avoidance": "Prevent scorching in kettle, clean heat surfaces, and verify yeast/pitching culture purity.",
    },
    {
        "slug": "aldehyde-complex",
        "name": "Aldehyde Complex",
        "nickname": "Raw Grain",
        "description": "A mix of grassy/grainy stale aldehydes from oxidation and incomplete maturation.",
        "common_styles": ["Young Lager", "Fast-Turnaround IPA", "Table Beer"],
        "avoidance": "Extend maturation windows and reduce oxygen ingress through closed-transfer practices.",
    },
    {
        "slug": "sulfur-dioxide",
        "name": "Sulfur Dioxide",
        "nickname": "Burning Sulfur",
        "description": "Pungent sulfur dioxide sensation that can overwhelm malt/hop expression.",
        "common_styles": ["Young White Wine Hybrid Beer", "Lager", "Fruit Sour"],
        "avoidance": "Improve fermentation ventilation and allow additional conditioning before release.",
    },
    {
        "slug": "chloroanisole",
        "name": "Chloroanisole",
        "nickname": "Cork Taint",
        "description": "Musty cork-like taint from chlorophenol conversion in corked or wood-aged products.",
        "common_styles": ["Corked Belgian Ale", "Barrel-Aged Sour", "Vintage Strong Ale"],
        "avoidance": "Use high-quality closures, avoid chlorinated cleaners near wood, and monitor cellar microflora.",
    },
    {
        "slug": "leathery-oxidation",
        "name": "Leathery Oxidation",
        "nickname": "Old Leather",
        "description": "Aged leathery stale character from prolonged oxidative storage.",
        "common_styles": ["Old Ale", "Stock Ale", "Aged Barleywine"],
        "avoidance": "Package with low oxygen, keep storage cool, and rotate stock by freshness targets.",
    },
    {
        "slug": "jammy-overripe",
        "name": "Jammy Overripe",
        "nickname": "Overripe Fruit",
        "description": "Overripe fruit esters that become cloying and out of balance.",
        "common_styles": ["Belgian Dark Strong", "Fruit Beer", "Imperial IPA"],
        "avoidance": "Use temperature-controlled fermentation and avoid severe yeast stress from underpitching.",
    },
    {
        "slug": "cereal-stale",
        "name": "Cereal Stale",
        "nickname": "Stale Cereal",
        "description": "Dry stale cereal flavor from malt oxidation and long warm storage.",
        "common_styles": ["Light Lager", "Cream Ale", "Session Blonde"],
        "avoidance": "Protect crushed malt from oxygen and humidity and package finished beer promptly.",
    },
]


FAMILY_RULES = {
    "sulfur": ("sulfur", "sulphur", "dms", "mercaptan", "rotten egg", "skunky", "matchstick"),
    "oxidation": ("oxidation", "oxidized", "papery", "cardboard", "stale", "trans-2-nonenal", "sherry"),
    "ester": ("ester", "isoamyl", "ethyl", "banana", "pear", "fruity", "overripe"),
}

STAGE_RULES = {
    "mash_boil": ("boil", "wort", "sparge", "mash", "kettle", "chill", "flameout", "hot-side"),
    "fermentation": ("fermentation", "yeast", "attenuation", "pitch", "conditioning", "lagering", "diacetyl"),
    "packaging": ("package", "packaging", "bottle", "keg", "shelf", "light", "oxygen", "transfer"),
}

FAMILY_CAUSES = {
    "sulfur": [
        "Yeast stress, nutrient imbalance, or insufficient conditioning time",
        "Cold-side contamination in sulfur-prone processes",
        "Poor venting/conditioning before packaging",
    ],
    "oxidation": [
        "Excess oxygen pickup during transfers or packaging",
        "Warm storage and extended shelf time",
        "Insufficient CO2 purging of vessels and packages",
    ],
    "ester": [
        "Warm fermentation and yeast stress",
        "Underpitching or insufficient oxygen at pitch",
        "Strain/style mismatch for intended flavor balance",
    ],
    "other": [
        "Process control drift (temperature, pH, timing)",
        "Ingredient freshness and handling issues",
        "Inconsistent sanitation or cleaning residue",
    ],
}

STAGE_CHECKS = {
    "mash_boil": [
        "Review mash/sparge pH and run-off limits",
        "Confirm vigorous uncovered boil and rapid chilling",
        "Check hot-side contact surfaces for scorching",
    ],
    "fermentation": [
        "Verify pitch rate, oxygenation, and yeast vitality",
        "Audit fermentation temperature profile",
        "Confirm terminal gravity and maturation completion",
    ],
    "packaging": [
        "Measure dissolved oxygen at packaging",
        "Verify CO2 purging and closed-transfer integrity",
        "Check light exposure and storage temperatures",
    ],
}

SEVERITY_HINTS = {
    "high": ("vomit", "fecal", "band-aid", "medicinal", "burnt plastic", "rancid", "sewage"),
    "medium": ("papery", "skunky", "buttery", "sulfur", "astringent", "harsh", "solvent"),
}


def _infer_family(text: str) -> str:
    for family, keywords in FAMILY_RULES.items():
        if any(keyword in text for keyword in keywords):
            return family
    return "other"


def _infer_stage(text: str, family: str) -> str:
    scores = {stage: sum(1 for keyword in keywords if keyword in text) for stage, keywords in STAGE_RULES.items()}
    stage = max(scores, key=lambda key: scores[key])
    if scores[stage] > 0:
        return stage
    if family == "oxidation":
        return "packaging"
    if family in {"sulfur", "ester"}:
        return "fermentation"
    return "mash_boil"


def _infer_severity(text: str) -> str:
    if any(keyword in text for keyword in SEVERITY_HINTS["high"]):
        return "High"
    if any(keyword in text for keyword in SEVERITY_HINTS["medium"]):
        return "Medium"
    return "Low to Medium"


def _enrich_flavor(flavor: dict) -> dict:
    text = " ".join([
        flavor["name"],
        flavor["nickname"],
        flavor["description"],
        flavor["avoidance"],
        " ".join(flavor["common_styles"]),
    ]).lower()

    family = _infer_family(text)
    stage = _infer_stage(text, family)

    flavor["family"] = family
    flavor["primary_stage"] = stage
    flavor["severity"] = _infer_severity(text)
    flavor["likely_causes"] = FAMILY_CAUSES[family]
    flavor["diagnostic_checks"] = STAGE_CHECKS[stage]
    flavor["qa_focus"] = [
        f"Track this fault in style flights where {', '.join(flavor['common_styles'][:2])} are benchmarked",
        "Record occurrence against batch date, fermentation profile, and package DO",
    ]
    return flavor


OFF_FLAVORS = [_enrich_flavor(item) for item in OFF_FLAVORS]


def get_flavor_by_slug(slug: str):
    """Return a single enriched flavor dictionary by slug."""
    return next((item for item in OFF_FLAVORS if item["slug"] == slug), None)
