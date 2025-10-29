package main

import (
    "fmt"
    "net"
    "strconv"
    "sync"
)

func main() {
    var wg sync.WaitGroup
    for port := 1; port <= 1024; port++ {
        wg.Add(1)
        go func(port int) {
            defer wg.Done()
            address := "127.0.0.1:" + strconv.Itoa(port)
            conn, err := net.Dial("tcp", address)
            if err == nil {
                fmt.Printf("Port %d is open\n", port)
                conn.Close()
            }
        }(port)
    }
    wg.Wait()
}
