# pre-commit-hooks

Git Hooks for the pre-commit framework.  

[![CodeFactor](https://www.codefactor.io/repository/github/timgrt/pre-commit-hooks/badge)](https://www.codefactor.io/repository/github/timgrt/pre-commit-hooks)

## check-vault-files

Checks that files with a given filename pattern are
encrypted with *ansible-vault*. By default, all files
with `vault` in the filename are checked, for example
a file named `vault.yml` or `variables-vault.yml` are checked.

```yaml
- repo: https://github.com/timgrt/pre-commit-hooks
  rev: v0.2.0
  hooks:
    - id: check-vault-files
```

Different filenames can be provided with the `files` parameter.
For example:

```yaml
- repo: https://github.com/timgrt/pre-commit-hooks
  rev: v0.2.0
  hooks:
    - id: check-vault-files
      files: 'secure.*'
```

This is a regular expression, files e.g. called *secure-file.yml* will
now be checked by the hook.

## check-file-names

Checks that all files comply to a given naming scheme.  
Currently, this hook ensures file names only consist of lowercase and
uppercase characters, separated by dashes, the filename must
start with a lowercase character.  
Hidden files are excluded, as well as Readme files.

You can provide the pattern for your filename syntax with the `--pattern` argument.
For example:

```yaml
- repo: https://github.com/timgrt/pre-commit-hooks
  rev: v0.2.0
  hooks:
    - id: check-file-names
      args: ['--pattern', '^[a-z][a-zA-Z\_]+$']
```

This would allow filenames with underscores.

In case you need to exclude more file, add the `exclude` parameter.

```yaml
- repo: https://github.com/timgrt/pre-commit-hooks
  rev: v0.2.0
  hooks:
    - id: check-file-names
      exclude: ^\.|README|Readme|LICENSE.*$
```

This is a regular expression, files called *Readme*, *README*, *LICENSE* and
files starting with a dot are excluded with the above statement.
