package main

import (
	"fmt"
	"strings"
	"time"
)

func spin(msg string, computation <-chan bool, spinning chan<- bool) {
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
			fmt.Print(status)
		}
	}
	fmt.Printf("\r%s\r", strings.Repeat(" ", len(status)))
	spinning <- false
}

func slowFunction() int {
	time.Sleep(3 * time.Second)
	return 42
}

func supervisor() int {
	computation := make(chan bool)
	spinning := make(chan bool)
	go spin("thinking!", computation, spinning)
	result := slowFunction()
	computation <- true
	<-spinning
	return result
}

func main() {
	result := supervisor()
	fmt.Println("Answer:", result)
}
