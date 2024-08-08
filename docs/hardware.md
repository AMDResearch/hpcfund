# System Overview

The HPC Fund Research Cloud consists of 40 high performance computing (HPC) servers attached to a unifying high-speed InfiniBand fabric supporting high-bandwidth, low-latency message passing for distributed-memory applications.  Each servers consists of dual-socket CPUs combined with multiple AMD Instinct MI series [accelerators](https://www.amd.com/en/graphics/instinct-server-accelerators).  The supporting operating system is [Rocky Linux](https://rockylinux.org). Additional details regarding the hardware configuration is summarized below.

## Compute servers

Each compute server consists of two [AMD EPYC&trade;](https://www.amd.com/en/processors/epyc-server-cpu-family) processors with access to 512 GB (or more) of main memory. High-speed user network connectivity for inter-node communication is accommodated by a [ConnextX-6](https://nvdam.widen.net/s/5j7xtzqfxd/connectx-6-infiniband-datasheet-1987500-r2) MT28908 Infiniband host channel adapter providing a maximum port speed of 200 Gb/s.   For accelerated analysis, each node also includes one or more [AMD Instinct&trade;](https://www.amd.com/en/products/accelerators/instinct.html) accelerators. Multiple generations of accelerators are available within the system with key characteristics highlighted as follows:
<!-- * [AMD MI100 Accelerator](https://www.amd.com/en/products/accelerators/instinct/mi100.html) 
  * Peak double-precision (FP64) performance of 11.5 TFLOPs
  * 32 GB of high bandwidth memory (HBM2e)
  * Peak GPU memory bandwidth 1.2 TB/s  
  * Form factor: PCIe Add-in Card
* [AMD MI210 Accelerator](https://www.amd.com/en/products/accelerators/instinct/mi200/mi210.html)
  * Peak double-precision (FP64) performance of 45.3 TFLOPs
  * 64 GB of high bandwidth memory (HBM2e)
  * Peak GPU memory bandwidth 1.6 TB/s
  Form factor: PCIe Add-in Card
* [AMD MI250 Accelerator](https://www.amd.com/en/products/accelerators/instinct/mi200/mi250.html)
  * Peak double-precision (FP64) performance of 43.3 TFLOPs (per GCD)
  * 64 GB of high bandwidth memory (HBM2e) (per GCD)
  * Peak GPU memory bandwidth 1.6 TB/s (per GCD)
  * Form factor: OAM Module -->

  ```{table} Table 1:  Hardware Overview of Available Node Types
| Accelerator       | Peak FP64 | HBM Capacity | HBM Peak B/W |            Host CPU                 | Host Memory |
| --------- | :------: | :---------: | :---------------: | :------------------------------------------: | :---: |
| [AMD MI100](https://www.amd.com/en/products/accelerators/instinct/mi100.html)  | 11.5 TFLOPs  |   32GB |   1.2 TB/s | 2 X EPYC 7V13 64-core | 512 GB |
| [AMD MI210](https://www.amd.com/en/products/accelerators/instinct/mi200/mi210.html)  | 45.3 TFLOPs  |   64GB |   1.6 TB/s | 2 X EPYC 7V13 64-core | 512 GB |
| [AMD MI250](https://www.amd.com/en/products/accelerators/instinct/mi200/mi250.html)  |  45.3 TFLOPs (per GCD) |  64GB (per GCD) |   1.6 TB/s (per GCD) | 2 X EPYC 7763 64-Core | 1.5 TB |
```

Note that one AMD MI250 accelerator provides two Graphics Compute Dies (GCDs) for which the programmer can use as two separate GPUs.

## File systems

Multiple shared file systems are available across the cluster.  These are provisioned by separate dedicated servers that aggregate a number of NVMe storage devices running the [WekaFS](https://docs.weka.io) software stack in order to provide a POSIX-compliant file system.

Each user has access to two primary storage locations: `$HOME` and `$WORK`. These are unique directories per user with quotas applied to prevent over-allocation of the file system. Upon login, the `$HOME` and `$WORK` environment variables will be set automatically to the correct paths and user's are encouraged to leverage these variables within their job scripts for convenience.  

<!---
## insert system architecture diagram (TODO)
-->

```{tip}
In addition to the standard `cd` command, a `cdw` convenience alias is provided in the default [BASH](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html) environment which can be issued to take a user directly to their work directory.
```

 Additional *temporary* storage is available during the lifetime of a job (see {doc}`jobs` for details on interacting with the resource management system.) This storage is not-shared across the cluster and any user contents will be removed at the conclusion of a user job.

A summary of the available file systems and their characteristics is provided in the table below:


| File System | Quota/Size | Type | Backups | Features |
| ----: | :--------: | :--: | :--: | --- |
|`$HOME` | 25GB | WekaFS | Yes (daily) |  Permanent storage accessible across the cluster.  Intended for housing source code, job scripts, smaller application inputs/outputs. Nightly snapshots are generated and retained for a maximum of **10 days**.|
| `$WORK` | 2TB (shared)  | WekaFS | No | Permanent storage accessible across the cluster.  Intended to provide storage for larger datasets and shared resources across a project team. Note that the storage quota is shared amongst all members of a particular project.|
| `$TMPDIR` | 100GB| XFS | No | Temporary storage that is unique to each assigned host during a user job.  |


