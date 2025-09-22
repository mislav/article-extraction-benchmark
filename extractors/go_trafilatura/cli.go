package main

import (
	"fmt"
	"os"

	"github.com/markusmobius/go-trafilatura"
)

func main() {
	result, err := trafilatura.Extract(os.Stdin, trafilatura.Options{
		EnableFallback: true,
	})
	if err != nil {
		panic(err)
	}
	_, err = fmt.Println(result.ContentText)
	if err != nil {
		panic(err)
	}
}
