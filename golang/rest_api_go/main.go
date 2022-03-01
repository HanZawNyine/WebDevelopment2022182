package main

import (
	"fmt"
	"net/http"
	"rest_api_go/config"
	"rest_api_go/handler"
)

func main() {

	fmt.Println("Your Developement Server at http://127.0.0.1:8080")
	appconfig := config.NewConfig()
	mainHandler := handler.NewMainHandler(appconfig)

	http.HandleFunc("/", mainHandler.Invoke)
	http.ListenAndServe(":8080", nil)

}
