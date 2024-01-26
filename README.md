# Difference Calculator

### Hexlet tests and linter status:

[![Actions Status](https://github.com/AVomalsi/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AVomalsi/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/865161db517720454f5d/maintainability)](https://codeclimate.com/github/AVomalsi/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/865161db517720454f5d/test_coverage)](https://codeclimate.com/github/AVomalsi/python-project-50/test_coverage)

[![checking-code](https://github.com/AVomalsi/python-project-50/actions/workflows/checking-code.yml/badge.svg)](https://github.com/AVomalsi/python-project-50/actions/workflows/checking-code.yml)

## Description

A **difference calculator** is a program that determines the difference between two data structures. Can be used for test output or for automatically tracking changes in configuration files.

**Utility features**:

- Support for different input formats: yaml, json;
- Generating a report in the form of plain text, stylish and json.

Below are examples of how the program works.

## Installation

To install the application, you need to run a command with a link to the repository (update pip before installing).

```bash
pip install git+https://github.com/AVomalsi/python-project-50
```

## Usage

Enter the following command to start using the application:

```bash
>> gendiff file_path1 file_path2
>> gendiff [-h, --help]
>> gendiff file_path1 file_path2 [-f, --format] format
```

The following options are available: -h, --help: call help; -f --format: file difference output format. Formats for displaying diff: "stylish" (default), "plain", "json".

The application accepts files with the extension: "json" and "yml" (yaml) as arguments.

### Comparison of flat files (JSON)

[![asciicast](https://asciinema.org/a/44HpFbbFPc9Edjj56oehMVrzg.svg)](https://asciinema.org/a/44HpFbbFPc9Edjj56oehMVrzg)

### Flat file comparison (YAML)

[![asciicast](https://asciinema.org/a/KMaUXsnN7YnObZfxC1JJYqE62.svg)](https://asciinema.org/a/KMaUXsnN7YnObZfxC1JJYqE62)

### Finding differences for files that have nested structures (YML, YAML)

[![asciicast](https://asciinema.org/a/oOlpJDvZcOHjwPZvChGYg5iWP.svg)](https://asciinema.org/a/oOlpJDvZcOHjwPZvChGYg5iWP)

### Show differences between files in flat format

[![asciicast](https://asciinema.org/a/hy10g6YRsA1B3ReN27Vyqg4pM.svg)](https://asciinema.org/a/hy10g6YRsA1B3ReN27Vyqg4pM)

### Output to JSON

[![asciicast](https://asciinema.org/a/jFXpx11EJiNkDhJEfICPifp50.svg)](https://asciinema.org/a/jFXpx11EJiNkDhJEfICPifp50)