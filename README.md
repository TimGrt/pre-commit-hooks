# pre-commit-hooks

Git Hooks for the pre-commit framework.  

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
    rev: v0.1.0
    hooks:
      - id: check-file-names
        args: ['--pattern', '^[a-z][a-zA-Z\_]+$']
```

This would allow filenames with underscores.

In case you need to exclude more file, add the `exclude` parameter.

```yaml
- repo: https://github.com/timgrt/pre-commit-hooks
    rev: v0.1.0
    hooks:
      - id: check-file-names
        exclude: ^\.|README|Readme|LICENSE.*$
```

This is a regular expression, files called *Readme*, *README*, *LICENSE* and
and files starting with a dot are excluded with the above statement.
