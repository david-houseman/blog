title: SSH credentials for GitHub
author: David Houseman
date: 2021-11-25

Beginning August 2021, GitHub has moved to token-based
authentication for command line git access. In other words,
passwords are no longer accepted.

The SSH public key/s can be uploaded to github in the Settings
-> SSH and GPG keys section of the github website. The accompanying
documentation for generating a key pair using `ssh-keygen` is
very clear and helpful.

The following data need to be added to ~/.ssh/config so that the ssh
client authenticates with github using the correct credentials.

    Host github.com
    User git
    IdentityFile ~/.ssh/id_rsa_github

It is helpful to test the connection using

    $ ssh -T github.com

and confirming that the correct key is used. After this change
`.git/config` so that the remote url uses `ssh` instead of `https`.
It should now be possible to `git pull`.
