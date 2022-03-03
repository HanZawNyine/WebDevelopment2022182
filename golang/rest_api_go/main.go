package main

import (
	"log"
	"net/http"
	"os"
	"rest_api_go/config"
	"rest_api_go/handler"
)

func main() {
	port := os.Getenv("PORT")
	log.Println("Listening on : " + port)
	appconfig := config.NewConfig()
	mainHandler := handler.NewMainHandler(appconfig)

	http.HandleFunc("/", mainHandler.Invoke)
	log.Fatal(http.ListenAndServe(":"+port, nil))

}
