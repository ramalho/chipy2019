package main

/*
1.5.3 Mutual exclusion with messages

Like serialization, mutual exclusion can be implemented using message passing.
For example, imagine that you and Bob operate a nuclear reactor that you monitor from remote stations.
Most of the time, both of you are watching for warning lights,
but you are both allowed to take a break for lunch.
It doesn’t matter who eats lunch first,
but it is very important that you don’t eat lunch at the same time,
leaving the reactor unwatched!

Puzzle: Figure out a system of message passing (phone calls) that enforces these restraints.
Assume there are no clocks, and you cannot predict when lunch will start or how long it will last.
What is the minimum number of messages that is required?
*/

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func show(name, activity string) {
	time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
	fmt.Printf("%s:\t%s\n", name, activity)
}

func work(name string, lunch_break *sync.Mutex, finish <-chan int) {
	for {
		show(name, "🛠 \tWorking")
		if rand.Intn(10) < 2 {
			lunch_break.Lock()
			show(name, "🌮\tStart lunch")
			show(name, "🍉\tEnd lunch")
			lunch_break.Unlock()
		}
		select {
		case <-finish:
			return
		default:
		}
	}
}

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	var lunch_break sync.Mutex
	finish := make(chan int)
	go work("Allen", &lunch_break, finish)
	go work("Bob", &lunch_break, finish)
	time.Sleep(400 * time.Millisecond)
	finish <- 1
	finish <- 1
}
