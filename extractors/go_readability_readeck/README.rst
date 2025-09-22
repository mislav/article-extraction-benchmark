Go-Readability
==============

Open Source article extractor written in Go: https://codeberg.org/readeck/go-readability

This is Readeck's fork of https://github.com/go-shiori/go-readability, created for performance improvements and compatibility with the latest version of `Readability.js <https://github.com/mozilla/readability>`

Usage
-----

To use the library I'm wrote a simple cli-module that reads the contents of the file passed in the arguments and outputs the parsing result to stdout.


Installation
------------

1. Install golang 1.23+
2. Go to the folder containing this file
3. Build an executable file:

    go build -o go_readability_cli
