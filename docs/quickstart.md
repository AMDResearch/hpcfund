# Quick-Start Guide

Welcome to the **AMD University Program (AUP) AI & HPC Cluster**! This guide will help you get up and running quickly.
For comprehensive documentation, please explore the full site.

---

## 1. Cluster Hardware

```{seealso}
[Compute Servers Section](compute-servers)
```

### Compute Nodes

#### Multi-GPU Nodes

| Nodes | CPUs                          | GPUs                 | DRAM           |
|:-----:|-------------------------------|----------------------|----------------|
| 4     | [2x] 128-core EPYC 9755       | [8x] MI350X 288 GB   | 3072 GB DDR5   |
| 1     | [2x] 128-core EPYC 9755       | [8x] MI325X 256 GB   | 3072 GB DDR5   |
| 2     | [2x] 96-core EPYC 9684X       | [8x] MI300X 192 GB   | 2304 GB DDR5   |
| 10    | [2x] 64-core EPYC 7763        | [4x] MI250 128 GB    | 1536 GB DDR4   |
| 21    | [2x] 64-core EPYC 7V13        | [4x] MI210 64 GB     | 512 GB DDR4    |

#### Single-GPU Nodes (Virtual)

| Nodes | CPUs                          | GPU                  | DRAM           |
|:-----:|-------------------------------|----------------------|----------------|
| 8     | 16 cores of EPYC 9755         | [1x] MI350X 288 GB   | 334 GB DDR5    |
| 8     | 16 cores of EPYC 9684X        | [1x] MI300X 192 GB   | 238 GB DDR5    |
| 28    | 16 cores of EPYC 7V13         | [1x] MI210 64 GB     | 64 GB DDR4     |

```{note}
**MI350X** will be deployed starting in Q2 2026. The `mi3508x` and `mi3501x` partitions will have charge factors of 1.4 and 0.175, respectively.
```

### Login Node

| Nodes | CPUs                          | GPUs                 | DRAM           |
|:-----:|-------------------------------|----------------------|----------------|
| 2     | [2x] 64-core EPYC 7V13        | [2x] MI210 64 GB     | 512 GB DDR4    |

```{warning}
The login node is shared by **all** users. Do **not** run compute-intensive workloads on it.
Use Slurm to submit jobs to compute nodes instead.
```

---

## 2. Logging In

Connect via SSH, replacing `<username>` with your assigned username:

```bash
ssh <username>@hpcfund.amd.com
```

---

## 3. Storage Areas

```{seealso}
[File Systems Section](file-systems)
```

You have two storage areas available:

| Variable | Path                             | Description                                    | Capacity                                  |
|----------|----------------------------------|------------------------------------------------|-------------------------------------------|
| `$HOME`  | `/home1/<username>`              | Your personal home directory                   | 25 GB                                     |
| `$WORK`  | `/work/<projectid>/<username>`   | Your directory within your project's workspace | 2 TB default (shared across project members) |

---

## 4. Software & Programming Environment

```{seealso}
[Software Section](#software)
```

We use [Lmod](https://lmod.readthedocs.io/) to manage software modules. Key commands:

```bash
module avail          # List all available packages
module list           # Show currently loaded packages
module load <pkg>     # Load a package (e.g., module load hdf5)
module unload <pkg>   # Unload a package
```

### Setting Up PyTorch (Recommended for AI Workloads)

While a ROCm-enabled PyTorch module is available via Lmod, we recommend installing your own
for greater flexibility. Here's how using a Python virtual environment:

```bash
python3 -m venv <name-of-venv>
source <name-of-venv>/bin/activate
pip3 install --upgrade pip
pip3 install torch torchvision \
    --index-url https://download.pytorch.org/whl/rocm7.2

# Install any additional packages you need
# pip3 install transformers datasets accelerate ...
```

```{tip}
Installing your own PyTorch environment gives you full control over versions and
additional dependencies without waiting for system-wide module updates.
```

---

## 5. Running Jobs

```{seealso}
[Running Jobs](#jobs)
```

We use [Slurm](https://slurm.schedmd.com/) for job scheduling. Two primary modes:

- **Batch Jobs** *(preferred for most workloads)*:
  [Batch Job Submission Guide](batch-jobs)

- **Interactive Jobs** *(for quick testing & debugging)*:
  [Interactive Usage Guide](interactive-jobs)

---

## 6. Jupyter

```{seealso}
[Jupyter Section](jupyter)
```

We provide a helper script to launch JupyterLab sessions that tunnel to your local browser.

```{tip}
You can replace `jupyter notebook` with `jupyter lab` in the script if you prefer
the full JupyterLab interface.
```

---

## 7. ROCm Profiling & Debugging Tools

If you're coming from the NVIDIA ecosystem, here's a mapping of equivalent AMD ROCm tools:

| AMD Tool                 | NVIDIA Tool    | Reference                                                                          |
|--------------------------|----------------|------------------------------------------------------------------------------------|
| ROCm Compute Profiler    | Nsight Compute | [Documentation](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/) |
| ROCm Systems Profiler    | Nsight Systems | [Documentation](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/latest/) |
| `rocprof`                | `nvprof`       | Run `rocprof -h`                                                                   |
| `rocm-smi` / `amd-smi`   | `nvidia-smi`   | Run `amd-smi -h`                                                                   |

---

## 8. Getting Help

### GitHub Issues

The primary support channel for help requests and technical issues is to submit a GitHub issues on our companion GitHub site: [github.com/AMDResearch/hpcfund](https://github.com/AMDResearch/hpcfund)

```{tip}
If you would like to receive announcements and notifications related to the cluster (e.g., system down times), go to the GitHub site, click the Watch button at the top-right, and select All Activity (or Custom → Discussions). Make sure your GitHub notification settings have email delivery enabled."
```

### Email

For general questions about the AUP AI & HPC Cluster program or your project, please send emails to: [hpc.fund@amd.com](mailto:hpc.fund@amd.com)

---

## 9. Additional Resources

### Hardware

- [AMD Instinct MI350X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi350x.html)
- [AMD Instinct MI355X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)
- [AMD Instinct MI325X](https://www.amd.com/en/products/accelerators/instinct/mi300/mi325x.html)
- [AMD Instinct MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html)
- [AMD Instinct MI300A](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300a.html)

### Software & Documentation

- [ROCm for AI](https://www.amd.com/en/products/software/rocm/ai.html)
- [ROCm for HPC](https://www.amd.com/en/products/software/rocm/hpc.html)
- [ROCm Documentation](https://rocm.docs.amd.com/en/latest/)
- [ROCm API Libraries](https://rocm.docs.amd.com/en/latest/reference/api-libraries.html)
- [ROCm CMake Packages](https://rocm.docs.amd.com/en/latest/conceptual/cmake-packages.html)
- [Containers & Deployment Guides](https://www.amd.com/en/developer/resources/infinity-hub.html)

### Learning & Tutorials

- [AMD AI Academy](https://www.amd.com/es/developer/resources/training/amd-ai-academy.html)
- [AMD Developer Program](https://www.amd.com/en/developer/ai-dev-program.html)
- [ROCm Blog](https://rocm.blogs.amd.com/)
- [Self-Guided AI Tutorials](https://rocm.blogs.amd.com/applications-models.html)
- [ROCm AI Developer Hub](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/)
- [ROCm HPC Tutorials (AMD Lab Notes)](https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-readme/)
- [ROCm Training Videos](https://www.amd.com/en/developer/resources/rocm-hub/training-videos.html)

