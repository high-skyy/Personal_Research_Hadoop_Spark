# SSH(Secure Shell)
- Brief : network protocol that gives users, particularly system administrators, a secure way to access a computer over an unsecured network.

## How it works
- SSH key relies upon the use of two related keys : (public key and private key)
  - public key의 경우 모두가 알고 있다.
  - private key의 경우 user 혼자만 알고 있다.

- Public key is used by both the user and the remote server to encrypt messages.
  - On the remote server side, it is saved in a file that contains a list of authorized public keys.
  - On the user's side, it is stored in SSH key management software or in a file on their computer.

### Procedure
1. User or a process requests a connection to the remote server.
2. challenge-response sequence is initiated.
3. The server sends an encrpyted challenge request using public key(private key를 가지고 해독 가능)
4. The user decrypts the key and responds back to the server.
5. Correct -> granted access.


## Details
- provides strong password authentication and public key.
- used to manage systems and applications remotely, enabling them to log in to another computer over a network.
  - execute commands and move files from one computer to another.
> system management를 원격으로 가능하게 해준다. (log in command execution move files 기능)
- client-server model
  - Secure Shell client application(Session의 display)을 ssh server(Session의 execution이 일어나는 곳)와 연결
    - Session : the total time devoted to an activity

- SSH를 ID와 PW를 가지고 security를 보장할 수 있지만 public key pair를 가지고 서로를 인증한다.
  - 각 host마다 unique한 public key pair를 generation 시킨다.
  - Session이 일어나기 위해서는 두 개의 public key가 필요하다.
    - authenticate the remote machine to the local machine.
    - authenticate the local machine to the remote machine.

## Details for implementation
1. Enter the key gen command $ ssh-keygen -t rsa
2. Enter file in which to save the keys. (Typically stored in ~/.ssh/directory...)
3. Put the public key to the remote server
4. System administrator can copy the public key into the remote server's authorized_keys file using (ssh-copy-id username@IP address)
5. Alternatively, you can paste in the keys using secure shell command
  - (e.g. $ cat ~/.ssh/id_rsa.pub | ssh username@IP address "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys").

## Commands
```
# 처음 접근하는 경우 user(접근하는 사람)의 local system's known_hosts file에 접근당하는 host key가 저장된다. (/.ssh/known_hosts , user's home directory)에 저장됨
# 저장된 이후에는 바로 접근을 할 수 있음.
$ ssh UserName@SSHserver.example.com      # connect to a remote host (for a terminal session)

# initiates the SSH server, which waits for incoming requests and enables authorized systems to connect to the local host.
$ sshd                               

# program to create a new authentication keypair for SSH
$ ssh-keygen

# program used to copy, install and configure an SSH key on a server to automate passwordless logins
$ ssh-copy-id

# used to add a key to the SSH authentication agent and is used with ssh-agent
$ ssh-add

# program used for copying files from one computer to another and is an SSH-secured version of rcp
$ scp
```

## Reference
- [Reference](https://www.techtarget.com/searchsecurity/definition/Secure-Shell)
- [Reference](https://sectigo.com/resource-library/what-is-an-ssh-key)