# System Architecture

## Clients

Students are each given a laptop running Xubuntu, with Firefox, and Visual Studio Code and a small collection of extensions installed.

The laptop image exists as a CloneZilla image which can deployed to all laptops via multicast.

The main extension required for VS Code is the "Remote - SSH" extension.

## Server

The server is running some variant of Debian, Docker, dnsmasq, and a few other things.

There is code which, given a list of users, spins up a Docker Debian container for each of them, with their own user account and root access. The SSH component is managed by sshpiper, which literally person-in-the-middles the SSH connection and forwards it to the correct container based on the username used to authenticate.

Scouts can then use VS Code to SSH to the container and drop files there.

Each container has port 80 exposed to the LAN via http://username.scouthack via rules within a Traefik proxy, so that each scout can browse to their own (and others') local website.
