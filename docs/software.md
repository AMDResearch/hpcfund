# Software

The HPC Fund Research Cloud uses [Lmod](https://github.com/TACC/Lmod) to manage the software user-environment.  With a default login shell, users will have a number of different modules pre-loaded as highlighted below. 

```
[test@login1 ~]$ module list

Currently Loaded Modules:
  1) autotools    4) gnu12/12.2.0     7) hpcfund
  2) prun/2.3     5) ucx/1.14.0
  3) rocm/5.4.2   6) openmpi4/4.1.5
```
This default stack provides an MPI compiler and the [ROCm](https://www.amd.com/en/graphics/servers-solutions-rocm) toolchain to enable GPU application development using the HIP programming model. [HIP](https://docs.amd.com/bundle/HIP-Programming-Guide-v5.4/page/Introduction_to_HIP_Programming_Guide.html) is a  dialect of C++ supported by the ROCm toolchain to implement highly tuned workloads on AMD Instinct accelerators 

## Lmod commands 

The Lmod system provides a flexible mechanism to manage your local software environment. The table below highlights some common Lmod commands and their purpose. Note that these commands can be used interactively, or directly within a SLURM job script.

| Command | Purpose |
| ------- | ------- |
| module list  | see the modules currently loaded|
| module avail | see all modules that are compatible to be loaded |
| module purge  | unload all modules |
| module load \<package\> | load a new module named \<package\> |
| module unload \<package\> | unload the module named \<package\> |
| module load hpcfund   | restore default login environment (typically used after `module purge`) |
| module show \<package\> | show the variables set by a particular modulefile |

```{tip}
The `module help` command can also be run locally on the system to get more information on available Lmod options and sub-commands.
```