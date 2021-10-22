https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

The link above has some nice instructions.

1. Open Git Bash, the application.

2. Make a new ssh key. Use ed25519 not rsa256.

$  ssh-keygen -t ed25519 -C "jeremy.evert@swosu.edu"
Generating public/private ed25519 key pair.

3. Now you can cd into the .ssh folder
ADMIN+evertj@STF128-002 MINGW64 ~
$ pwd
/c/Users/evertj

ADMIN+evertj@STF128-002 MINGW64 ~
$ cd .ssh/

ADMIN+evertj@STF128-002 MINGW64 ~/.ssh
$ pwd
/c/Users/evertj/.ssh

4. You can use ls to look around. Here you can see the public key for ed15519


ADMIN+evertj@STF128-002 MINGW64 ~/.ssh
$ ls
id_ed25519  id_ed25519.pub  id_rsa  id_rsa.pub

5. now we make sure our agent is working with eval "$(ssh-agent -s)"

ADMIN+evertj@STF128-002 MINGW64 ~/.ssh
$ eval "$(ssh-agent -s)"
Agent pid 607

6. Next we add our ssh key to the agent.

ADMIN+evertj@STF128-002 MINGW64 ~/.ssh
$ ssh-add ~/.ssh/id_ed25519
Identity added: /c/Users/evertj/.ssh/id_ed25519 (jeremy.evert@swosu.edu)

ADMIN+evertj@STF128-002 MINGW64 ~/.ssh
$ ls
id_ed25519  id_ed25519.pub  id_rsa  id_rsa.pub

7. now we can print out our public key with cat id_ed25519.pub

ADMIN+evertj@STF128-002 MINGW64 ~/.ssh
$ cat id_ed25519.pub

copy and paste that long string into

github > settings > SSH and GPG keys > new key