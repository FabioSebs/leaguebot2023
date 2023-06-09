package config

import (
	"os"

	_ "github.com/joho/godotenv/autoload"
)

type Config struct {
	FullDomain     string
	AllowedDomains []string
}

func NewConfig() Config {
	return Config{
		FullDomain:     os.Getenv("FULLDOMAIN"),
		AllowedDomains: []string{os.Getenv("ALLOWED1"), os.Getenv("ALLOWED2")},
	}
}
