# DS-A2 | Inference and Uncertainty Notebook

## Project
Reproducible submission for DS-A2 on FVC2004 federated fingerprint verification.

## Estimand
psi_Fed = (1/K) * sum_k (genuine_rate_k - impostor_rate_k)
with K = 20 clients keyed by `database::finger_id`.

## Hypotheses
- H0: psi_Fed = 0
- H1: psi_Fed > 0
- MME: psi_Fed = 0.15

## Dataset
FVC2004 DB1_B and DB2_B. Academic use only.

## Reproduction
1. Install from environment.yml.
2. Open notebooks/ds_a2_inference.ipynb.
3. Run top to bottom.

## Scope
Associational and inferential. Not causal.
