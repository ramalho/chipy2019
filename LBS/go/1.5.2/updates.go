package main

/*
Puzzle: Suppose that 100 threads run the following program concurrently
(if you are not familiar with Python, the `for` loop runs the update 100 times.):

```
for i in range(100):
    temp = count
    count = temp + 1
```

What is the largest possible value of count after all threads have completed?

What is the smallest possible value?

Hint: the first question is easy; the second is not.
*/

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var count int
var wg sync.WaitGroup

func update() {
	defer wg.Done()
	for i := 0; i < 100; i++ {
		temp := count
		time.Sleep(time.Duration(rand.Intn(1)))
		count = temp + 1
	}
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go update()
	}
	wg.Wait()
	fmt.Println("count:", count)
}
