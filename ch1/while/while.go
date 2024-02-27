package main

import "fmt"

func whileLoop(n int) int {
	sum := 0
	i := 1
	for i <= n {
		sum += i
		i++
	}
	return sum
}

func main() {
	fmt.Println(whileLoop(10))
}