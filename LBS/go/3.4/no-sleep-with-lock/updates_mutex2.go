package main

/*
3.4 Mutex

A second common use for semaphores is to enforce mutual exclusion.
We have already seen one use for mutual exclusion,
controlling concurrent access to shared variables.
The mutex guarantees that only one thread accesses the shared variable at a time.

A mutex is like a token that passes from one thread to another,
allowing one thread at a time to proceed.
For example, in The Lord of the Flies a group of children use a conch as a mutex.
In order to speak, you have to hold the conch.
As long as only one child holds the conch, only one can speak.

Similarly, in order for a thread to access a shared variable,
it has to “get” the mutex; when it is done, it “releases” the mutex.
Only one thread can hold the mutex at a time.

Puzzle: Add semaphores to the following example to enforce mutual exclusion to the shared variable count.

  Thread A
 ┌────────────────
1│ count = count + 1

  Thread B
 ┌────────────────
1│ count = count + 1

*/

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var count int
var countLock sync.Mutex
var wg sync.WaitGroup

func update() {
	defer wg.Done()
	for i := 0; i < 100; i++ {
		time.Sleep(time.Duration(rand.Intn(1000)) * time.Microsecond)
		countLock.Lock()
		count++
		countLock.Unlock()
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
