package main

import (
	"fmt"
	"strings"
	"time"
)

func spin(msg string, computation <-chan bool, spinning chan<- bool) {
	spinner_chars := []rune(`⠇⠋⠙⠸⠴⠦`)
	i := 0
	status := ""
	repeat := true
	for repeat {
		select {
		case <- computation:
			repeat = false
		default:
			time.Sleep(100 * time.Millisecond)
			char := spinner_chars[i]
			i = (i + 1) % len(spinner_chars)
			status = fmt.Sprintf("\r%c %s", char, msg)
			fmt.Print(status)
		}
	}
	fmt.Printf("\r%s\r", strings.Repeat(" ", len(status)))
	spinning <- false
}

func slow_function() int {
    time.Sleep(3 * time.Second)
	return 42
}

func supervisor() int {
	computation := make(chan bool)
	spinning := make(chan bool)
	go spin("thinking!", computation, spinning)
	result := slow_function()
	computation <- true
	<- spinning
	return result
}

func main() {
	result := supervisor()
	fmt.Println("Answer:", result)
}
