import numpy as np

# 1. Definition of the 4x4 Natural Square (1 to 16)
# This matrix defines the numerical values assigned to each cell.
NATURAL_SQUARE = np.array([
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
])

# 2. The 36 Domino Tiling Patterns (P1 to P36)
# Each pattern is represented as a 4x4 grid where identical letters
# indicate cells belonging to the same 2-block domino.
PATTERNS = {
    1: """
        A A B B
        C C D D
        E E F F
        G G H H
    """,
    2: """
        A A B B
        C C D D
        E E F G
        H H F G
    """,
    3: """
        A A B B
        C C D D
        E F F G
        E H H G
    """,
    4: """
        A A B B
        C C D D
        E F G G
        E F H H
    """,
    5: """
        A A B B
        C C D D
        E F G H
        E F G H
    """,
    6: """
        A A B B
        C C D E
        F F D E
        G G H H
    """,
    7: """
        A A B B
        C C D E
        F G D E
        F G H H
    """,
    8: """
        A A B B
        C D D E
        C F F E
        G G H H
    """,
    9: """
        A A B B
        C D E E
        C D F F
        G G H H
    """,
    10: """
        A A B B
        C D E E
        C D F G
        H H F G
    """,
    11: """
        A A B B
        C D E F
        C D E F
        G G H H
    """,
    12: """
        A A B C
        D D B C
        E E F F
        G G H H
    """,
    13: """
        A A B C
        D D B C
        E E F G
        H H F G
    """,
    14: """
        A A B C
        D D B C
        E F F G
        E H H G
    """,
    15: """
        A A B C
        D D B C
        E F G G
        E F H H
    """,
    16: """
        A A B C
        D D B C
        E F G H
        E F G H
    """,
    17: """
        A A B C
        D E B C
        D E F F
        G G H H
    """,
    18: """
        A A B C
        D E B C
        D E F G
        H H F G
    """,
    19: """
        A B B C
        A D D C
        E E F F
        G G H H
    """,
    20: """
        A B B C
        A D D C
        E E F G
        H H F G
    """,
    21: """
        A B B C
        A D D C
        E F F G
        E H H G
    """,
    22: """
        A B B C
        A D D C
        E F G G
        E F H H
    """,
    23: """
        A B B C
        A D D C
        E F G H
        E F G H
    """,
    24: """
        A B B C
        A D E C
        F D E G
        F H H G
    """,
    25: """
        A B C C
        A B D D
        E E F F
        G G H H
    """,
    26: """
        A B C C
        A B D D
        E E F G
        H H F G
    """,
    27: """
        A B C C
        A B D D
        E F F G
        E H H G
    """,
    28: """
        A B C C
        A B D D
        E F G G
        E F H H
    """,
    29: """
        A B C C
        A B D D
        E F G H
        E F G H
    """,
    30: """
        A B C C
        A B D E
        F F D E
        G G H H
    """,
    31: """
        A B C C
        A B D E
        F G D E
        F G H H
    """,
    32: """
        A B C D
        A B C D
        E E F F
        G G H H
    """,
    33: """
        A B C D
        A B C D
        E E F G
        H H F G
    """,
    34: """
        A B C D
        A B C D
        E F F G
        E H H G
    """,
    35: """
        A B C D
        A B C D
        E F G G
        E F H H
    """,
    36: """
        A B C D
        A B C D
        E F G H
        E F G H
    """
}

# 3. Definition of Pairings
# These specific pairings exhibit algebraic symmetric properties (High-order Complementary Identities).
PAIRINGS = [
    (1, 36), (8, 24), (11, 21), (15, 26), (3, 34), (9, 18),
    (19, 23), (6, 31), (5, 32), (13, 28), (2, 35), (4, 33),
    (12, 29), (16, 25), (7, 30), (10, 17), (14, 27), (20, 22)
]


def parse_pattern_to_dominoes(pattern_str):
    """
    Extracts a list of 2-cell value pairs covered by each domino
    from the pattern string, using the values from NATURAL_SQUARE.
    """
    # Clean up the string to get a linear list of labels
    cleaned_str = "".join(pattern_str.split())
    if len(cleaned_str) != 16:
        raise ValueError("Pattern string length is not 16.")
        
    grid_labels = np.array(list(cleaned_str)).reshape((4, 4))
    
    domino_blocks = {}
    
    # Iterate through all cells (i, j)
    for i in range(4):
        for j in range(4):
            label = grid_labels[i, j]
            value = NATURAL_SQUARE[i, j]
            
            if label not in domino_blocks:
                domino_blocks[label] = []
            
            domino_blocks[label].append(value)

    # Convert the dictionary into a list of domino value tuples
    domino_values = []
    for label, values in domino_blocks.items():
        if len(values) != 2:
            raise ValueError(f"Domino label {label} covers {len(values)} cells, not 2.")
        domino_values.append(tuple(values))
        
    return domino_values


def calculate_sum_of_block_sums_power(domino_values, k):
    """
    Calculates the total sum of block sums raised to the power k, S_sum^k(P).
    S_sum^k(P) = Sum_{i=1}^8 (x_i + y_i)^k
    """
    total_sum = 0
    for x, y in domino_values:
        block_sum = x + y
        total_sum += (block_sum ** k)
    return total_sum


def main():
    """
    Main execution: Calculates and outputs the pair sums of the power sums 
    of the 2-block sums for all defined pairings.
    """
    results = {}

    # Pre-parse domino values for all patterns
    parsed_dominoes = {}
    for pid, pattern_str in PATTERNS.items():
        parsed_dominoes[pid] = parse_pattern_to_dominoes(pattern_str)
        
    print("## 📊 Verification Results: Pair Sums of Block Sums Raised to Power k")
    print("------------------------------------------------------------------------------------------")
    print("Pair (P_i, P_j) | S_sum^1 Sum | S_sum^2 Sum | S_sum^3 Sum | S_sum^4 Sum")
    print("------------------------------------------------------------------------------------------")

    # Execute calculation for the defined pairings
    for pid_i, pid_j in PAIRINGS:
        dominoes_i = parsed_dominoes[pid_i]
        dominoes_j = parsed_dominoes[pid_j]
        
        sums_i = {}
        sums_j = {}
        sum_of_sums = {}

        # Calculate sums for k=1 to k=4
        for k in range(1, 5):
            sums_i[k] = calculate_sum_of_block_sums_power(dominoes_i, k)
            sums_j[k] = calculate_sum_of_block_sums_power(dominoes_j, k)
            sum_of_sums[k] = sums_i[k] + sums_j[k]

        results[(pid_i, pid_j)] = sum_of_sums
        
        # Output results
        print(
            f"P{pid_i:02d}-P{pid_j:02d}     | "
            f"{sum_of_sums[1]:>11,} | "
            f"{sum_of_sums[2]:>11,} | "
            f"{sum_of_sums[3]:>11,} | "
            f"{sum_of_sums[4]:>11,}"
        )
        
    print("------------------------------------------------------------------------------------------")
    print("\n## 🔍 Observations on Results")
    
    # Verify k=1 sum is invariant (272)
    k1_sums = [sum_of_sums[1] for sum_of_sums in results.values()]
    k1_invariant_value = k1_sums[0] if k1_sums else 0
    print(f"* S_sum^1 (k=1) is invariant across all pairs with a value of {k1_invariant_value} (expected and trivial result).")
    
    # Verify invariance for k=2, 3, 4
    for k in range(2, 5):
        k_sums = [sum_of_sums[k] for sum_of_sums in results.values()]
        unique_k_sums = set(k_sums)
        
        if len(unique_k_sums) == 1:
            print(f"* S_sum^{k} Pair Sum is **invariant** across all pairs with a value of {list(unique_k_sums)[0]:,}.")
        else:
            print(f"* S_sum^{k} Pair Sum is **NOT invariant**. Unique values: {sorted(list(unique_k_sums))}.")


if __name__ == "__main__":
    main()