import React, { useState, useEffect } from "react";
import SidebarMain from "../components/SidebarMain";

import SearchDropDown from "../components/SearchDropDown";
import StatBarArtist from "../components/StatBarArtist";
import BarGraphComponents from "../components/BarGraphComponents";
import LoadingSpinner from "../components/LoadingSpinner";

const ArtistPage = () => {
  const [artist_uri, setArtist_uri] = useState("");
  const [query, setQuery] = useState("");
  const [trackPopularityLoading, setTrackPopularityLoading] = useState(true);

  const [chartData1, setChartData1] = useState({
    labels: [],
    datasets: [],
  });

  const [chartOptions1, setChartOptions1] = useState({});

  useEffect(() => {
    console.log("reload");
    // Remplacer l'URL par celle de votre API
    if (artist_uri === "") {
      return;
    }
    fetch(`http://localhost:8000/artist-tracks-popularity/${artist_uri}`)
      .then((response) => response.json())
      .then((data) => {
        // Transformer les données reçues pour qu'elles soient compatibles avec Chart.js
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);

        setChartData1({
          labels: labels,
          datasets: [
            {
              label: "presences des titres",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });
        setTrackPopularityLoading(false);
        setChartOptions1({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text: "Chansons les plus populaire de l'artiste",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });
  }, [artist_uri]);

  const handleSuggestionClick = (name, artist_uri) => {
    // Handle the suggestion click here
    setArtist_uri(artist_uri);

    setQuery(name);
  };

  return (
    <div className="bg-slate-900 h-screen">
      <SidebarMain />
      <div className="p-4 sm:ml-64 ">
        <h1 className="mb-4 text-4xl font-extrabold pb-4 leading-none tracking-tight text-gray-300 md:text-5xl lg:text-6xl dark:text-white">
          Artist
        </h1>
        <div className="p-4 border-2  border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="grid grid-cols-1 pb-4">
            <SearchDropDown
              url="http://localhost:8000/artist-list"
              initialQuery={query}
              onSuggestionClick={handleSuggestionClick}
            />
          </div>
          {artist_uri !== "" && (
            <>
              <div className="grid grid-cols-4 gap-4 mb-4">
                <StatBarArtist key={artist_uri} artist_uri={artist_uri} />
              </div>
              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
                  {trackPopularityLoading ? (
                    <LoadingSpinner />
                  ) : (
                    <BarGraphComponents
                      data={chartData1}
                      options={chartOptions1}
                    />
                  )}
                </div>
                <div className="flex items-center justify-center rounded bg-gray-800  dark:bg-gray-800">
                  dfgfg
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default ArtistPage;
