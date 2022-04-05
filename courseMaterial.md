# scouthack: webdev v0.1

## install your software

1. connect to the network drive:

| windows                                         | linux                           | osx                            |
| ----------------------------------------------- | ------------------------------- | ------------------------------ |
| `this pc` -> `map network drive` (use     `s:`) | <kbd>ctrl </kbd> + <kbd>l</kbd> | <kbd>cmd </kbd> + <kbd>k</kbd> |
| \\\192.168.0.2\                                 | smb://192.168.0.2               | smb://192.168.0.2              |
|                                                 |                                 |

2. Make sure you have the following software packages installed:
- visual studio code (vscode)
- git
- a terminal application - you can check this using:

    linux: <kbd>menu</kbd>,  `terminal emulator`
    ```bash
    username@locahost:~$
    ```

    osx: <kbd>cmd</kbd> + <kbd>space</kbd> `terminal`,<kbd>return</kbd>
    ```bash
    username@locahost:~$
    ```

    win 10: <kbd>ctrl</kbd> + <kbd>r</kbd>, `cmd`, <kbd>enter<kbd>
    ``` powershell
    c:\users\username>
    ```
    > if you do not have a terminal for windows after trying this, or are using windows 7, please install `s:\win64\putty.exe`.

# Connect to the Development Server: `scouthack`

1. Open Visual Studio Code

2. Click the green icon on the bottom left of the screen.

    a. A text field will open up in the top of the screen, select the first option by hitting <kbd>Enter</kbd>:

    <kbd>Connect to Host...                     Remote-SSH</kbd>

Type your `firstname@192.168.0.2` (all lower case) and hit <kbd>Enter</kbd>.

`Select configured SSH host or enter user@host`:
```bash
yourname@192.168.0.2
```
Then hit <kbd>Enter</kbd>.


`Enter passphrase for ssh key`:
```bash
yourname
```
Then hit <kbd>Enter</kbd>.


# Coursework
### html
1. [ots reference](https://opentechschool.github.io/html-css-beginners/en/core/structure.html)
2. https://w3schools.com
3. https://www.w3.org/
### css
1. [ots reference](https://opentechschool.github.io/html-css-beginners/en/core/structure.html)
2. https://w3schools.com
3. https://www.w3.org/

### bootstrap
1. [bootstrap 4](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

### git

1. open vscode, and open a folder to store your development (dev) project.

2. go to the <kbd>source control</kbd> tab (third down on the left) and select `initialize repository` to start logging file changes.

    you'll see that you can add files to the staged changes. then, you can select <kbd>commit</kbd> where you'll be prompted to provide a comment for the commit; describe the commit, then, <kbd>commit</kbd>!

3. here's how it's done on the command line without using vscode

    ```bash
    # initialize your git repository
    $ git init

    # add files to your git repo
    $ git add .

    # save file changes to your local git repo
    $ git commit

    # add a connection to a remote repo
    $ git remote add origin git@scouthack.com:yourname/yourrepo.git

    # upload changes to the remote repo
    $ git push -u origin master
    ```

##  [the linux command line](https://ixpeering.dl.sourceforge.net/project/linuxcommand/tlcl/19.01/tlcl-19.01.pdf)

1. navigating a linux command line interface (cli)

```bash
#this is the prompt
yourname@scouthack:~$ _

# execute the following command as a superuser/administrator
yourname@scouthack:~$ sudo

# !! repeats the previous command entered as a superuser
yourname@scouthack:~$ sudo !!

# show contents of folder (flags -l, -a, -h)
yourname@scouthack:~$ ls -lah

# make a new folder (flag -p)
yourname@scouthack:~$ mkdir -p

# move to the current directory (folder)
yourname@scouthack:~$ cd .

# move up to the folder above
yourname@scouthack:~$ cd ..

# windows equivalent to "c:\"
yourname@scouthack:~$ cd /

# c:\documents\users\yourusername\ (windows)
# or
# /users/yourusername (macos)
yourname@scouthack:~$ cd ~
```

### installing system tools

1. system update and upgrade

    update your system with a list of available software that can be updated:

```bash
$ sudo apt update

hit:1 http://security.ubuntu.com/ubuntu focal-security inrelease
hit:2 http://archive.ubuntu.com/ubuntu focal inrelease
hit:3 http://archive.ubuntu.com/ubuntu focal-updates inrelease
hit:4 http://archive.ubuntu.com/ubuntu focal-backports inrelease
...
reading package lists... done
building dependency tree
reading state information... done
all packages are up to date.
$ _
```

then upgrade your software available in the list:

```
$ sudo apt upgrade
[sudo] password for yourname: _
    reading package lists... done
    building depedency tree
    reading state information... done
    calculating upgrade... done
    the following additional packages will be installed:
    ...
    suggested packages:
    ...
    the following new packages will be installed:
    ...
    0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
    need to get 00.0 mb of archives.
    after this operation, 00.0 mb of additional disk space will be used.
do you want to continue? [y/n] _
    preparing to unpack ...
    unpacking ...
    selecting previously unselected package ...
    ...
    setting up ____
    processing triggers for systemd (245.4-4ubuntu3.7) ...
    processing triggers for man-db (2.9.1-1) ...
    processing triggers for libc-bin (2.31-0ubuntu9.2) ...
$ _
```

> shortcut

> you can update and upgrade at the same time with one command using the <code>&&</code> tool and the <code>-y</code> flag to automaticaly approve prompts for installing software:

```bash
$ sudo apt update && sudo apt upgrade -y
```

2. install the following software to help us configure our server:
    - nano, a text editor for the command line, similar to notepad (windows) or textedit++ (macos).

        ```bash
        $ sudo apt install nano
        ```

    2. editing files in the cli

       ```bash
       $ nano foo    # notepad or textedit for the cli
       ```

## web servers

1. python

    ```python3
    $ python3 -m http.server
    ```

4. [lamp](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04)

    a. apache2

    install _apache2_ and its dependencies, auto confirm

    ```bash
    $ sudo apt install apache2 -y
    ```
    create a configuration (`.conf`) file to configure `yourname.scouthack.local` based off the template file `000-default.conf`

    ```bash
    $ sudo nano /etc/apache2/sites-available/your-site.conf
    ```

use `nano` to edit your `.conf` file to look like this:

```
gnu nano 4.8        /etc/apache2/sites-available/your-site.conf
```

```apache
<virtualhost *:80>
    # the servername helps direct the web server as to what the web
    # address being asked about is, and directs the request to the
    # documentroot path.

    servername yourname.scouthack.local
    serveralias yourname.scouthack.local

    # the documentroot directive tells apache where on your local
    # filesystem to look for files to serve to the internet

    documentroot /var/www/html/yourname.scouthack.local/site/

    # create entries for where log files should be stored.

    errorlog ${apache_log_dir}/error.log
    customlog ${apache_log_dir}/access.log combined
</virtualhost>
```

            ```
            ^g get help     ^o write out    ^w where is     ^k cut text     ^j justify      ^c cur pos      m-u undo        m-a mark text
            ^x exit         ^r read file    ^\ replace      ^u paste text   ^t to spell     ^_ go to line   m-e redo        m-6 copy text
            ```

            hold <kbd>ctrl</kbd>+<kbd>o</kbd> to `^o write out`, or save your file, then <kbd>ctrl</kbd>+<kbd>x</kbd> to `^x exit`

            ```bash
            sudo mkdir -p /var/www/html/yourname.scouthack.local/site/
            sudo a2ensite yourname.scouthack.local.conf
            sudo service apache2 start
            ```

6. making stuff happen: scripting with php
```php
<?php info ?>
```

6. django
7. wordpress
8. things we missed that you might want to know:
    1. ip address mapping using bind9
    2. building more features into your django site
    3. customising your wordpress installation
    4. javascript!
