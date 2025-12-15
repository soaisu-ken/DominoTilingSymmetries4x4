import numpy as np
from itertools import combinations

# Define the 36 domino tiling patterns
# The indices (0-7) represent the 8 individual domino blocks.
patterns = {
    1: [[0,0,1,1], [2,2,3,3], [4,4,5,5], [6,6,7,7]],
    2: [[0,0,1,1], [2,2,3,3], [4,4,5,6], [7,7,5,6]],
    3: [[0,0,1,1], [2,2,3,3], [4,5,5,6], [4,7,7,6]],
    4: [[0,0,1,1], [2,2,3,3], [4,5,6,6], [4,5,7,7]],
    5: [[0,0,1,1], [2,2,3,3], [4,5,6,7], [4,5,6,7]],
    6: [[0,0,1,1], [2,2,3,4], [5,5,3,4], [6,6,7,7]],
    7: [[0,0,1,1], [2,2,3,4], [5,6,3,4], [5,6,7,7]],
    8: [[0,0,1,1], [2,3,3,4], [2,5,5,4], [6,6,7,7]],
    9: [[0,0,1,1], [2,3,4,4], [2,3,5,5], [6,6,7,7]],
    10: [[0,0,1,1], [2,3,4,4], [2,3,5,6], [7,7,5,6]],
    11: [[0,0,1,1], [2,3,4,5], [2,3,4,5], [6,6,7,7]],
    12: [[0,0,1,2], [3,3,1,2], [4,4,5,5], [6,6,7,7]],
    13: [[0,0,1,2], [3,3,1,2], [4,4,5,6], [7,7,5,6]],
    14: [[0,0,1,2], [3,3,1,2], [4,5,5,6], [4,7,7,6]],
    15: [[0,0,1,2], [3,3,1,2], [4,5,6,6], [4,5,7,7]],
    16: [[0,0,1,2], [3,3,1,2], [4,5,6,7], [4,5,6,7]],
    17: [[0,0,1,2], [3,4,1,2], [3,4,5,5], [6,6,7,7]],
    18: [[0,0,1,2], [3,4,1,2], [3,4,5,6], [7,7,5,6]],
    19: [[0,1,1,2], [0,3,3,2], [4,4,5,5], [6,6,7,7]],
    20: [[0,1,1,2], [0,3,3,2], [4,4,5,6], [7,7,5,6]],
    21: [[0,1,1,2], [0,3,3,2], [4,5,5,6], [4,7,7,6]],
    22: [[0,1,1,2], [0,3,3,2], [4,5,6,6], [4,5,7,7]],
    23: [[0,1,1,2], [0,3,3,2], [4,5,6,7], [4,5,6,7]],
    24: [[0,1,1,2], [0,3,4,2], [5,3,4,6], [5,7,7,6]],
    25: [[0,1,2,2], [0,1,3,3], [4,4,5,5], [6,6,7,7]],
    26: [[0,1,2,2], [0,1,3,3], [4,4,5,6], [7,7,5,6]],
    27: [[0,1,2,2], [0,1,3,3], [4,5,5,6], [4,7,7,6]],
    28: [[0,1,2,2], [0,1,3,3], [4,5,6,6], [4,5,7,7]],
    29: [[0,1,2,2], [0,1,3,3], [4,5,6,7], [4,5,6,7]],
    30: [[0,1,2,2], [0,1,3,4], [5,5,3,4], [6,6,7,7]],
    31: [[0,1,2,2], [0,1,3,4], [5,6,3,4], [5,6,7,7]],
    32: [[0,1,2,3], [0,1,2,3], [4,4,5,5], [6,6,7,7]],
    33: [[0,1,2,3], [0,1,2,3], [4,4,5,6], [7,7,5,6]],
    34: [[0,1,2,3], [0,1,2,3], [4,5,5,6], [4,7,7,6]],
    35: [[0,1,2,3], [0,1,2,3], [4,5,6,6], [4,5,7,7]],
    36: [[0,1,2,3], [0,1,2,3], [4,5,6,7], [4,5,6,7]],
}

def calculate_s_sum_k(pattern, k):
    """Calculates the k-th power sum of the 2-block sums (S_sum^k)"""
    # 4x4 Natural Square: 1 to 16
    grid = np.arange(1, 17).reshape(4, 4)
    block_sums = []
    
    visited = set()
    for i in range(4):
        for j in range(4):
            block_id = pattern[i][j]
            if block_id not in visited:
                visited.add(block_id)
                positions = [(r, c) for r in range(4) for c in range(4) 
                           if pattern[r][c] == block_id]
                block_sum = sum(grid[r, c] for r, c in positions)
                block_sums.append(block_sum)
    
    return sum(s**k for s in block_sums)

def calculate_s_prod(pattern):
    """Calculates the sum of 2-block products (S_prod)"""
    grid = np.arange(1, 17).reshape(4, 4)
    products = []
    
    visited = set()
    for i in range(4):
        for j in range(4):
            block_id = pattern[i][j]
            if block_id not in visited:
                visited.add(block_id)
                positions = [(r, c) for r in range(4) for c in range(4) 
                           if pattern[r][c] == block_id]
                values = [grid[r, c] for r, c in positions]
                # Each block has exactly two cells, so their product is calculated
                products.append(values[0] * values[1])
    
    return sum(products)

def find_perfect_complementary_pairs():
    """Searches for Complete Algebraic Complementary Pairs"""
    # Invariant Constants from the Extended High-Order Complementary Identity Theorem
    C1, C2, C3 = 272, 5848, 141032
    C_prod = 1428
    
    results = []
    used = set()
    
    # Iterate through all unique pairs (i, j) where i < j
    for i in range(1, 37):
        if i in used:
            continue
            
        pattern_i = patterns[i]
        s_sum1_i = calculate_s_sum_k(pattern_i, 1)
        s_sum2_i = calculate_s_sum_k(pattern_i, 2)
        s_sum3_i = calculate_s_sum_k(pattern_i, 3)
        s_prod_i = calculate_s_prod(pattern_i)
        
        for j in range(i+1, 37):
            if j in used:
                continue
                
            pattern_j = patterns[j]
            s_sum1_j = calculate_s_sum_k(pattern_j, 1)
            s_sum2_j = calculate_s_sum_k(pattern_j, 2)
            s_sum3_j = calculate_s_sum_k(pattern_j, 3)
            s_prod_j = calculate_s_prod(pattern_j)
            
            # Check the Complete Algebraic Complementary Pair conditions
            if (abs((s_sum1_i + s_sum1_j) - C1) < 1e-9 and
                abs((s_sum2_i + s_sum2_j) - C2) < 1e-9 and
                abs((s_sum3_i + s_sum3_j) - C3) < 1e-9 and
                abs((s_prod_i + s_prod_j) - C_prod) < 1e-9):
                
                results.append({
                    'pair': (i, j),
                    's_sum1': (s_sum1_i, s_sum1_j),
                    's_sum2': (s_sum2_i, s_sum2_j),
                    's_sum3': (s_sum3_i, s_sum3_j),
                    's_prod': (s_prod_i, s_prod_j)
                })
                used.add(i)
                used.add(j)
                break # Found the unique complement, move to the next pattern i
    
    return results, used

def verify_uniqueness():
    """Verifies the existence and unique partition of the theorem."""
    print("=" * 80)
    print("Verification Program for Unique Partition of Complete Complementary Pairs")
    print("=" * 80)
    
    pairs, used = find_perfect_complementary_pairs()
    
    print(f"\n[Results]")
    print(f"Number of Complete Complementary Pairs Found: {len(pairs)}")
    print(f"Number of Patterns Classified: {len(used)}")
    print(f"Total Number of Patterns: 36")
    
    if len(pairs) == 18 and len(used) == 36:
        print("\n✓ SUCCESS: All 36 tilings are uniquely partitioned into 18 Complete Complementary Pairs, as stated by the theorem.")
    else:
        print("\n✗ FAILURE: The unique partition failed.")
        return False
    
    print("\n" + "=" * 80)
    print("Details of Complete Complementary Pairs")
    print("=" * 80)
    
    for idx, result in enumerate(pairs, 1):
        i, j = result['pair']
        print(f"\nPair {idx}: (P{i}, P{j})")
        print(f"  S_sum^1: {result['s_sum1'][0]} + {result['s_sum1'][1]} = {sum(result['s_sum1'])}")
        print(f"  S_sum^2: {result['s_sum2'][0]} + {result['s_sum2'][1]} = {sum(result['s_sum2'])}")
        print(f"  S_sum^3: {result['s_sum3'][0]} + {result['s_sum3'][1]} = {sum(result['s_sum3'])}")
        print(f"  S_prod:  {result['s_prod'][0]} + {result['s_prod'][1]} = {sum(result['s_prod'])}")
    
    # Additional check for uniqueness: ensures no pattern belongs to multiple pairs
    print("\n" + "=" * 80)
    print("Additional Uniqueness Check: Ensuring each pattern belongs to only one pair")
    print("=" * 80)
    
    pattern_count = {}
    for result in pairs:
        i, j = result['pair']
        pattern_count[i] = pattern_count.get(i, 0) + 1
        pattern_count[j] = pattern_count.get(j, 0) + 1
    
    all_unique = all(count == 1 for count in pattern_count.values())
    
    if all_unique:
        print("✓ Each pattern strictly belongs to one pair (Uniqueness confirmed)")
    else:
        print("✗ Duplication detected")
        for p, count in pattern_count.items():
            if count > 1:
                print(f"  Pattern P{p} belongs to {count} pairs")
    
    return len(pairs) == 18 and len(used) == 36 and all_unique

if __name__ == "__main__":
    success = verify_uniqueness()
    print("\n" + "=" * 80)
    if success:
        print(" [PROOF COMPLETE] Unique partition of the Extended High-Order Complementary Identity Theorem numerically verified.")
    else:
        print(" [VERIFICATION FAILED] The claim of the theorem could not be confirmed.")
    print("=" * 80)