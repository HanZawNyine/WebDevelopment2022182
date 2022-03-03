package handler

import (
	"encoding/json"
	"net/http"
	"rest_api_go/config"
)

func NewMainHandler(config config.Config) *MainHandler {
	return &MainHandler{config}
}

type MainHandler struct {
	Config config.Config
}

func (handler *MainHandler) Invoke(res http.ResponseWriter, req *http.Request) {
	data := map[string]interface{}{
		"Description": "Deploy Golang Rest API",
		"Version":     handler.Config.Version,
	}
	bytes, err := json.Marshal(data)

	if err != nil {
		res.WriteHeader(http.StatusInternalServerError)
		res.Write([]byte("Something Went Wrong"))
		return
	}

	res.Header().Add("Content-Type", "application/json")
	res.WriteHeader(http.StatusOK)
	res.Write(bytes)
}
