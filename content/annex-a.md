# ANNEX A — Quick reference

A quick reference document listing available options to developers building a
releng-tool project.

## Arguments

Arguments which are accepted by releng-tool from the command line:

```{parsed-literal}
[`clean`](action-clean)
[`distclean`](action-distclean)
[`extract`](action-extract)
[`fetch`](action-fetch)
[`fetch-full`](action-fetch-full)
[`init`](action-init)
[`licenses`](action-licenses)
[`mrproper`](action-mrproper)
[`patch`](action-patch)
[`punch`](action-punch)
[`sbom`](action-sbom)
[`state`](action-state)
[`<pkg>-build`](action-pkg-build)
[`<pkg>-clean`](action-pkg-clean)
[`<pkg>-configure`](action-pkg-configure)
[`<pkg>-distclean`](action-pkg-distclean)
[`<pkg>-exec "<cmd>"`](action-pkg-exec)
[`<pkg>-extract`](action-pkg-extract)
[`<pkg>-fetch`](action-pkg-fetch)
[`<pkg>-fetch-full`](action-pkg-fetch-full)
[`<pkg>-fresh`](action-pkg-fresh)
[`<pkg>-install`](action-pkg-install)
[`<pkg>-license`](action-pkg-license)
[`<pkg>-patch`](action-pkg-patch)
[`<pkg>-rebuild`](action-pkg-rebuild)
[`<pkg>-rebuild-only`](action-pkg-rebuild-only)
[`<pkg>-reconfigure`](action-pkg-reconfigure)
[`<pkg>-reconfigure-only`](action-pkg-reconfigure-only)
[`<pkg>-reinstall`](action-pkg-reinstall)
[`--assets-dir <dir>`](arg-assets-dir)
[`--cache-dir <dir>`](arg-cache-dir)
[`--config <file>`](arg-config)
[`--debug`](arg-debug)
[`--debug-extended`](arg-debug-extended)
[`--development [<mode>]`, `-D [<mode>]`](arg-development)
[`--dl-dir <dir>`](arg-dl-dir)
[`--force`, `-F`](arg-force)
[`--help`, `-h`](arg-help)
[`--images-dir <dir>`](arg-images-dir)
[`--jobs <jobs>`, `-j <jobs>`](arg-jobs)
[`--local-sources [[<pkg>:]<dir>]`, `-L [[<pkg>:]<dir>]`](arg-local-sources)
[`--nocolorout`](arg-nocolorout)
[`--only-mirror`](arg-only-mirror)
[`--out-dir <dir>`](arg-out-dir)
[`--profile [<profile>]`, `-P [<profile>]`](arg-profile)
[`--relaxed-args`](arg-relaxed-args)
[`--root-dir <dir>`](arg-root-dir)
[`--sbom-format <fmt>`](arg-sbom-format)
[`--quirk <quirk-id>`](arg-quirk)
[`--verbose`, `-V`](arg-verbose)
[`--version`](arg-version)
[`--werror`, `-Werror`](arg-werror)
```

## Configuration options

Options which are read by releng-tool from a project's configuration script
(`releng-tool.rt`):

```{parsed-literal}
[`cache_ext`](conf-cache-ext) = &lt;callable&gt;
[`default_devmode_ignore_cache`](conf-default-devmode-ignore-cache) = bool
[`default_internal`](conf-default-internal) = bool
[`environment`](conf-environment) = {'&lt;key&gt;': '&lt;val&gt;'}
[`extensions`](conf-extensions) = ['&lt;extension&gt;', '&lt;extension&gt;']
[`external_packages`](conf-external-packages) = ['&lt;path&gt;', '&lt;path&gt;']
[`extra_license_exceptions`](conf-extra-license-exceptions) = {'&lt;short-exception-id&gt;': '&lt;exception-name&gt;'}
[`extra_licenses`](conf-extra-licenses) = {'&lt;short-license-id&gt;': '&lt;license-name&gt;'}
[`license_header`](conf-license-header) = '&lt;data&gt;'
[`override_extract_tools`](conf-override-extract-tools) = {'&lt;tool&gt;': '&lt;tool-path&gt;'}
[`override_revisions`](conf-override-revisions) = {'&lt;pkg&gt;': '&lt;revision&gt;'}   *(deprecated)*
[`override_sites`](conf-override-sites) = {'&lt;pkg&gt;': '&lt;site&gt;'}   *(deprecated)*
[`packages`](conf-packages) = ['&lt;pkg&gt;', '&lt;pkg&gt;', '&lt;pkg&gt;']
[`prerequisites`](conf-prerequisites) = ['&lt;tool&gt;', '&lt;tool&gt;', '&lt;tool&gt;']
[`quirks`](conf-quirks) = ['&lt;quirk-id&gt;']
[`sbom_format`](conf-sbom-format) = '&lt;format&gt;'
&nbsp;&nbsp;└── csv, html, json, json-spdx, rdf-spdx, text, xml
[`sysroot_prefix`](conf-sysroot-prefix) = '&lt;path&gt;' # '/usr'
[`url_mirror`](conf-url-mirror) = '&lt;mirror-url&gt;'
[`urlopen_context`](conf-urlopen-context) = &lt;ssl.SSLContext&gt;
[`vsdevcmd`](conf-vsdevcmd) = bool or str
[`vsdevcmd_products`](conf-vsdevcmd-products) = str
```

## Environment variables

Environment (and script) variables available to context's invoked by
releng-tool (may vary per context):

```{parsed-literal}
[`BUILD_DIR`](env-build-dir)
[`CACHE_DIR`](env-cache-dir)
[`DL_DIR`](env-dl-dir)
[`HOST_BIN_DIR`](env-host-bin-dir)
[`HOST_DIR`](env-host-dir)
[`HOST_INCLUDE_DIR`](env-host-include-dir)
[`HOST_LIB_DIR`](env-host-lib-dir)
[`HOST_SHARE_DIR`](env-host-share-dir)
[`IMAGES_DIR`](env-images-dir)
[`LICENSE_DIR`](env-license-dir)
[`NJOBS`](env-njobs)
[`NJOBSCONF`](env-njobsconf)
[`OUTPUT_DIR`](env-output-dir)
[`PKG_BUILD_BASE_DIR`](env-pkg-build-base-dir)
[`PKG_BUILD_DIR`](env-pkg-build-dir)
[`PKG_BUILD_OUTPUT_DIR`](env-pkg-build-output-dir)
[`PKG_CACHE_DIR`](env-pkg-cache-dir)
[`PKG_CACHE_FILE`](env-pkg-cache-file)
[`PKG_DEFDIR`](env-pkg-defdir)
[`PKG_DEVMODE`](env-pkg-defmode)
[`PKG_INTERNAL`](env-pkg-internal)
[`PKG_LOCALSRCS`](env-pkg-localsrcs)
[`PKG_NAME`](env-pkg-name)
[`PKG_REVISION`](env-pkg-revision)
[`PKG_SITE`](env-pkg-site)
[`PKG_VERSION`](env-pkg-version)
[`PREFIX`](env-prefix)
[`PREFIXED_HOST_DIR`](env-prefixed-host-dir)
[`PREFIXED_STAGING_DIR`](env-prefixed-staging-dir)
[`PREFIXED_TARGET_DIR`](env-prefixed-target-dir)
[`RELENG_CLEAN`](env-releng-clean)
[`RELENG_DEBUG`](env-releng-debug)
[`RELENG_DEVMODE`](env-releng-devmode)
[`RELENG_DISTCLEAN`](env-releng-distclean)
[`RELENG_EXEC`](env-releng-exec)
[`RELENG_FORCE`](env-releng-force)
[`RELENG_GENERATED_LICENSES`](env-releng-generated-licenses)
[`RELENG_GENERATED_SBOMS`](env-releng-generated-sboms)
[`RELENG_LOCALSRCS`](env-releng-localsrcs)
[`RELENG_MRPROPER`](env-releng-mrproper)
[`RELENG_PROFILES`](env-releng-profiles)
[`RELENG_REBUILD`](env-releng-rebuild)
[`RELENG_RECONFIGURE`](env-releng-reconfigure)
[`RELENG_REINSTALL`](env-releng-reinstall)
[`RELENG_SCRIPT`](env-releng-script)
[`RELENG_SCRIPT_DIR`](env-releng-script-dir)
[`RELENG_TARGET_PKG`](env-releng-target-dir)
[`RELENG_VERBOSE`](env-releng-version)
[`RELENG_VERSION`](env-releng-version)
[`ROOT_DIR`](env-root-dir)
[`STAGING_BIN_DIR`](env-staging-bin-dir)
[`STAGING_DIR`](env-staging-dir)
[`STAGING_INCLUDE_DIR`](env-staging-include-dir)
[`STAGING_LIB_DIR`](env-staging-lib-dir)
[`STAGING_SHARE_DIR`](env-staging-share-dir)
[`SYMBOLS_DIR`](env-symbols-dir)
[`TARGET_BIN_DIR`](env-target-bin-dir)
[`TARGET_DIR`](env-target-dir)
[`TARGET_INCLUDE_DIR`](env-target-include-dir)
[`TARGET_LIB_DIR`](env-target-lib-dir)
[`TARGET_SHARE_DIR`](env-target-share-dir)
[`<PKG_NAME>_BUILD_DIR`](env-pkg-var-build-dir)
[`<PKG_NAME>_BUILD_OUTPUT_DIR`](env-pkg-var-output-dir)
[`<PKG_NAME>_DEFDIR`](env-pkg-var-defdir)
[`<PKG_NAME>_NAME`](env-pkg-var-name)
[`<PKG_NAME>_REVISION`](env-pkg-var-revision)
[`<PKG_NAME>_VERSION`](env-pkg-var-version)
```

Other environment variables accepted by releng-tool:

```{parsed-literal}
`NO_COLOR`
[`RELENG_ASSETS_DIR`](env-releng-assets-dir)
[`RELENG_CACHE_DIR`](env-releng-cache-dir)
[`RELENG_DL_DIR`](env-releng-dl-dir)
[`RELENG_GLOBAL_OUTPUT_CONTAINER_DIR`](env-releng-global-out-container-dir)
[`RELENG_IGNORE_RUNNING_AS_ROOT`](env-releng-ignore-running-as-root)
[`RELENG_IGNORE_UNKNOWN_ARGS`](env-releng-ignore-unknown-args)
[`RELENG_IMAGES_DIR`](env-releng-images-dir)
[`RELENG_OUTPUT_DIR`](env-releng-out-dir)
[`RELENG_PARALLEL_LEVEL`](env-releng-parallel-level)
```

## Package types

Package types supported by releng-tool:

```{parsed-literal}
[Autotools](/guides/packages/pkg-type-autotools)
[CMake](/guides/packages/pkg-type-cmake)
[Cargo](/guides/packages/pkg-type-cargo)
[Make](/guides/packages/pkg-type-make)
[Meson](/guides/packages/pkg-type-meson)
[Python](/guides/packages/pkg-type-python)
[SCons](/guides/packages/pkg-type-scons)
[Script](/guides/packages/pkg-type-script) *(default)*
```

## Package options

Configuration options parsed by releng-tool for a package definition:

```{parsed-literal}
[`LIBFOO_AUTOTOOLS_AUTORECONF`](pkg-opt-autotools-autoreconf) = bool
`LIBFOO_BUILD_DEFS` = {'FOO': 'BAR'}
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-build-defs), [Cargo](pkg-opt-cargo-build-defs), [CMake](pkg-opt-cmake-build-defs), [Make](pkg-opt-make-build-defs), [Meson](pkg-opt-meson-build-defs), [Python](pkg-opt-python-build-defs), [SCons](pkg-opt-scons-build-defs))*
`LIBFOO_BUILD_ENV` = {'FOO': 'BAR'}
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-build-env), [Cargo](pkg-opt-cargo-build-env), [CMake](pkg-opt-cmake-build-env), [Make](pkg-opt-make-build-env), [Meson](pkg-opt-meson-build-env), [Python](pkg-opt-python-build-env), [SCons](pkg-opt-scons-build-env))*
`LIBFOO_BUILD_OPTS` = {'--option': 'value'} or ['--option', 'value']
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-build-opts), [Cargo](pkg-opt-cargo-build-opts), [CMake](pkg-opt-cmake-build-opts), [Make](pkg-opt-make-build-opts), [Meson](pkg-opt-meson-build-opts), [Python](pkg-opt-python-build-opts), [SCons](pkg-opt-scons-build-opts))*
[`LIBFOO_BUILD_SUBDIR`](pkg-opt-build-subdir) = '&lt;subdir&gt;'
[`LIBFOO_CARGO_NAME`](pkg-opt-cargo-name) = '&lt;name&gt;'
[`LIBFOO_CARGO_NOINSTALL`](pkg-opt-cargo-noinstall) = bool
[`LIBFOO_CMAKE_BUILD_TYPE`](pkg-opt-cmake-build-type) = '&lt;build-type&gt;'
&nbsp;&nbsp;└── Debug, Release, RelWithDebInfo, MinSizeRel
[`LIBFOO_CMAKE_NOINSTALL`](pkg-opt-cmake-noinstall) = bool
`LIBFOO_CONF_DEFS` = {'FOO': 'BAR'}
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-conf-defs), [CMake](pkg-opt-cmake-conf-defs), [Make](pkg-opt-make-conf-defs), [Meson](pkg-opt-meson-conf-defs), [SCons](pkg-opt-scons-conf-defs))*
`LIBFOO_CONF_ENV` = {'FOO': 'BAR'}
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-conf-env), [CMake](pkg-opt-cmake-conf-env), [Make](pkg-opt-make-conf-env), [Meson](pkg-opt-meson-conf-env), [SCons](pkg-opt-scons-conf-env))*
`LIBFOO_CONF_OPTS` = {'--option': 'value'} or ['--option', 'value']
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-conf-opts), [CMake](pkg-opt-cmake-conf-opts), [Make](pkg-opt-make-conf-opts), [Meson](pkg-opt-meson-conf-opts), [SCons](pkg-opt-scons-conf-opts))*
[`LIBFOO_DEPENDENCIES`](pkg-opt-dependencies) = ['&lt;pkg&gt;', '&lt;pkg&gt;']   *(deprecated)*
[`LIBFOO_DEVMODE_IGNORE_CACHE`](pkg-opt-devmode-ignore-cache) = bool
[`LIBFOO_DEVMODE_REVISION`](pkg-opt-devmode-revision) = '&lt;revision&gt;'
`LIBFOO_ENV` = {'FOO': 'BAR'}
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-env), [Cargo](pkg-opt-cargo-env), [CMake](pkg-opt-cmake-env), [Make](pkg-opt-make-env), [Meson](pkg-opt-meson-env), [Python](pkg-opt-python-env), [SCons](pkg-opt-scons-env))*
[`LIBFOO_EXTENSION`](pkg-opt-extension) = '&lt;extension&gt;'
[`LIBFOO_EXTERNAL`](pkg-opt-external) = bool
[`LIBFOO_EXTOPT`](pkg-opt-extopt) = {'FOO': 'BAR'}
[`LIBFOO_EXTRACT_TYPE`](pkg-opt-extract-type) = 'ext-&lt;extraction-extension&gt;'
[`LIBFOO_FETCH_OPTS`](pkg-opt-fetch-opts) = {'--option': 'value'} or ['--option', 'value']
[`LIBFOO_FIXED_JOBS`](pkg-opt-fixed-jobs) = int # &gt;= 1
[`LIBFOO_GIT_CONFIG`](pkg-opt-git-config) = {'FOO': 'BAR'}
[`LIBFOO_GIT_DEPTH`](pkg-opt-git-depth) = int # &gt;= 0
[`LIBFOO_GIT_REFSPECS`](pkg-opt-git-refspecs) = ['&lt;refspec&gt;'] # e.g. pull
[`LIBFOO_GIT_SUBMODULES`](pkg-opt-git-submodules) = bool
[`LIBFOO_GIT_VERIFY_REVISION`](pkg-opt-git-verify-revision) = bool
[`LIBFOO_HOST_PROVIDES`](pkg-opt-host-provides) = '&lt;tool&gt;' or ['&lt;tool-a&gt;', '&lt;tool-b&gt;']
`LIBFOO_INSTALL_DEFS` = {'FOO': 'BAR'}
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-install-defs), [Cargo](pkg-opt-cargo-install-defs), [CMake](pkg-opt-cmake-install-defs), [Make](pkg-opt-make-install-defs), [Meson](pkg-opt-meson-install-defs), [SCons](pkg-opt-scons-install-defs))*
`LIBFOO_INSTALL_ENV` = {'FOO': 'BAR'}
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-install-env), [Cargo](pkg-opt-cargo-install-env), [CMake](pkg-opt-cmake-install-env), [Make](pkg-opt-make-install-env), [Meson](pkg-opt-meson-install-env), [SCons](pkg-opt-scons-install-env))*
`LIBFOO_INSTALL_OPTS` = {'--option': 'value'} or ['--option', 'value']
&nbsp;&nbsp;└── *([Autotools](pkg-opt-autotools-install-opts), [Cargo](pkg-opt-cargo-install-opts), [CMake](pkg-opt-cmake-install-opts), [Make](pkg-opt-make-install-opts), [Meson](pkg-opt-meson-install-opts), [SCons](pkg-opt-scons-install-opts))*
[`LIBFOO_INSTALL_TYPE`](pkg-opt-install-type) = '&lt;install-type&gt;'
&nbsp;&nbsp;└── host, images, staging, staging_and_target, target
[`LIBFOO_INTERNAL`](pkg-opt-internal) = bool
[`LIBFOO_MAKE_NOINSTALL`](pkg-opt-make-noinstall) = bool
[`LIBFOO_MESON_NOINSTALL`](pkg-opt-meson-noinstall) = bool
[`LIBFOO_NEEDS`](pkg-opt-needs) = ['&lt;pkg&gt;', '&lt;pkg&gt;']
[`LIBFOO_NO_EXTRACTION`](pkg-opt-no-extraction) = bool
[`LIBFOO_LICENSE`](pkg-opt-license) = '&lt;license&gt;' or ['&lt;license&gt;', '&lt;license&gt;']
[`LIBFOO_LICENSE_FILES`](pkg-opt-license-files) = '&lt;file&gt;' or ['&lt;file&gt;', '&lt;file&gt;']
[`LIBFOO_PATCH_SUBDIR`](pkg-opt-patch-subdir) = '&lt;subdir&gt;'
[`LIBFOO_PREFIX`](pkg-opt-prefix) = '&lt;path&gt;' # '/usr'
[`LIBFOO_PYTHON_DIST_PATH`](pkg-opt-python-dist-path) = '&lt;path&gt;'  # e.g. 'dist/'
[`LIBFOO_PYTHON_INSTALLER_INTERPRETER`](pkg-opt-python-installer-interpreter) = '&lt;interpreter&gt;'
[`LIBFOO_PYTHON_INSTALLER_LAUNCHER_KIND`](pkg-opt-python-installer-launcher-kind) = '&lt;kind&gt;'
&nbsp;&nbsp;└── posix, win-amd64, win-arm64, win-arm, win-ia32
[`LIBFOO_PYTHON_INSTALLER_SCHEME`](pkg-opt-python-installer-scheme) = dict or str
[`LIBFOO_PYTHON_INTERPRETER`](pkg-opt-python-interpreter) = '&lt;path&gt;'
[`LIBFOO_PYTHON_SETUP_TYPE`](pkg-opt-python-setup-type) = '&lt;setup-type&gt;'
&nbsp;&nbsp;└── distutils, setuptools, flit, hatch, pdm, pep517, poetry
[`LIBFOO_REMOTE_CONFIG`](pkg-opt-remote-config) = bool
[`LIBFOO_REMOTE_SCRIPTS`](pkg-opt-remote-scripts) = bool
[`LIBFOO_REVISION`](pkg-opt-revision) = '&lt;revision&gt;'
[`LIBFOO_SCONS_NOINSTALL`](pkg-opt-scons-noinstall) = bool
[`LIBFOO_SKIP_REMOTE_CONFIG`](pkg-opt-skip-remote-config) = bool   *(deprecated)*
[`LIBFOO_SKIP_REMOTE_SCRIPTS`](pkg-opt-skip-remote-scripts) = bool   *(deprecated)*
[`LIBFOO_SITE`](pkg-opt-site) = '&lt;site&gt;'
[`LIBFOO_STRIP_COUNT`](pkg-opt-strip-count) = int # &gt;= 0
[`LIBFOO_TYPE`](pkg-opt-type) = '&lt;type&gt;'
&nbsp;&nbsp;└── autotools, cargo, cmake, make, meson, python, scons, script, ext-&lt;extension&gt;
[`LIBFOO_VCS_TYPE`](pkg-opt-vcs-type) = '&lt;vcs-type&gt;'
&nbsp;&nbsp;└── brz, bzr, cvs, file, git, hg, local, none, perforce, rsync, scp, svn, url
[`LIBFOO_VERSION`](pkg-opt-version) = '&lt;version&gt;'
[`LIBFOO_VSDEVCMD`](pkg-opt-vsdevcmd) = bool or str
[`LIBFOO_VSDEVCMD_PRODUCTS`](pkg-opt-vsdevcmd-products) = str
```

## Script helpers

Functions available to scripts invoked by releng-tool or importable via
`from releng_tool import *`:

```{parsed-literal}
[`debug`](releng_tool.debug)(msg, *args)
[`err`](releng_tool.err)(msg, *args)
[`hint`](releng_tool.hint)(msg, *args)
[`log`](releng_tool.log)(msg, *args)
[`note`](releng_tool.note)(msg, *args)
[`releng_cat`](releng_tool.releng_cat)(file, *args)
[`releng_copy`](releng_tool.releng_copy)(src, dst, quiet=False, critical=True, dst_dir=None, nested=False)
[`releng_copy_into`](releng_tool.releng_copy_into)(src, dst, quiet=False, critical=True, nested=False)
[`releng_env`](releng_tool.releng_env)(key, value=None)
[`releng_execute`](releng_tool.releng_execute)(args, cwd=None, env=None, env_update=None, quiet=False, critical=True,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poll=False, capture=None, expand=None, args_native=False)
[`releng_execute_rv`](releng_tool.releng_execute_rv)(command, args, cwd=None, env=None, env_update=None, args_native=False)
[`releng_exists`](releng_tool.releng_exists)(path, *args)
[`releng_exit`](releng_tool.releng_exit)(msg=None, code=None)
[`releng_expand`](releng_tool.releng_expand)(obj, kv=None)
[`releng_include`](releng_tool.releng_include)(file_path)
[`releng_join`](releng_tool.releng_join)(path, *args)
[`releng_ls`](releng_tool.releng_ls)(dir_, recursive=False)
[`releng_mkdir`](releng_tool.releng_mkdir)(dir_, *args, quiet=False)
[`releng_move`](releng_tool.releng_move)(src, dst, quiet=False, critical=True, dst_dir=None, nested=False)
[`releng_move_into`](releng_tool.releng_move_into)(src, dst, quiet=False, critical=True, nested=False)
[`releng_path`](releng_tool.releng_path)(*pathsegments)
[`releng_remove`](releng_tool.releng_remove)(path, quiet=False)
[`releng_require_version`](releng_tool.releng_require_version)(minver, maxver=None, quiet=False, critical=True)
[`releng_symlink`](releng_tool.releng_symlink)(target, link_path, quiet=False, critical=True, lpd=False, relative=True)
[`releng_tmpdir`](releng_tool.releng_tmpdir)(dir_=None, *args, wd=False)
[`releng_touch`](releng_tool.releng_touch)(file, *args)
[`releng_wd`](releng_tool.releng_wd)(dir_)
[`success`](releng_tool.success)(msg, *args)
[`verbose`](releng_tool.verbose)(msg, *args)
[`warn`](releng_tool.warn)(msg, *args)
```

## Quirks

Quirk options used by releng-tool:

```{parsed-literal}
[`releng.bzr.certifi`](quirk-releng.bzr.certifi)
[`releng.cmake.disable_direct_includes`](quirk-releng.cmake.disable_direct_includes)
[`releng.disable_devmode_ignore_cache`](quirk-releng.disable_devmode_ignore_cache)
[`releng.disable_local_site_warn`](quirk-releng.disable_local_site_warn)
[`releng.disable_prerequisites_check`](quirk-releng.disable_prerequisites_check)
[`releng.disable_remote_configs`](quirk-releng.disable_remote_configs)
[`releng.disable_remote_scripts`](quirk-releng.disable_remote_scripts)
[`releng.disable_spdx_check`](quirk-releng.disable_spdx_check)
[`releng.disable_verbose_patch`](quirk-releng.disable_verbose_patch)
[`releng.git.no_depth`](quirk-releng.git.no_depth)
[`releng.git.no_quick_fetch`](quirk-releng.git.no_quick_fetch)
[`releng.git.replicate_cache`](quirk-releng.git.replicate_cache)
[`releng.log.execute_args`](quirk-releng.log.execute_args)
[`releng.log.execute_env`](quirk-releng.log.execute_env)
[`releng.stats.no_pdf`](quirk-releng.stats.no_pdf)
```
