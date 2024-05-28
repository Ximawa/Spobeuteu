import React, { useState } from "react";
import SidebarMain from "../components/SidebarMain";

import SearchDropDown from "../components/SearchDropDown";
import StatBarArtist from "../components/StatBarArtist";

const ArtistPage = () => {
  const [artist_uri, setArtist_uri] = useState("");
  const [query, setQuery] = useState("");

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
          <div className="grid grid-cols-4 gap-4 mb-4">
            {artist_uri !== "" && (
              <StatBarArtist key={artist_uri} artist_uri={artist_uri} />
            )}
          </div>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
              dfg
            </div>
            <div className="flex items-center justify-center rounded bg-gray-800  dark:bg-gray-800">
              dfgfg
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ArtistPage;
