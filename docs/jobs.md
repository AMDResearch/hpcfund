# Running Jobs

The HPC Fund Research Cloud runs the [SLURM](https://slurm.schedmd.com/overview.html) workload resource manager in order to organize job scheduling across the cluster. In order to access back-end compute resources, users must submit jobs to SLURM (either interactive or batch) and the underlying scheduler will manage execution of all jobs using a [multi-factor](https://slurm.schedmd.com/priority_multifactor.html) priority algorithm.

Multiple partitions (or queues) are available for users to choose from and each job submission is associated with a particular partition request.  The table below summarizes available production queues and runlimits currently available:

| Queue     | Max Time | Max Node(s) | Charge Multiplier |                Configuration                 |
| --------- | :------: | :---------: | :---------------: | :------------------------------------------: |
| `devel`   | 30 min.  |      1      |        1X         | Targeting short development needs (4xMI100). |
| `mi1004x` | 24 hours |     16      |        1X         |       4 x MI100 accelerators per node.       |
| `mi1008x` | 24 hours |      4      |       1.5X        |       8 x MI100 accelerators per node.       |

Note that special requests that extend beyond the above queue limits may potentially be accommodated on a case-by-case basis.q

## Batch job submission

Example SLURM batch job submission scripts are available on the login node at `/opt/ohpc/pub/examples/slurm`.  A basic starting job for MPI-based applications is available in this directory named `job.mpi` and is shown below for reference:

```
#!/bin/bash

#SBATCH -J test               # Job name
#SBATCH -o job.%j.out         # Name of stdout output file (%j expands to jobId)
#SBATCH -N 2                  # Total number of nodes requested
#SBATCH -n 8                  # Total number of mpi tasks requested
#SBATCH -t 01:30:00           # Run time (hh:mm:ss) - 1.5 hours
#SBATCH -p mi1004x            # Desired partition

# Launch an MPI-based executable

prun ./a.out
```

Note that the `prun` utility included in the above job script is a wrapper script for launching MPI-based executables. In this example, 8 MPI tasks will be launched on two physical nodes, or 4 MPI tasks per node. This is a fairly common use case for the `mi1004x` partition where 1 MPI task is allocated per GPU accelerator.

```{tip}
SLURM batch submission scripts are just shell scrips - you can customize the script to perform various pre and post-processing tasks in addition to launching parallel jobs.
```

## Interactive usage
In addition to running batch jobs, you may also request an interactive session on one or more compute nodes.  This is convenient for longer compilations or when undertaking debugging and testing tasks where it is convenient to have access to an interactive shell.  To submit interactive jobs, the `salloc` command is used and the example below illustrates an interactive session submitted to the devel queue:

```
[test@login1 ~]$ salloc -N 1 -n 4 -p devel -t 00:30:00
salloc: ---------------------------------------------------------------
salloc: AMD HPC Fund Job Submission Filter
salloc: ---------------------------------------------------------------
salloc: --> ok: runtime limit specified
...
...
salloc: Granted job allocation 449
[test@t004-002 ~]$
```
When the above command is submitted on the login node, SLURM will queue the job and the prompt will temporarily hang until adequate resources are available. Once the scheduler has allocated resources,  your prompt will be updated to provide a login on the first assigned compute node. From here, you can run any shell commands until the maximum job runlimit is reached.  You can also launch parallel jobs interactively from within your allocation, for example:

```
[test@t004-002 ~]$ prun hostname
[prun] Master compute host = t004-002
[prun] Resource manager = slurm
[prun] Launch cmd = mpirun hostname (family=openmpi4)
t004-002.hpcfund
t004-002.hpcfund
t004-002.hpcfund
t004-002.hpcfund
```

```{tip}
To terminate an interactive job, simply type `exit` at your shell prompt.
```


## Compute node access
HPC Fund compute nodes are allocated in an **exclusive** fashion such that only a single user is on a node at any one time and is allocated all resources associated with the host (CPUs, host memory, GPUs, etc). Consequently, ssh access to back-end compute hosts are dynamically controlled with temporary access granted for the duration of a user's job.  The `squeue` command can be used to interrogate a running job and identify assigned hosts in order to gain ssh access. For example:

```
[test@login1 ~]$ squeue -j 451
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               451     devel interact     test  R       0:10      2 t004-[002-003]

[test@login1 ~]$ ssh t004-003
...
[test@t004-003 ~]$
```

## Command SLURM commands:

The table below highlights several of the more common user-facing SLURM commands. Consult the man pages (e.g. `man sbatch`) for more detailed information and command-line options for these utilities.

| Command | Purpose |
| ------- | ------- |
| sbatch  | submit a job for later execution |
| scancel | cancel (delete) a pending or running job |
| salloc  | allocate resources in real time (e.g. to request an interactive job) |
| sinfo   | report the state of partitions and nodes |
| squeue  | report the state of queue jobs |

## Job dependencies

TODO
