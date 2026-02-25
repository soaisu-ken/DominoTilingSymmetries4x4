Domino Tiling Algebraic Symmetry & Classification Verifiers
This repository provides the official implementation of the Computational Verification Protocol described in the paper:
"Algebraic Symmetries and the 90-Degree Rotation Complementarity Theorem in Domino Tilings of the $4 \times 4$ Natural Square" by Kenichi Takemura.
🛡️ Computational Verification Protocol
To ensure mathematical rigor and reproducibility, these scripts follow a formal verification protocol:
	1	Normalization (Canonical Form): All 36 tilings are stored in a canonical integer matrix format. ID labels (0–7) are reassigned using a row-major normalization function to eliminate duplicates.
	2	Population Completeness: The set of 36 tilings is verified against Kasteleyn’s formula ($\sqrt{|\det A|} = 36$). Symmetry closure under the $D_4$ group is confirmed via Burnside's Lemma.
	3	Exhaustive Search: Pairwise identities are verified by checking all $\binom{36}{2} = 630$ possible combinations to prove the uniqueness of the 18 Algebraic Complementary Pairs.

🔢 Script Mapping & Functionality
1. Population & Symmetry Audit
	•	File: calculator0_symmetry_check.py
	•	Corresponding Result: Theorem 2 & Table 2
	•	Description: Verifies the 8 elements of the dihedral group $D_4$ acting on the 36 tilings. It confirms the 9 symmetry classes (families) and the count of fixed points for each transformation.
2. 90-Degree Rotation Verifier
	•	File: domino_tiling_rotation_verifier.py (Calculator 1)
	•	Corresponding Result: Theorem 3 (90-Degree Rotation Product Sum Theorem)
	•	Identity: $S_{\text{prod}}(P) + S_{\text{prod}}(P^{90}) = 1,428$ for all $P \in \mathcal{P}$.
3. Power Sums of 2-Block Sums
	•	File: power_sum_verifier.py (Calculator 2)
	•	Corresponding Result: Theorem 5 & Table 5
	•	Identity: Verifies that for the 18 specific pairs $(P_i, P_j)$, the sums of $k$-th powers of 2-block sums are invariant for $k=1, 2, 3$.
	◦	$k=1: \sum (x+y)^1 = 272$
	◦	$k=2: \sum (x+y)^2 = 5,848$
	◦	$k=3: \sum (x+y)^3 = 141,032$
4. Product Square Sum Analysis
	•	File: product_square_pair_sum_verifier.py (Calculator 3)
	•	Corresponding Result: Section 6 (Further Observations)
	•	Description: Demonstrates the "breaking" of invariance at $S_{\text{prod}^2}$ and its congregation into 4 specific discrete values across the 18 pairs.
5. Uniqueness & Partition Proof
	•	File: complete_complementary_pair_verifier.py (Calculator 4)
	•	Corresponding Result: Theorem 5 (Complete Complementary Pair Theorem)
	•	Description: An exhaustive search verifier that proves the 36 tilings are uniquely and completely partitioned into 18 pairs satisfying all simultaneous algebraic identities.

🛠 Installation & Reproduction
Requirements
	•	Python 3.10+
	•	NumPy 1.23+
Bash

pip install numpy
Reproducing Paper Results
To reproduce the core proof of the paper (the unique 18-pair partition), execute:
Bash

python complete_complementary_pair_verifier.py
This script will output the confirmation of the 18 pairs and their respective invariant sums as presented in the final tables of the manuscript.

📄 Citation
If you use these verifiers or the tiling library in your research, please cite: