"""
Burnside's Lemma Verification for 4x4 Domino Tilings
=====================================================
This program verifies the fixed-point counts |Fix(g)| for each element g of
the dihedral group D4, acting on the 36 distinct domino tilings of a 4x4 grid.

Each tiling is represented as a 4x4 grid of block labels (A-H).
Two cells sharing the same label form a domino.

A tiling P is "fixed" by a transformation g if applying g to the grid
produces a tiling that is isomorphic to P (i.e., same domino structure,
possibly with relabeled blocks).
"""

import numpy as np
from itertools import permutations

# ============================================================
# STEP 1: Define all 36 tilings as 4x4 label grids
# Labels are integers 0-7 (representing A-H)
# ============================================================

def parse_pattern(text_grid):
    """Convert letter grid to integer grid (A=0, B=1, ..., H=7)."""
    rows = []
    for line in text_grid.strip().split('\n'):
        row = [ord(c) - ord('A') for c in line.split()]
        rows.append(row)
    return rows

# All 36 patterns defined as 4x4 label grids
PATTERNS_RAW = [
    # P1
    """A A B B
C C D D
E E F F
G G H H""",
    # P2
    """A A B B
C C D D
E E F G
H H F G""",
    # P3
    """A A B B
C C D D
E F F G
E H H G""",
    # P4
    """A A B B
C C D D
E F G G
E F H H""",
    # P5
    """A A B B
C C D D
E F G H
E F G H""",
    # P6
    """A A B B
C C D E
F F D E
G G H H""",
    # P7
    """A A B B
C C D E
F G D E
F G H H""",
    # P8
    """A A B B
C D D E
C F F E
G G H H""",
    # P9
    """A A B B
C D E E
C D F F
G G H H""",
    # P10
    """A A B B
C D E E
C D F G
H H F G""",
    # P11
    """A A B B
C D E F
C D E F
G G H H""",
    # P12
    """A A B C
D D B C
E E F F
G G H H""",
    # P13
    """A A B C
D D B C
E E F G
H H F G""",
    # P14
    """A A B C
D D B C
E F F G
E H H G""",
    # P15
    """A A B C
D D B C
E F G G
E F H H""",
    # P16
    """A A B C
D D B C
E F G H
E F G H""",
    # P17
    """A A B C
D E B C
D E F F
G G H H""",
    # P18
    """A A B C
D E B C
D E F G
H H F G""",
    # P19
    """A B B C
A D D C
E E F F
G G H H""",
    # P20
    """A B B C
A D D C
E E F G
H H F G""",
    # P21
    """A B B C
A D D C
E F F G
E H H G""",
    # P22
    """A B B C
A D D C
E F G G
E F H H""",
    # P23
    """A B B C
A D D C
E F G H
E F G H""",
    # P24
    """A B B C
A D E C
F D E G
F H H G""",
    # P25
    """A B C C
A B D D
E E F F
G G H H""",
    # P26
    """A B C C
A B D D
E E F G
H H F G""",
    # P27
    """A B C C
A B D D
E F F G
E H H G""",
    # P28
    """A B C C
A B D D
E F G G
E F H H""",
    # P29
    """A B C C
A B D D
E F G H
E F G H""",
    # P30
    """A B C C
A B D E
F F D E
G G H H""",
    # P31
    """A B C C
A B D E
F G D E
F G H H""",
    # P32
    """A B C D
A B C D
E E F F
G G H H""",
    # P33
    """A B C D
A B C D
E E F G
H H F G""",
    # P34
    """A B C D
A B C D
E F F G
E H H G""",
    # P35
    """A B C D
A B C D
E F G G
E F H H""",
    # P36
    """A B C D
A B C D
E F G H
E F G H""",
]

PATTERNS = [parse_pattern(p) for p in PATTERNS_RAW]


# ============================================================
# STEP 2: Normalize a tiling to a canonical form
# (relabel blocks in reading order: first block seen = 0, etc.)
# ============================================================

def normalize(grid):
    """
    Normalize a 4x4 label grid by relabeling blocks in first-encounter order.
    Returns a tuple-of-tuples for hashing.
    """
    mapping = {}
    next_id = 0
    result = []
    for row in grid:
        new_row = []
        for val in row:
            if val not in mapping:
                mapping[val] = next_id
                next_id += 1
            new_row.append(mapping[val])
        result.append(tuple(new_row))
    return tuple(result)


# ============================================================
# STEP 3: Define all 8 D4 transformations on a 4x4 grid
# Coordinates: grid[r][c], r=row (0=top), c=col (0=left)
# ============================================================

def transform_grid(grid, transform_func):
    """Apply a coordinate transformation to a 4x4 grid."""
    n = 4
    new_grid = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_r, new_c = transform_func(r, c, n)
            new_grid[new_r][new_c] = grid[r][c]
    return new_grid

# Identity
def e(r, c, n):       return (r, c)

# 90-degree clockwise rotation: (r,c) -> (c, n-1-r)
def r90(r, c, n):     return (c, n-1-r)

# 180-degree rotation: (r,c) -> (n-1-r, n-1-c)
def r180(r, c, n):    return (n-1-r, n-1-c)

# 270-degree clockwise rotation: (r,c) -> (n-1-c, r)
def r270(r, c, n):    return (n-1-c, r)

# Horizontal flip (reflect across horizontal midline): (r,c) -> (n-1-r, c)
def sh(r, c, n):      return (n-1-r, c)

# Vertical flip (reflect across vertical midline): (r,c) -> (r, n-1-c)
def sv(r, c, n):      return (r, n-1-c)

# Main diagonal (transpose): (r,c) -> (c, r)
def sd1(r, c, n):     return (c, r)

# Anti-diagonal: (r,c) -> (n-1-c, n-1-r)
def sd2(r, c, n):     return (n-1-c, n-1-r)

TRANSFORMS = {
    'e':    e,
    'r90':  r90,
    'r180': r180,
    'r270': r270,
    's_h':  sh,
    's_v':  sv,
    's_d1': sd1,
    's_d2': sd2,
}

# Precompute normalized forms of all 36 patterns
NORM_PATTERNS = [normalize(p) for p in PATTERNS]
NORM_SET = set(NORM_PATTERNS)

# ============================================================
# STEP 4: Check if a transformed tiling is fixed (= same tiling)
# ============================================================

def is_fixed(pattern_idx, transform_func):
    """
    Returns True if applying transform_func to PATTERNS[pattern_idx]
    yields a tiling with the same domino structure (up to relabeling).
    """
    original = PATTERNS[pattern_idx]
    transformed = transform_grid(original, transform_func)
    return normalize(transformed) == NORM_PATTERNS[pattern_idx]

# ============================================================
# STEP 5: Compute Fix(g) for each transformation
# ============================================================

print("=" * 70)
print("Burnside's Lemma: Fixed-Point Verification for 4x4 Domino Tilings")
print("=" * 70)
print()

total_fixed = 0
results = {}

for name, func in TRANSFORMS.items():
    fixed_ids = [i+1 for i in range(36) if is_fixed(i, func)]
    count = len(fixed_ids)
    total_fixed += count
    results[name] = (count, fixed_ids)

    id_str = ', '.join(f'P{i}' for i in fixed_ids) if fixed_ids else 'none'
    print(f"|Fix({name:5s})| = {count:2d}  →  {id_str}")

print()
print(f"Sum of |Fix(g)| = {total_fixed}")
families = total_fixed / 8
print(f"Number of orbits (families) = {total_fixed} / 8 = {families}")
print()

# ============================================================
# STEP 6: Verify against the values claimed in the paper
# ============================================================

CLAIMED = {
    'e':    36,
    'r90':  2,
    'r180': 8,
    'r270': 2,
    's_h':  12,
    's_v':  12,
    's_d1': 0,
    's_d2': 0,
}

print("=" * 70)
print("Verification against paper's claimed values:")
print("=" * 70)
print(f"{'Transform':<8} {'Computed':>10} {'Claimed':>10} {'Match':>8}")
print("-" * 40)

all_ok = True
for name in TRANSFORMS:
    computed = results[name][0]
    claimed  = CLAIMED[name]
    ok = computed == claimed
    if not ok:
        all_ok = False
    mark = "✅" if ok else "❌"
    print(f"{name:<8} {computed:>10} {claimed:>10} {mark:>8}")

print()
if all_ok:
    print("✅ All values match. Burnside's Lemma yields 9 families.")
else:
    print("❌ Some values do not match — please check pattern definitions.")

# ============================================================
# STEP 7: Detailed listing of fixed patterns per transformation
# ============================================================

print()
print("=" * 70)
print("Detailed fixed-pattern listing (for Table in paper):")
print("=" * 70)
for name, (count, ids) in results.items():
    id_str = ', '.join(f'P{i}' for i in ids) if ids else 'none'
    print(f"  {name:6s}: |Fix| = {count:2d}   [{id_str}]")

# ============================================================
# STEP 8: Verify the 9-orbit structure (Burnside count = 9)
# ============================================================

print()
print("=" * 70)
print("Orbit (Family) structure:")
print("=" * 70)

visited = set()
orbits = []
for i in range(36):
    if i in visited:
        continue
    orbit = set()
    for func in TRANSFORMS.values():
        transformed = transform_grid(PATTERNS[i], func)
        norm = normalize(transformed)
        # Find which pattern index matches
        try:
            j = NORM_PATTERNS.index(norm)
            orbit.add(j)
        except ValueError:
            pass  # transformed tiling not in our list (shouldn't happen)
    orbit_ids = sorted(orbit)
    for idx in orbit_ids:
        visited.add(idx)
    orbits.append(orbit_ids)

for k, orb in enumerate(orbits):
    id_str = ', '.join(f'P{i+1}' for i in orb)
    print(f"  Family {k+1} (size {len(orb)}): {id_str}")

print()
print(f"Total families found: {len(orbits)}")
assert len(orbits) == 9, "Expected 9 families!"
print("✅ Confirmed: 9 equivalence classes under D4.")