# Requirements

releng-tool is developed in [Python][python] and requires either
[Python][python] 3.9+ to run on a host system. A series of optional
tools are required if certain stages or features are used. For example,
projects fetching sources from [Git][git] will require the `git` tool
installed; projects with patches will required the `patch` tool. While
some features may be operating system-specific (e.g. Autotools features are
designed for Linux-based hosts), releng-tool can work on various operating
system variants.


[git]: https://git-scm.com/
[python]: https://www.python.org/
