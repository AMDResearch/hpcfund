# Node-Hour Estimates

The AMD University Program (AUP) AI & HPC Cluster supports **academic AI and HPC research and education** through year-long node-hour allocations, awarded quarterly to university faculty leading innovative, impactful, open-source projects. 

When submitting a proposal, you will estimate the node-hours your project needs **in each partition** (i.e., node type; see Table 1) over a **1-year period**, which will then be normalized into a single node-hour allocation.

This guide explains how to prepare those estimates when completing the proposal (Step 3 of our 3-Step process):  
[https://www.amd.com/en/corporate/university-program/ai-hpc-cluster.html#apply](https://www.amd.com/en/corporate/university-program/ai-hpc-cluster.html#apply)

---
## Available Partitions and Capacity

**Table 1. Partitions, charge factors, and approximate annual and quarterly capacity**

| Partition | GPUs<br>per node | GPU type            | Number<br>of nodes | Charge<br>factor | ~Annual<br>node-hours |
| --------- | ------------- | ------------------- | --------------- | ------------- | ---------------------------- |
| mi3508x   | 8             | AMD Instinct MI350X | 4               | 1.40          | ~33,000                      |
| mi3501x   | 1             | AMD Instinct MI350X | 8               | 0.175         | ~67,000                      |
| mi3258x   | 8             | AMD Instinct MI325X | 1               | 1.20          | ~8,000                       |
| mi3008x   | 8             | AMD Instinct MI300X | 2               | 1.00          | ~17,000                      |
| mi3001x   | 1             | AMD Instinct MI300X | 8               | 0.125         | ~67,000                      |
| mi2508x   | 8             | AMD Instinct MI250  | 10              | 0.80          | ~83,000                      |
| mi2104x   | 4             | AMD Instinct MI210  | 11              | 0.40          | ~92,000                      |
| mi2101x   | 1             | AMD Instinct MI210  | 28              | 0.10          | ~233,000                     |

- Approximate annual node-hours in this table reflect total usable capacity across the entire cluster and are shared among all projects. 

- The [1x] partitions represent virtual “slice” nodes that use a fraction (1/8 or 1/4) of a physical node’s resources; charge factors reflect this proportional usage.

- Each quarter, we allocate ~1/4 of our total annual node-hour capacity to multiple new projects.

---
## What to Provide in the Proposal

Include an **estimate of the node-hours needed by partition** (i.e., by node type; see Table 1). Enter zeros for partitions you do not plan to use.

- A **node-hour** is the accounting unit used to allocate compute usage. Node-hours are consumed based on the number of nodes used and the run time (e.g., 4 nodes × 25 hours = 100 node-hours).
- These are planning estimates for the full allocation period of 1 year.

---
## How Allocations Are Calculated

Each partition has a charge factor reflecting relative capability and availability. Your per-partition requests will be converted into a single normalized node-hour allocation using these factors.

**PIs do not need to perform normalization**; simply provide the actual node-hours needed per partition.

Key points:
- You receive one total allocation, not fixed per-partition limits.
- Higher-capability partitions consume the total allocation more quickly.
- You may shift usage across partitions during the year, as long as the total usage remains within the awarded allocation.

---
## Hardware Selection Guidance

General guidance on hardware capabilities:
- **MI350X / MI325X** – largest memory capacity; suited for very large or memory-constrained models.
- **MI300X** – high-performance general-purpose accelerator for modern ML workloads.
- **MI250 / MI210** – well-suited for development, testing, and compute-intensive workloads with smaller memory footprints.

Projects that effectively combine MI200- and MI300-series usage are generally able to **receive larger total allocations**.

---
## MI3XX Usage Considerations

MI3XX-class nodes (MI300X, MI325X, MI350X) are a limited shared resource.

During allocation review, the following guidelines are considered (in addition to scientific merit and impact):
- Requests **≤2%** of a partition’s **annual capacity** are typically straightforward to support.
- Requests between **3–9%** of a partition’s **annual capacity** require a clear technical rationale and strong expected impact.
- Requests **≥10%** of a partition’s **annual capacity** are typically not considered.

---
## Justification

Provide a brief justification of your node-hour estimates in the proposal form. Focus on technical requirements (e.g., memory footprint, model size, precision needs) and prior experience with comparable workloads.

---
## Summary (quick reference)

- Provide annual node-hour estimates by partition.
- MI3XX capacity is limited and shared.
- Mixed MI200/MI300 usage enables larger total allocations.
- Hardware usage may evolve within the awarded total.

