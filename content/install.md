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

While the use of [Python][python]/[pipx][pipx] is almost consistent between
Linux distributions, below is a series of helpful steps to install
this package under specific distributions of Linux. From a terminal,
invoke the following commands:

````{tab} Alpine
```{eval-rst}
.. only:: latex

    **Alpine**
```

```shell-session
# apk add pipx
# pipx install --global releng-tool
# releng-tool --version
releng-tool <version>
```

Using `dosas`:
```shell-session
$ doas apk add pipx
$ doas pipx install --global releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} Arch
```{eval-rst}
.. only:: latex

    **Arch**
```

```shell-session
# pacman -S python-pipx
# pipx install --global releng-tool
# releng-tool --version
releng-tool <version>
```

Using `sudo`:
```shell-session
$ sudo pacman -S python-pipx
$ sudo pipx install --global releng-tool
$ releng-tool --version
releng-tool <version>
```

This package is also [available on AUR][releng-tool-aur].
````

````{tab} Debian
```{eval-rst}
.. only:: latex

    **Debian**
```
```shell-session
# apt-get install -y pipx
# pipx install --global releng-tool
# releng-tool --version
releng-tool <version>
```

Using `sudo`:
```shell-session
$ sudo apt-get install -y pipx
$ sudo pipx install --global releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} Fedora
```{eval-rst}
.. only:: latex

    **Fedora**
```
```shell-session
# dnf install -y pipx
# pipx install --global releng-tool
# releng-tool --version
releng-tool <version>
```

Using `sudo`:
```shell-session
$ sudo dnf install pipx
$ sudo pipx install --global releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} openSUSE
```{eval-rst}
.. only:: latex

    **openSUSE**
```
```shell-session
# zypper install -y python3-pipx
# pipx install --global releng-tool
# releng-tool --version
releng-tool <version>
```

Using `sudo`:
```shell-session
$ sudo zypper install -y python3-pipx
$ sudo pipx install --global releng-tool
$ releng-tool --version
releng-tool <version>
```
````

````{tab} Ubuntu
```{eval-rst}
.. only:: latex

    **Ubuntu**
```
```shell-session
# apt-get install -y pipx
# pipx ensurepath
# pipx install releng-tool
# releng-tool --version
releng-tool <version>
```

Using `sudo`:
```shell-session
$ sudo apt-get install -y pipx
$ pipx ensurepath
$ pipx install releng-tool
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

> Python — Downloads \
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

(python-dependencies)=
## Optional Python Dependencies

:::{note}
The following only applies to releng-tool installations performed using
[pipx][pipx] or using a virtual environment. If an installation is performed
through a system's package manager, any dependencies should also be installed
using the system's package manager.
:::

A releng-tool installation also supports the automatic installation of
optional Python-based dependencies (if required for a project and not
manually installed).

The following outlines the various configuration sets supported when installing
releng-tool:

| Feature                    | Value           | Version |
| -------------------------- | :-------------: | :-----: |
| All Dependencies           | `all`           | 3.0     |
| Meson Support              | `meson`         | 3.0     |
| Python Support (All)       | `py-all`        | 3.0     |
| Python Flit Support        | `py-flit`       | 3.0     |
| Python Hatch Support       | `py-hatch`      | 3.0     |
| Python PDM Support         | `py-pdm`        | 3.0     |
| Python Poetry Support      | `py-poetry`     | 3.0     |
| Python Setuptools Support  | `py-setuptools` | 3.0     |
| SCons Support              | `scons`         | 3.0     |
| Statistics (PDF) Support   | `statistics`    | 0.8     |

Users may install all dependencies using:

```shell
pipx install releng-tool[all]
```

For example, if a project contains Meson-based packages, releng-tool can
utilize a Meson installation available from the native system or the version
found in the running interpreter (if even different). Users could either:

- Install Meson using the system package manager.
- Install Meson in their releng-tool installation environment:

  ```
  pipx inject releng-tool meson
  ```

- Install Meson dependency when installing releng-tool:

  ```
  pipx install releng-tool[meson]
  ```

## Development

To install the most recent development sources, the following
[pipx][pipx]/[pip][pip] command can be used:

```shell
pipx install git+https://github.com/releng-tool/releng-tool.git
 (or)
pip install git+https://github.com/releng-tool/releng-tool.git
```


[pip]: https://pip.pypa.io/
[pipx]: https://pipx.pypa.io/
[python]: https://www.python.org/
[releng-tool-aur]: https://aur.archlinux.org/packages/releng-tool/
