package main

import (
	"fmt"
	"net/url"
	"os"

	readability "github.com/go-shiori/go-readability"
	"golang.org/x/net/html"
)

func main() {
	doc, err := html.Parse(os.Stdin)
	if err != nil {
		panic(err)
	}

	u, _ := url.Parse("https://fake-url.com")

	article, err := readability.FromDocument(doc, u)
	if err != nil {
		panic(err)
	}

	fmt.Print(article.TextContent)
}
