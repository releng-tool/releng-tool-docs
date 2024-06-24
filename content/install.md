# Installation

The recommended method of installing/upgrading releng-tool is using
[pipx][pipx]:

```shell
pipx install releng-tool
 (or)
python -m pipx install releng-tool
```

If pipx is not available, users may use [pip][pip] instead:

```shell
pip install -U releng-tool
 (or)
python -m pip install -U releng-tool
```

To verify the package has been installed, the following command can be used:

```shell
releng-tool --version
 (or)
python -m releng-tool --version
```

## Quick-start

The following provides a series of steps to assist in preparing a new
environment to use this package.

`````{tab} Linux
```{eval-rst}
.. only:: latex

    Linux
    -----
```

While the use of [Python][python]/[pip][pip] is almost consistent between
Linux distributions, below is a series of helpful steps to install
this package under specific distributions of Linux. From a terminal,
invoke the following commands:

````{tab} Arch
```{eval-rst}
.. only:: latex

    **Arch**
```
Using `pipx`:
```shell-session
$ sudo pacman -Syu
$ sudo pacman -S python-pipx
$ pipx ensurepath
$ pipx install releng-tool
$ releng-tool --version
releng-tool <version>
```

Using `pip`:
```shell-session
$ sudo pacman -Sy
$ sudo pacman -S python-pip
$ sudo pip install -U releng-tool
$ releng-tool --version
releng-tool <version>
```

This package is also [available on AUR][releng-tool-aur].
````

````{tab} CentOS
```{eval-rst}
.. only:: latex

    **CentOS**
```
```shell-session
$ sudo yum install epel-release
$ sudo yum install python-pip
$ sudo pip install -U releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} Fedora
```{eval-rst}
.. only:: latex

    **Fedora**
```
Using `pipx`:
```shell-session
$ sudo dnf install pipx
$ pipx ensurepath
$ pipx install releng-tool
$ releng-tool --version
releng-tool <version>
```

Using `pip`:
```shell-session
$ sudo dnf install python-pip
$ sudo pip install -U releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} openSUSE
```{eval-rst}
.. only:: latex

    **openSUSE**
```
Using `pip`:
```shell-session
$ pip install -U releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} Ubuntu
```{eval-rst}
.. only:: latex

    **Ubuntu**
```
Using `pipx` (Ubuntu 23.04 or above):
```shell-session
$ sudo apt update
$ sudo apt install pipx
$ pipx ensurepath
$ pipx install releng-tool
$ releng-tool --version
releng-tool <version>
```

Using `pip`:
```shell-session
$ sudo apt update
$ sudo apt install python-pip
$ sudo pip install -U releng-tool
$ releng-tool --version
releng-tool <version>
```
````
`````

````{tab} OS X
```{eval-rst}
.. only:: latex

    OS X
    ----
```
From a terminal, invoke the following commands if using `pipx`:

```shell-session
$ brew install pipx
$ pipx ensurepath
$ pipx install releng-tool
$ releng-tool --version
releng-tool <version>
```

Or, if using `pip`:

```shell-session
$ sudo easy_install pip
$ sudo pip install -U releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} Windows
```{eval-rst}
.. only:: latex

    Windows
    -------
```

If not already installed, download the most recent version of [Python][python]:

> Python - Downloads\
> <https://www.python.org/downloads/>

When invoking the installer, it is recommended to select the option to
"Add Python to PATH". However, users can explicitly invoked Python from
an absolute path (the remainder of these steps will assume Python is
available in the path).

Open a Windows command prompt and invoke the following:

```doscon
> python -m pip install -U releng-tool
> python -m releng-tool --version
releng-tool ~version~
```
````

## Development

To install the most recent development sources, the following [pip][pip]
command can be used:

```shell
pip install git+https://github.com/releng-tool/releng-tool.git
```


[pip]: https://pip.pypa.io/
[pipx]: https://pipx.pypa.io/
[python]: https://www.python.org/
[releng-tool-aur]: https://aur.archlinux.org/packages/releng-tool/
