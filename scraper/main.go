package main

import (
	"fmt"

	"github.com/FabioSebs/leaguebot2023/scraper/scraper"
)

func main() {
	// wc := wordcounter.NewWordCounter()
	ws := scraper.NewWebScraper()
	collector := ws.CollectorSetup()
	_, time := ws.GetChamps(collector)
	fmt.Println(time)
}
