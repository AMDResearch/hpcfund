# System Access

Remote access to the HPC Fund Research Cloud is supported via the standard [secure shell](https://en.wikipedia.org/wiki/Secure_Shell) (ssh) protocol. For access, users will need to use a local ssh client on their laptop or workstation; these are available by default on Linux and Mac OS systems.   If connecting from Windows, there are a number of 3rd party clients available including [Putty](https://www.putty.org) and [SecureCRT](https://www.vandyke.com/products/securecrt/). Alternatively, Windows users may want to consider enabling the Windows Subsystem for Linux ([WSL](https://learn.microsoft.com/en-us/windows/wsl/install)) to gain access to an embedded Linux distribution and command-line tools (including an ssh client) alongside your traditional Windows desktop and apps.

## Login node

To initiate a connection to the login node, issue the following where *username* is replaced with your assigned userid.

```
localhost$ ssh username@hpcfund.amd.com
```

## Key-based access

Prior to accessing the system for the first time, each user will need to first share their **public** ssh key with system administrators. SSH keys are used to authenticate and establish an encrypted communication channel between a client and the remote host.

## Terminal multiplexers

Remote users may find it convenient to run a terminal multiplexer on the login node to accommodate reconnecting to a persistent shell and avoid local network interruptions.  Two such options are available on the login node(s):
* [tmux](https://github.com/tmux/tmux/wiki/Getting-Started)
* [screen](https://www.gnu.org/software/screen/)

## Usage

Cluster login node(s) are shared among all users and are provided as an external access point to system's analysis back-end. The login nodes provide an interactive environment for code compilation, editing, limited pre- and post-processing, and an avenue to interact with the resource manager.

**Do Not Run Jobs on the Login Nodes**

Do not run long-running applications or perform intensive computational activity on the login nodes. Your account may be suspended and you will lose access to the queues if you do not adhere to this policy and your actions are impacting other users.  Instead, submit long running batch jobs to SLURM or obtain an interactive session on a compute node for dedicated resources (see {doc}`jobs` for more info).
