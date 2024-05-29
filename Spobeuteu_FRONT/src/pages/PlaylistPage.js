import React, { useState, useEffect } from "react";
import SidebarMain from "../components/SidebarMain";

import SearchDropDown from "../components/SearchDropDown";
import StatBarPlaylist from "../components/StatBarPlaylist";
import BarGraphComponents from "../components/BarGraphComponents";
import LoadingSpinner from "../components/LoadingSpinner";

const PlaylistPage = () => {
  const [playlist_pid, setPlaylist_pid] = useState("");
  const [query, setQuery] = useState("");

  const [playlistData, setPlaylistData] = useState({
    labels: [],
    datasets: [],
  });
  const [chartOptions, setChartOptions] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSuggestionClick = (name, playlist_pid) => {
    setPlaylist_pid(playlist_pid);
    setQuery(name);
  };

  useEffect(() => {
    if (playlist_pid === "") {
      return;
    }
    fetch(`http://localhost:8000/playlist-artist-track-count/${playlist_pid}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);
        setPlaylistData({
          labels: labels,
          datasets: [
            {
              label: "presences des artistes",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });
        setIsLoading(false);
        setChartOptions({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text: "Artistes les plus populaires de la playlist",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });
  }, [playlist_pid]);

  return (
    <div className="bg-slate-900 h-screen">
      <SidebarMain />
      <div className="p-4 sm:ml-64 ">
        <h1 className="mb-4 text-4xl font-extrabold pb-4 leading-none tracking-tight text-gray-300 md:text-5xl lg:text-6xl dark:text-white">
          Playlist
        </h1>
        <div className="p-4 border-2  border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="grid grid-cols-1 pb-4">
            <SearchDropDown
              url="http://localhost:8000/playlist-list"
              initialQuery={query}
              onSuggestionClick={handleSuggestionClick}
            />
          </div>
          {playlist_pid !== "" && (
            <>
              <div className="grid grid-cols-4 gap-4 mb-4">
                <StatBarPlaylist
                  key={playlist_pid}
                  playlist_pid={playlist_pid}
                />
              </div>
              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
                  {isLoading ? (
                    <LoadingSpinner />
                  ) : (
                    <BarGraphComponents
                      data={playlistData}
                      options={chartOptions}
                    />
                  )}
                </div>
                <div className="flex items-center justify-center rounded bg-gray-800  dark:bg-gray-800">
                  {/* {albumPopularityLoading ? (
                    <LoadingSpinner />
                  ) : (
                    <BarGraphComponents
                      data={chartData2}
                      options={chartOptions2}
                    />
                  )} */}
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default PlaylistPage;
