import numpy as np

# 1. Definition of the 4x4 Natural Square (1 to 16)
NATURAL_SQUARE = np.array([
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
])

# 2. The 36 Domino Tiling Patterns (P1 to P36)
# The pattern definitions are kept for completeness, though they are large.
PATTERNS = {
    1: "A A B B C C D D E E F F G G H H",
    2: "A A B B C C D D E E F G H H F G",
    3: "A A B B C C D D E F F G E H H G",
    4: "A A B B C C D D E F G G E F H H",
    5: "A A B B C C D D E F G H E F G H",
    6: "A A B B C C D E F F D E G G H H",
    7: "A A B B C C D E F G D E F G H H",
    8: "A A B B C D D E C F F E G G H H",
    9: "A A B B C D E E C D F F G G H H",
    10: "A A B B C D E E C D F G H H F G",
    11: "A A B B C D E F C D E F G G H H",
    12: "A A B C D D B C E E F F G G H H",
    13: "A A B C D D B C E E F G H H F G",
    14: "A A B C D D B C E F F G E H H G",
    15: "A A B C D D B C E F G G E F H H",
    16: "A A B C D D B C E F G H E F G H",
    17: "A A B C D E B C D E F F G G H H",
    18: "A A B C D E B C D E F G H H F G",
    19: "A B B C A D D C E E F F G G H H",
    20: "A B B C A D D C E E F G H H F G",
    21: "A B B C A D D C E F F G E H H G",
    22: "A B B C A D D C E F G G E F H H",
    23: "A B B C A D D C E F G H E F G H",
    24: "A B B C A D E C F D E G F H H G",
    25: "A B C C A B D D E E F F G G H H",
    26: "A B C C A B D D E E F G H H F G",
    27: "A B C C A B D D E F F G E H H G",
    28: "A B C C A B D D E F G G E F H H",
    29: "A B C C A B D D E F G H E F G H",
    30: "A B C C A B D E F F D E G G H H",
    31: "A B C C A B D E F G D E F G H H",
    32: "A B C D A B C D E E F F G G H H",
    33: "A B C D A B C D E E F G H H F G",
    34: "A B C D A B C D E F F G E H H G",
    35: "A B C D A B C D E F G G E F H H",
    36: "A B C D A B C D E F G H E F G H"
}

# 3. Definition of Pairings (Algebraic Symmetric Pairs)
PAIRINGS = [
    (1, 36), (8, 24), (11, 21), (15, 26), (3, 34), (9, 18),
    (19, 23), (6, 31), (5, 32), (13, 28), (2, 35), (4, 33),
    (12, 29), (16, 25), (7, 30), (10, 17), (14, 27), (20, 22)
]


def parse_pattern_to_dominoes(pattern_str):
    """
    Extracts a list of 2-cell value pairs [(x, y), ...] covered by each domino
    from the pattern string, utilizing the values from NATURAL_SQUARE.
    (Function retained from previous version)
    """
    cleaned_str = "".join(pattern_str.split())
    grid_labels = np.array(list(cleaned_str)).reshape((4, 4))

    domino_blocks = {}

    for i in range(4):
        for j in range(4):
            label = grid_labels[i, j]
            value = NATURAL_SQUARE[i, j]

            if label not in domino_blocks:
                domino_blocks[label] = []

            domino_blocks[label].append(value)

    domino_values = []
    for values in domino_blocks.values():
        if len(values) != 2:
            raise ValueError(f"Domino block contains values other than two.")
        domino_values.append(tuple(values))

    return domino_values


def calculate_sum_of_block_products_squared(domino_values):
    """
    Calculates the 2-Block Product Square Sum: S_prod^2(P) = Sum_{i=1}^8 (x_i * y_i)^2.
    """
    total_product_squared_sum = 0
    for x, y in domino_values:
        block_product = x * y
        total_product_squared_sum += (block_product ** 2)
    return total_product_squared_sum


def main():
    """
    Main execution: Calculates and outputs the pair sum of S_prod^2(P) 
    for all defined algebraic symmetric pairings.
    """

    # Pre-parse domino values for all patterns
    parsed_dominoes = {}
    for pid, pattern_str in PATTERNS.items():
        parsed_dominoes[pid] = parse_pattern_to_dominoes(pattern_str)

    # Pre-calculate S_prod^2(P) for all patterns
    all_s_prod_sq = {}
    for pid in range(1, 37):
        all_s_prod_sq[pid] = calculate_sum_of_block_products_squared(parsed_dominoes[pid])

    print("## 📊 Verification Results: Pair Sums of 2-Block Product Square Sum ($S_{\\text{prod}^2}$)")
    print("--------------------------------------------------------------------------------")
    print("Pair (P_i, P_j) | $S_{\\text{prod}^2}(P_i)$ | $S_{\\text{prod}^2}(P_j)$ | Pair Sum")
    print("--------------------------------------------------------------------------------")

    pair_sums = []

    # Execute calculation for the specified pairings
    for pid_i, pid_j in PAIRINGS:
        s_prod_sq_i = all_s_prod_sq[pid_i]
        s_prod_sq_j = all_s_prod_sq[pid_j]
        sum_of_products_sq = s_prod_sq_i + s_prod_sq_j
        pair_sums.append(sum_of_products_sq)

        # Output results
        print(
            f"P{pid_i:02d}-{pid_j:02d}     | "
            f"{s_prod_sq_i:15,} | "
            f"{s_prod_sq_j:15,} | "
            f"{sum_of_products_sq:20,}"
        )

    print("--------------------------------------------------------------------------------")

    # Analyze the results
    unique_pair_sums = set(pair_sums)
    print("\n## 🔍 Observations")

    if len(unique_pair_sums) == 1:
        invariant_sum = list(unique_pair_sums)[0]
        print(f"* The Pair Sum is **invariant** across all pairs, with a value of {invariant_sum:,}.")
    else:
        print(f"* The Pair Sum is **NOT consistent** across all pairs.")
        print(f"* Observed unique Pair Sums (Ascending): {sorted(list(unique_pair_sums))}")


if __name__ == "__main__":
    main()