import React, { useState, useEffect } from "react";
import SidebarMain from "../components/SidebarMain";

import SearchDropDown from "../components/SearchDropDown";
import StatBarAlbum from "../components/StatBarAlbum";
import BarGraphComponents from "../components/BarGraphComponents";
import LoadingSpinner from "../components/LoadingSpinner";

const AlbumPage = () => {
  const [album_uri, setAlbum_uri] = useState("");
  const [query, setQuery] = useState("");

  const [trackPopularityLoading, setTrackPopularityLoading] = useState(true);
  const [chartData1, setChartData1] = useState({
    labels: [],
    datasets: [],
  });
  const [chartOptions1, setChartOptions1] = useState({});

  useEffect(() => {
    if (album_uri === "") {
      return;
    }
    fetch(`http://localhost:8000/track-popularity-by-album/${album_uri}`)
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
              text: "Chansons les plus populaire de l'album",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });
  }, [album_uri]);

  const handleSuggestionClick = (name, album_uri) => {
    // Handle the suggestion click here
    setAlbum_uri(album_uri);
    setQuery(name);
  };

  return (
    <div className="bg-slate-900 h-screen">
      <SidebarMain />
      <div className="p-4 sm:ml-64 ">
        <h1 className="mb-4 text-4xl font-extrabold pb-4 leading-none tracking-tight text-gray-300 md:text-5xl lg:text-6xl dark:text-white">
          Album
        </h1>
        <div className="p-4 border-2  border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="grid grid-cols-1 pb-4">
            <SearchDropDown
              url="http://localhost:8000/album-list"
              initialQuery={query}
              onSuggestionClick={handleSuggestionClick}
            />
          </div>
          {album_uri !== "" && (
            <>
              <div className="grid grid-cols-4 gap-4 mb-4">
                <StatBarAlbum key={album_uri} album_uri={album_uri} />
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
                <div className="flex items-center justify-center rounded bg-gray-800  dark:bg-gray-800"></div>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default AlbumPage;
