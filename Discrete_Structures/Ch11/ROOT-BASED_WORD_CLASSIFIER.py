# ------------------------------------------------------------
# ROOT-BASED WORD CLASSIFIER
# ------------------------------------------------------------
# This program groups academic words in a way that tries to
# make more HUMAN sense than plain alphabetical order.
#
# Instead of asking:
#   "Which word comes first alphabetically?"
#
# it asks:
#   "What root, prefix, suffix, or subject family does this
#    word seem to belong to?"
#
# WHY THIS CAN BE BETTER:
# Alphabetical order is useful for search, but not always for
# meaning. For example, "biology" and "calculus" might sit near
# each other alphabetically even though they are not closely
# related as ideas.
#
# This program tries to build a more meaningful structure.
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 1: Our list of words
# ------------------------------------------------------------
words = [
    "mathematics",
    "physics",
    "geography",
    "zoology",
    "meteorology",
    "geology",
    "psychology",
    "chemistry",
    "biology",
    "calculus",
    "astronomy",
    "sociology",
    "ecology",
    "logic",
    "statistics",
    "trigonometry",
    "anatomy",
    "philosophy",
    "literature",
    "history"
]


# ------------------------------------------------------------
# STEP 2: Define some root / prefix / suffix patterns
# ------------------------------------------------------------
# These are not perfect etymologies.
# They are a practical classroom-friendly approximation.
#
# Each key is a category label.
# Each value is a list of clues that suggest membership.
# ------------------------------------------------------------
patterns = {
    "geo (earth / land)": ["geography", "geology", "geophysics"],
    "zoo (animal / living creature)": ["zoology"],
    "psycho (mind / soul)": ["psychology"],
    "meteor (things in the air / atmosphere)": ["meteorology"],
    "bio (life)": ["biology"],
    "astro (star / outer space)": ["astronomy"],
    "eco (household / environment)": ["ecology"],
    "socio (society)": ["sociology"],
    "ana (up / throughout, often used in body analysis terms)": ["anatomy"],
    "trigono / metry (triangle / measure)": ["trigonometry"],
    "math / mathemat (learning / science)": ["mathematics"],
    "phys (nature)": ["physics"],
    "chem (alchemy / chemistry tradition)": ["chemistry"],
    "calcul (counting stone / calculation tradition)": ["calculus"],
    "histor (inquiry / investigation)": ["history"],
    "phil / sophy (love of wisdom)": ["philosophy"],
    "liter (letters)": ["literature"],
    "logic (reason / word)": ["logic"],
    "stat (state / numerical summary tradition)": ["statistics"]
}


# ------------------------------------------------------------
# STEP 3: Also classify by suffix pattern
# ------------------------------------------------------------
# Suffixes often tell us something about the kind of word.
# For example:
#   -ology often means "study of"
#   -ics often marks a field of study
#   -graphy can mean writing / description
#   -metry can mean measurement
# ------------------------------------------------------------
def get_suffix_category(word):
    if word.endswith("ology"):
        return "-ology (study of)"
    elif word.endswith("ics"):
        return "-ics (field / discipline)"
    elif word.endswith("graphy"):
        return "-graphy (writing / description)"
    elif word.endswith("metry"):
        return "-metry (measurement)"
    elif word.endswith("phy"):
        return "-phy / -sophy family"
    elif word.endswith("ure"):
        return "-ure"
    elif word.endswith("ory"):
        return "-ory"
    else:
        return "other suffix"


# ------------------------------------------------------------
# STEP 4: Broad domain classification
# ------------------------------------------------------------
# This is even more human-centered.
# It groups words by their academic neighborhood.
# ------------------------------------------------------------
domain_map = {
    "formal sciences": ["mathematics", "calculus", "statistics", "logic", "trigonometry"],
    "natural sciences": ["physics", "chemistry", "biology", "geology", "zoology", "astronomy", "ecology", "anatomy", "meteorology"],
    "social sciences": ["psychology", "sociology", "geography"],
    "humanities": ["history", "philosophy", "literature"]
}


# ------------------------------------------------------------
# STEP 5: Helper function to find the root category
# ------------------------------------------------------------
def get_root_category(word):
    """
    Return the root-based category label for the word.
    If the word is not explicitly listed, return 'unknown root group'.
    """
    for category, word_list in patterns.items():
        if word in word_list:
            return category
    return "unknown root group"


# ------------------------------------------------------------
# STEP 6: Helper function to find the domain
# ------------------------------------------------------------
def get_domain(word):
    """
    Return the broad academic domain for a word.
    """
    for domain, word_list in domain_map.items():
        if word in word_list:
            return domain
    return "unclassified domain"


# ------------------------------------------------------------
# STEP 7: Build a nested classification structure
# ------------------------------------------------------------
# Our structure will look like this:
#
# domain
#   -> suffix category
#       -> root category
#           -> list of words
#
# This lets us see the same word as part of multiple levels
# of organization.
# ------------------------------------------------------------
classification_tree = {}

for word in words:
    domain = get_domain(word)
    suffix = get_suffix_category(word)
    root = get_root_category(word)

    # Create missing layers as needed
    if domain not in classification_tree:
        classification_tree[domain] = {}

    if suffix not in classification_tree[domain]:
        classification_tree[domain][suffix] = {}

    if root not in classification_tree[domain][suffix]:
        classification_tree[domain][suffix][root] = []

    classification_tree[domain][suffix][root].append(word)


# ------------------------------------------------------------
# STEP 8: Pretty-print the classification tree
# ------------------------------------------------------------
def print_classification_tree(tree):
    """
    Print the nested classification structure in a readable way.
    """
    for domain, suffix_groups in tree.items():
        print(f"\nDOMAIN: {domain}")

        for suffix, root_groups in suffix_groups.items():
            print(f"  SUFFIX GROUP: {suffix}")

            for root, words_in_group in root_groups.items():
                print(f"    ROOT GROUP: {root}")
                for word in words_in_group:
                    print(f"      - {word}")


# ------------------------------------------------------------
# STEP 9: Run the program
# ------------------------------------------------------------
print("ROOT-BASED / MEANING-BASED CLASSIFICATION")
print("=" * 55)
print_classification_tree(classification_tree)