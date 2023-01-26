# Directory roles

## Root filesystem
- /bin
  - Commands needed during bootup that might be used by normal users
- /sbin
  - Like /bin but the commands are not intended for normal users, although they may use them if necessary and allowed.
  - Usually the root's default path
- /etc
  - Configuration files specific to the machine
- /root
  - The home directory for user root. (Not accessible to other users on the system)
- /lib
  - Shared libraries needed by the programs on the root filesystem.
- /tmp
  - Temporary files.
- [Reference](https://tldp.org/LDP/sag/html/root-fs.html)

### etc directory
The /etc directory is contained in the root directory. It stores storage system configuration files, executables required to boot the system, and some log files
- [Reference](https://library.netapp.com/ecmdocs/ECMP1155684/html/GUID-06DD6AEA-FD2B-453C-8EBF-545FEE8C4CB0.html)

- /etc/profile, /etc/bash
  - Files executed at login or startup time by the BASH.
  - Allow the system administrator to set global defaults for all users.
  - Users can also create individual copies of these in their home directory to personalize their environment
    - Bash is a command processor that typically runs in a text window where the user types commands that cause actions. Bash can also read and execute commands from a file called a shell script

> Bash 는 command language 이다. Command 를 처리해 주고 shell script 라는 파일을 읽거나 명령을 실행할 수 있다.

- /etc/hosts
  - Just an address and a host name.
  - [Reference](https://unix.stackexchange.com/questions/421491/what-is-the-purpose-of-etc-hosts)
- Interactive shell
  - Used where a user can interact with the shell
- non-interactive shell
  - Used when a user cannot interact with the shell.
- /etc/profile
  - sets the environment variables at startup of the bash shell
  - Executed only for interactive shells
  - [Reference](https://unix.stackexchange.com/questions/64258/what-do-the-scripts-in-etc-profile-d-do)
- /etc/bashrc
  - Similar to profile but is executed for both interactive and non-interactive shells.
  - [Reference](https://askubuntu.com/questions/939736/what-is-the-difference-between-etc-profile-and-bashrc)

- [Reference](https://tldp.org/LDP/sag/html/etc-fs.html)