package main

/*
Allen's tasks:

1. Eat breakfast
2. Work
3. Eat lunch
4. Call Bob


Bob's tasks:

1. Eat breakfast
2. Wait for a call
3. Eat lunch

*/

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

func show(name, activity string) {
	time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
	fmt.Printf("%s:\t%s\n", name, activity)
}

func allen_day(call chan<- int) {
	defer wg.Done()
	show("Allen", "☕\tEating breakfast")
	show("Allen", "🛠\tWorking")
	show("Allen", "🌮\tEating lunch")
	show("Allen", "📞\tCall Bob")
	call <- 1
}

func bob_day(call <-chan int) {
	defer wg.Done()
	show("Bob", "☕\tEating breakfast")
	show("Bob", "🕰\tWaiting for a call")
	<-call
	show("Bob", "🍔\tEating lunch")
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	call := make(chan int)
	wg.Add(2)
	go allen_day(call)
	go bob_day(call)
	wg.Wait()
}
