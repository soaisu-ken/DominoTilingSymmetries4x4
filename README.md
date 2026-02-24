# Domino Tiling Algebraic Symmetry & Classification Verifiers

This repository contains Python scripts to verify the combinatorial and algebraic properties of domino tilings in a $4 \times 4$ natural square, as presented in the paper:
**"Algebraic Symmetries and the 90-Degree Rotation Complementarity Theorem in Domino Tilings of the $4 \times 4$ Natural Square"** by Kenichi Takemura.

---

## 🔢 Calculator 0: Symmetry and Burnside's Lemma Verifier

This script (**calculator0_symmetry_check.py**) verifies the combinatorial and group-theoretic results presented in Theorem 2.

### Functionality
1. **Exhaustive Verification of Fixed Points:** It calculates $|\text{Fix}(g)|$ for each of the 8 elements of the dihedral group $D_4$ acting on the 36 tilings.
2. **Reproduction of Paper Results:** Confirms the 9 symmetry classes (families) as listed in Table 2.
3. **Pattern ID Mapping:** Explicitly maps each pattern (P1–P36) to its respective symmetry class and behavior under rotation/reflection.

---

## 🔢 Verifier No.1: 90-Degree Rotation Product Sum

Verifies the **"90-Degree Rotation Product Sum Complementarity Theorem"**.

### Verified Theorem
For all 36 patterns $P$:
$$S_{\text{prod}}(P) + S_{\text{prod}}(P^{90}) = 1,428$$
* **File:** `domino_tiling_rotation_verifier.py`

---

## 🔢 Verifier No.2: Power Sums of 2-Block Sums

Verifies the invariance of power sums $S_{\mathrm{sum}}^k(P) = \sum (x_i + y_i)^k$ for 18 specific pairs.

| $k$ | Identity (Invariant Sum) |
| :---: | :--- |
| **1** | $S_{\text{sum}}^1(P_i) + S_{\text{sum}}^1(P_j) = 272$ |
| **2** | $S_{\text{sum}}^2(P_i) + S_{\text{sum}}^2(P_j) = 5,848$ |
| **3** | $S_{\text{sum}}^3(P_i) + S_{\text{sum}}^3(P_j) = 141,032$ |
* **File:** `power_sum_verifier.py`

---

## 🔢 Verifier No.3: 2-Block Product Square Sum

Verifies that $S_{\mathrm{prod}^2}(P) = \sum (x_i y_i)^2$ congregates into four specific values for the 18 pairs.
$$S_{\text{prod}^2}(P_i) + S_{\text{prod}^2}(P_j) \in \{ 219,324, \ 219,444, \ 221,244, \ 221,364 \}$$
* **File:** `product_square_pair_sum_verifier.py`

---

## 🔢 Verifier No.4: Complete Complementary Pairs

Confirms that all 36 patterns are uniquely partitioned into 18 **Complete Complementary Pairs** satisfying all four algebraic metrics simultaneously.
* **File:** `complete_complementary_pair_verifier.py`

---

## 🛠 Installation & Usage

### Requirements
* Python 3.x
* NumPy

```bash
pip install numpy
Execution
Run any of the scripts from your terminal, for example:
Bash

python calculator0_symmetry_check.py