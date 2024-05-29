import React, { useState, useEffect } from "react";
import SidebarMain from "../components/SidebarMain";

import SearchDropDown from "../components/SearchDropDown";
import StatBarTrack from "../components/StatBarTrack";
import BarGraphComponents from "../components/BarGraphComponents";
import LoadingSpinner from "../components/LoadingSpinner";

const TrackPage = () => {
  const [track_uri, setTrack_uri] = useState("");

  const handleSuggestionClick = (name, track_uri) => {
    // Handle the suggestion click here
    setTrack_uri(track_uri);

    setQuery(name);
  };
  const [query, setQuery] = useState("");

  return (
    <div className="bg-slate-900 h-screen">
      <SidebarMain />
      <div className="p-4 sm:ml-64 ">
        <h1 className="mb-4 text-4xl font-extrabold pb-4 leading-none tracking-tight text-gray-300 md:text-5xl lg:text-6xl dark:text-white">
          Track
        </h1>
        <div className="p-4 border-2  border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="grid grid-cols-1 pb-4">
            <SearchDropDown
              url="http://localhost:8000/track-list"
              initialQuery={query}
              onSuggestionClick={handleSuggestionClick}
            />
          </div>
          {track_uri !== "" && (
            <>
              <div className="grid grid-cols-4 gap-4 mb-4">
                <StatBarTrack key={track_uri} track_uri={track_uri} />
              </div>
              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
                  {/* {trackPopularityLoading ? (
                    <LoadingSpinner />
                  ) : (
                    <BarGraphComponents
                      data={chartData1}
                      options={chartOptions1}
                    />
                  )} */}
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

export default TrackPage;
