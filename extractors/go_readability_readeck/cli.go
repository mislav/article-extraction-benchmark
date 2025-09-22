package main

import (
	"fmt"
	"net/url"
	"os"

	readability "codeberg.org/readeck/go-readability"
)

func main() {
	if len(os.Args) < 2 {
		panic("Input file not provided in args")
	}
	if len(os.Args) > 2 {
		panic("Args accept only one argument")
	}
	input := os.Args[1]

	fSrc, err := os.Open(input)
	defer fSrc.Close()
	if err != nil {
		panic(err)
	}

	u, _ := url.Parse("https://fake-url.com")

	article, err := readability.FromReader(fSrc, u)
	if err != nil {
		panic(err)
	}

	fmt.Print(article.TextContent)
}
