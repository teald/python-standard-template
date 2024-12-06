# NOIRLab Standard Python Template

This template is the standard template for Python projects in NOIRLab. It
enforces conformance to our programming standards for Python projects using
`pre-commmit`.

# Adding conformance to an existing project

To make this template as portable as possible, the only file needed to enforce
conformance is `.pre-commit-config.yaml`. To enforce conformance on your own project repository:

1. Install [`pre-commit`](https://pre-commit.com/)

   - It can be installed using [`pipx`](https://github.com/pypa/pipx)
     (*recommended*, for isolated app environment)
     ```console
     pipx install pre-commit
     ```
   - It can be installed using `pip`:
     ```console
     python -m pip install pre-commit
     ```

2. Copy `.pre-commit-config.yaml` file from this repository to your repository

3. Add `.pre-commit-config.yaml` to your git repository:

   ```console
   git add .pre-commit-config

   ```

4. Install the git hooks using `pre-commit`

   ```console
   pre-commit install
   ```

# Starting a new project from this Template

This template uses [`cookiecutter`][cookiecutter] to provide a starting point for *new* projects. To start a new project:

1. Install [`cookiecutter`][cookiecutter]

   - It can be installed using [`pipx`](https://github.com/pypa/pipx)
     (*recommended*, for isolated app environment)

     ```console
     pipx install cookiecutter
     ```

   - It can be installed using `pip`:

     ```console
     python -m pip install cookiecutter
     ```

2. Use the `cookiecutter` CLI to build from this repository:

   ```console
   cookiecutter <LINK TO THIS REPOSITORY>
   ```

   You will be prompted for inputs, including providing things like:

   ```
   + A project name
   ```

And that's it!

# Reporting problems with this template

Please [raise an issue](/issues) if you find any problems in this template.

[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/
