# Extensions

A releng-tool project can use an extension by registering the extension name
in the `extensions` configuration option inside the project configuration
(`releng`). For example, to load an extension `my_awesome_extension` into
releng-tool, the following can be defined:

```python
extensions = [
   'my_awesome_extension',
]
```

During the initial stages of a releng-tool process, the process will
check and load any configured extension. In the event that an extension is
missing, is unsupported for the running releng-tool version or fails to load;
a detailed error message will be presented to the user.

Extensions are typically Python packages installed for the running Python
environment. If extensions are not packaged/installed, users can alternatively
append the location of an extension implementation into the system path in
the releng-tool configuration file. For example, if a user has a releng-tool
project checked out alongside a checked out extension in a folder named
`my-awesome-extension`, the extension's path can be registered into the
system path using the following:

```python
import os
import sys

container_dir = os.path.dirname(ROOT_DIR)
ext_dir = os.path.join(container_dir, 'my-awesome-extension')
sys.path.append(ext_dir)
```

While the ability to load extensions is supported, capabilities provided by
extensions are not officially supported by releng-tool. For issues related to
specific extension use, it is recommended to see the documentation provided
by the providers of said extensions.

For developers interesting in implementing extensions, a list of available API
interfaces and documentation for these interfaces can be found inside the
[API implementation][releng-tool-api]. Implementation in the API folder aims
to be "API safe" -- there is a strong attempt to prevent the changing of
classes, methods, etc. to prevent compatibility issues as both releng-tool
and extensions (if any) evolve.

## Examples

The following provides a series of examples for developers on how to develop
extensions for releng-tool:

:::{toctree}
:maxdepth: 1

making-a-custom-post-build-action
making-a-custom-package-type
:::


[releng-tool-api]: https://github.com/releng-tool/releng-tool/blob/main/releng_tool/api/__init__.py
