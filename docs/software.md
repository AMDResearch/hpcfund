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

## Python on HPC Fund

A base Python installation is available on the HPC Fund cluster which includes a handful of common packages (e.g., `numpy`, `pandas`). If additional packages are needed, users can customize their environments by installing packages with a user install, creating a Python virtual environment to install packages in, or loading a module for a specific package (e.g., `pytorch`, `tensorflow`). Examples of each method are given below.

### Python user installs

Users can install additional Python packages to their local environment using the `--user` flag to `pip install`, which (by default) installs the packages to their `~/.local` directory. User installations can be performed as follows:

```
$ python -m pip install --user <package-name>
```

### Python virtual environments

While user installs do allow for custom environments, virtual environments are more flexible when working on multiple Python projects. Instead of installing additional packages in e.g., `~/.local`, the packages are compartmentalized within the virtual environment, which can be helpful if different projects require different packages (or versions of packages). A virtual environment can be created as follows:

```
$ python -m venv <path-to-venv>/<name-of-venv>
```

Then, the virtual environment can be activated as follows:

```
$ source <path-to-venv>/<name-of-venv>/bin/activate

(<name-of-venv>) $
```

While activated, the name of the virtual environment is shown in parentheses before the prompt. By default, the newly created virtual environment will simply include `pip` and `setuptools`; this can be seen by issuing the command `pip list` once the virtual environment has been activated. If a user would like to create a virtual environment with the packages included in the base Python environment already available, an additional flag can be given, `--system-site-packages`:

```
$ python -m venv --system-site-packages <path-to-venv>/<name-of-venv>
```

After activating the virtual environment, `pip list` will show that the packages from the base Python environment are available. Once a virtual environment has been created and activated, additional packages can be installed within it with e.g., `pip`. To deactivate the environment, simply issue the command `deactivate`.

### AI framework modules

For AI workloads, users are provided with `pytorch` and `tensorflow` modules that simply extend the base Python environment by adding to the `PATH` and `PYTHONPATH` environment variables to point to the additional packages. E.g., 

```
$ module load pytorch
```

Users who wish to build virtual environments on top of these AI framework modules need to make sure that 1) while creating the virtual environment, the module(s) is loaded and the `--system-site-packages` flag is used, and 2) the module(s) is also loaded while the virtual environment is activated. 

