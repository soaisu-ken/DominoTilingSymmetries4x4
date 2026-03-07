Domino Tiling Algebraic Symmetry & Classification Verifiers
This repository provides the official implementation of the Computational Verification Protocol described in the paper:
"Algebraic Symmetries and the 90-Degree Rotation Complementarity Theorem in Domino Tilings of the $4 \times 4$ Natural Square" by Kenichi Takemura.
🛡️ Computational Verification Protocol
To ensure mathematical rigor and reproducibility, these scripts follow a formal verification protocol:
	1	Normalization (Canonical Form): All 36 tilings are stored in a canonical integer matrix format. ID labels (0–7) are reassigned using a row-major normalization function to eliminate duplicates and labeling artifacts.
	2	Population Completeness: The set of 36 tilings is verified against Kasteleyn’s formula ($\sqrt{|\det A|} = 36$). Symmetry closure under the $D_4$ group is confirmed via Burnside's Lemma.
	3	Existence & Multiplicity Analysis: Beyond verifying pairwise identities, this protocol enumerates all possible valid partitions. It proves that while a perfect complementary partition always exists, there are exactly 12 distinct ways to achieve it.
🔢 Script Mapping & Functionality
0. Population & Symmetry Audit
	•	File: calculator0_symmetry_check.py
	•	Corresponding Result: Theorem 2 & Table 2
	•	Description: Verifies the 8 elements of the dihedral group $D_4$ acting on the 36 tilings. It confirms the 9 symmetry classes (families) and the count of fixed points for each transformation.
1. 90-Degree Rotation Verifier
	•	File: Domino Tiling Calculator1.py
	•	Corresponding Result: Theorem 3 (90-Degree Rotation Product Sum Theorem)
	•	Identity: $S_{\text{prod}}(P) + S_{\text{prod}}(P^{90}) = 1,428$ for all $P \in \mathcal{P}$.
2. Power Sums of 2-Block Sums
	•	File: Domino Tiling Calculator2.py
	•	Corresponding Result: Theorem 5 & Table 5
	•	Identity: Verifies that for the 18 specific pairs $(P_i, P_j)$, the sums of $k$-th powers of 2-block sums are invariant for $k=1, 2, 3$.
	◦	$k=1: \sum (x+y)^1 = 272$
	◦	$k=2: \sum (x+y)^2 = 5,848$
	◦	$k=3: \sum (x+y)^3 = 141,032$
3. Product Square Sum Analysis
	•	File: Domino Tiling Calculator3.py
	•	Corresponding Result: Section 6 (Further Observations)
	•	Description: Demonstrates the "breaking" of invariance at $S_{\text{prod}^2}$ and its congregation into 4 specific discrete values across the 18 pairs.
4. Integrated Partition Verifier
	•	File: Domino Tiling Calculator4.py
	•	Corresponding Result: Theorem 5 (Algebraic Perfect Complementary Partition)
	•	Description: An integrated verifier that confirms the 36 tilings can be partitioned into 18 pairs satisfying all simultaneous algebraic identities described in the paper.
5. Multiplicity & Enumeration Proof
	•	File: enumerate_all_partitions.py
	•	Corresponding Result: Theorem 5.5 (Multiplicity of Partitions)
	•	Description: Uses a graph-theoretical approach to enumerate all valid perfect matchings. It proves the multiplicity is exactly 12, derived from the product of internal matching possibilities of specific subgraphs ($K_4$ and $K_{2,2}$).
🛠 Installation & Reproduction
Requirements
	•	Python 3.10+
	•	NumPy 1.23+
Bash

pip install numpy
Reproducing Results
To reproduce the core proof of the multiplicity (12 partitions), execute:
Bash

python enumerate_all_partitions.py

