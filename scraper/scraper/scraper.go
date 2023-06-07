package scraper

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"time"

	"github.com/FabioSebs/leaguebot2023/scraper/config"
	"github.com/FabioSebs/leaguebot2023/scraper/logger"
	"github.com/gocolly/colly"
)

var (
	champs = make([]Champ, 0)
)

type WebScraper interface {
	CollectorSetup() *colly.Collector
	GetChamps(*colly.Collector) ([]Champ, time.Duration)
}

type GoCollyProgram struct {
	Collector *colly.Collector
	Config    config.Config
	Logger    logger.Logger
}

func NewWebScraper() WebScraper {
	env := config.NewConfig()

	return &GoCollyProgram{
		Collector: colly.NewCollector(colly.AllowedDomains(
			env.AllowedDomains...,
		)),
		Config: env,
		Logger: logger.NewLogger(),
	}
}

// div.site-inner div.site-content div.wptb-table-container div.wptb-table-container-matrix table.wptb-preview-table
func (g *GoCollyProgram) CollectorSetup() *colly.Collector {
	g.Collector.OnHTML("body div.site div.site-inner div.site-content div.wptb-table-container div.wptb-table-container-matrix table.wptb-preview-table", func(element *colly.HTMLElement) {
		element.ForEach("td.wptb-cell", func(i int, h *colly.HTMLElement) {
			if i >= 5 && i%5 == 0 {
				champ := Champ{
					Champ: h.DOM.Find("p").Text(),
				}
				champs = append(champs, champ)
			}
		})
	})

	// Request Feedback
	g.Collector.OnRequest(func(r *colly.Request) {
		g.Logger.WriteTrace(fmt.Sprintf("visiting url: %s", r.URL.String()))
	})

	// Error Feedback
	g.Collector.OnError(func(r *colly.Response, err error) {
		g.Logger.WriteError(fmt.Sprintf("error: %s", err.Error()))
	})
	return g.Collector
}

func (g *GoCollyProgram) GetChamps(collector *colly.Collector) ([]Champ, time.Duration) {
	//empty slice
	defer emptyReviews(&champs)
	start := time.Now()
	returnRev := make([]Champ, 0)
	if err := collector.Visit(g.Config.FullDomain); err != nil {
		g.Logger.WriteError(err.Error())
	}
	writeJSON(champs)
	returnRev = champs
	return returnRev, time.Since(start)
}

func writeJSON(data []Champ) {
	leaguedata, err := json.MarshalIndent(data, "", " ")
	if err != nil {
		log.Println("Unable to create json file")
		return
	}

	if err = ioutil.WriteFile("leaguechamps.json", leaguedata, 0644); err != nil {
		log.Println("unable to write to json file")
	}
}

func emptyReviews(list *[]Champ) {
	list = nil
}
