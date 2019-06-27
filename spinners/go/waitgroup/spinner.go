package main

import (
	"fmt"
	"os"
	"strings"
	"sync"
	"time"
)

func spin(msg string, computation <-chan bool, spinning *sync.WaitGroup) {
	defer spinning.Done()
	spinnerChars := []rune(`⠇⠋⠙⠸⠴⠦`)
	i := 0
	status := ""
	repeat := true
	for repeat {
		select {
		case <-computation:
			repeat = false
		default:
			time.Sleep(100 * time.Millisecond)
			char := spinnerChars[i]
			i = (i + 1) % len(spinnerChars)
			status = fmt.Sprintf("\r%c %s", char, msg)
			os.Stdout.Write([]byte(status))
		}
	}
	status = fmt.Sprintf("\r%s\r", strings.Repeat(" ", len(status)))
	os.Stdout.Write([]byte(status))
}

func slowFunction() int {
	time.Sleep(3 * time.Second)
	return 42
}

func supervisor() int {
	computation := make(chan bool)
	spinning := sync.WaitGroup{}
	spinning.Add(1)
	go spin("thinking!", computation, &spinning)
	result := slowFunction()
	computation <- true
	spinning.Wait()
	return result
}

func main() {
	result := supervisor()
	fmt.Println("Answer:", result)
}
