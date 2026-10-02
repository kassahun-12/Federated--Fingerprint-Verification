# Data Dictionary

| Variable | Type | Role |
|---|---|---|
| database | categorical | grouping / client key |
| finger_id | categorical | client key |
| impression_id | numeric | within-client repetition |
| filename | identifier | excluded |
| path | identifier | excluded |
| size_bytes | numeric | anomaly check |
| client_key | categorical | database::finger_id |
| score | numeric | match score |
| pair_type | categorical | genuine / impostor |
| rd_k | numeric | per-client risk difference |
