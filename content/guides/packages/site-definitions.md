# Site definitions

The following outlines the details for defining supported site definitions.
If attempting to use an extension-provided site type, please refer to the
documentation provided by the extension.

```{note}
All site values can be defined with a unique prefix value (e.g. `git+` for
Git sources); however, this is optional if a package wishes to use the
[`LIBFOO_VCS_TYPE`](pkg-opt-vcs-type) option.
```

## Breezy site

To define a [Breezy][breezy]-based location, the site value must be
prefixed with a `brz+` value. A site can be defined as follows:

```python
LIBFOO_SITE = 'brz+https://example.com/project/trunk'
# (or)
LIBFOO_SITE = 'brz+lp:<project>'
```

The value after the prefix is a path which will be provided to a `brz export`
call [^brzexport]. Content from a Bazaar or Git repository will be fetched and
archived into a file during fetch stage. Once a cached archive is made, the
fetch stage will be skipped unless the archive is manually removed.

## Bazaar site

To define a [Bazaar][bazaar]-based location, the site value must be
prefixed with a `bzr+` value. A site can be defined as follows:

```python
LIBFOO_SITE = 'bzr+ssh://example.com/project/trunk'
# (or)
LIBFOO_SITE = 'bzr+lp:<project>'
```

The value after the prefix is a path which will be provided to a `bzr export`
call [^bzrexport]. Content from a Bazaar repository will be fetched and
archived into a file during fetch stage. Once a cached archive is made, the
fetch stage will be skipped unless the archive is manually removed.

## CVS site

To define a [CVS][cvs]-based location, the site value must be prefixed
with a `cvs+` or other common CVSROOT value. A site can be defined as
follows:

```python
LIBFOO_SITE = ':pserver:anonymous@cvs.example.com:/var/lib/cvsroot mymodule'
# (or)
LIBFOO_SITE = 'cvs+:ext:cvs@cvs.example.org:/usr/local/cvsroot mymodule'
```

The value after the prefix is a space-separated pair, where the first part
represents the CVSROOT [^cvsroot] to use and the second part specifies the
CVS module [^cvsmodule]  to use. Content from a CVS repository will be
fetched and archived into a file during fetch stage. Once a cached archive
is made, the fetch stage will be skipped unless the archive is manually
removed.

## Git site

To define a [Git][git]-based location, the site value must be prefixed with
a `git+` value or postfixed with the `.git` value. A site can be defined
as follows:

```python
LIBFOO_SITE = 'https://example.com/libfoo.git'
# (or)
LIBFOO_SITE = 'git+git@example.com:base/libfoo.git'
```

The site value (less prefix, if used) is used as a Git remote [^gitremote]
for a locally managed cache source. Git sources will be cached inside the
`cache` directory on first-run. Future runs to fetch a project's source
will use the cached Git file system. If a desired revision exists, content
will be acquired from the cache location. If a desired revision does not
exist, the origin remote will be fetched for the new revision (if it exists).

(site-local)=
## Local site

To define a package to use local site/sources, the site value can be set
to `local`. A local site can be defined as follows:

```python
LIBFOO_SITE = 'local'
```

This is equivalent to configuring [`LIBFOO_VCS_TYPE`](pkg-opt-vcs-type)
to a `local` VCS type as well. Note that a local package is intended for
development/testing/training purposes. See
[`LIBFOO_VCS_TYPE`](pkg-opt-vcs-type) for more information.

## Mercurial site

To define a [Mercurial][mercurial]-based location, the site value must be
prefixed with a `hg+` value. A site can be defined as follows:

```python
LIBFOO_SITE = 'hg+https://example.com/project'
```

The value after the prefix is used as the `SOURCE` in an `hg clone` call
[^hgclone]. Mercurial sources will be cached inside the `cache` directory on
first-run. Future runs to fetch a project's source will use the cached Mercurial
repository. If a desired revision exists, content will be acquired from the
cache location. If a desired revision does not exist, the origin remote will be
pulled for the new revision (if it exists).

## Perforce site

To define a Perforce-based location, the site value must be prefixed with
an `perforce+` value. A site can be defined as follows:

```python
LIBFOO_SITE = 'perforce+srcs.example.com:1666 //base/libfoo/main'
# (or)
LIBFOO_SITE = 'perforce+guest@tcp4:perforce.example.org:1666 //guest/libfoo'
```

The value after the prefix is a space-separated pair, where the first part
represents the Perforce service (`P4PORT` [^p4port]) to use and the second
part specifies the Perforce depot path. Perforce data is fetched using
`git p4 <option>` [^git-p4] command. This requires a host to have both
[Git][git] and Perforce's [Helix Command-Line Client (P4)][perforce-cli]
installed. Content from a Perforce depot will be fetched and archived into
a file during fetch stage. Once a cached archive is made, the fetch stage 
ill be skipped unless the archive is manually removed.

## rsync site

To define an rsync-based location, the site value must be prefixed with an
`rsync+` value. A site can be defined as follows:

```python
LIBFOO_SITE = 'rsync+<source>'
```

The value of `<source>` will be provided to a `rsync` call's [^rsynccommand]
`SRC` value. Fetched content will be stored in an archive inside the `dl`
directory. Once fetched, the fetch stage will be skipped unless the archive
is manually removed. By default, the `--recursive` argument is applied.
Adding or replacing options can be done by using the
[`LIBFOO_FETCH_OPTS`](pkg-opt-fetch-opts) option.

## SCP site

To define an SCP-based location, the site value must be prefixed with a `scp+`
value. A site can be defined as follows:

```python
LIBFOO_SITE = 'scp+[user@]host:]file'
```

The value after the prefix is a path which will be provided to a `scp` call's
[^scpcommand] source host value. The SCP site only supports copying a file from
a remote host. The fetched file will be stored inside the `dl` directory. Once
fetched, the fetch stage will be skipped unless the file is manually removed.

## SVN site

To define a [Subversion][subversion]-based location, the site value must be
prefixed with a `svn+` value. A site can be defined as follows:

```python
LIBFOO_SITE = 'svn+https://svn.example.com/repos/libfoo/c/branches/libfoo-1.2'
```

The value after the prefix is a path which will be provided to a
`svn checkout` call [^svncheckout]. Content from a Subversion repository will
be fetched and archived into a file during fetch stage. Once a cached archive
is made, the fetch stage will be skipped unless the archive is manually removed.

## URL site (default)

All packages that do not define a helper prefix/postfix value (as seen
in other site definitions) or do not explicitly set a
[`LIBFOO_VCS_TYPE`](pkg-opt-vcs-type) value (other than `url`), will be
considered a URL site. A URL site can be defined as follows:

```python
LIBFOO_SITE = 'https://example.com/my-file'
```

The site value provided will be directly used in a URL request. URL values
supported are defined by the Python's `urlopen` implementation [^urlopen],
which includes (but not limited to) `http(s)://`, `ftp://`, `file://` and
more.

See also [`urlopen_context`](conf-urlopen-context).


[^brzexport]: <https://www.breezy-vcs.org/doc/en/user-reference/export-help.html>
[^bzrexport]: <https://web.archive.org/web/http://doc.bazaar.canonical.com/bzr.2.7/en/user-reference/export-help.html>
[^cvsmodule]: <https://www.gnu.org/software/trans-coord/manual/cvs/html_node/checkout.html#checkout>
[^cvsroot]: <https://www.gnu.org/software/trans-coord/manual/cvs/html_node/Specifying-a-repository.html>
[^git-p4]: <https://git-scm.com/docs/git-p4>
[^gitremote]: <https://git-scm.com/docs/git-remote>
[^hgclone]: <https://www.mercurial-scm.org/doc/hg.1.html#clone>
[^p4port]: <https://www.perforce.com/manuals/cmdref/Content/CmdRef/P4PORT.html>
[^rsynccommand]: <https://linux.die.net/man/1/rsync>
[^scpcommand]: <https://linux.die.net/man/1/scp>
[^svncheckout]: <http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.checkout.html>
[^urlopen]: <https://docs.python.org/library/urllib.request.html#urllib.request.urlopen>

[bazaar]: https://wikipedia.org/wiki/GNU_Bazaar
[breezy]: https://www.breezy-vcs.org/
[cvs]: http://cvs.nongnu.org/
[git]: https://git-scm.com/
[mercurial]: https://www.mercurial-scm.org/
[perforce-cli]: https://www.perforce.com/manuals/p4guide/Content/P4Guide/chapter.install.html
[subversion]: https://subversion.apache.org/
