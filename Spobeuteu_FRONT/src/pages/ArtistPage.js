import React from "react";
import SidebarMain from "../components/SidebarMain";

import SearchDropDown from "../components/SearchDropDown";

const ArtistPage = () => {
  return (
    <div className="bg-slate-900 h-screen">
      <SidebarMain />
      <div className="p-4 sm:ml-64 ">
        <h1 className="mb-4 text-4xl font-extrabold pb-4 leading-none tracking-tight text-gray-300 md:text-5xl lg:text-6xl dark:text-white">
          Artist
        </h1>
        <div className="p-4 border-2  border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="pb-4">
            <SearchDropDown />
          </div>
          <div className="flex items-center justify-center mb-4 rounded bg-gray-800 dark:bg-gray-800">
            dgf
          </div>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
              dfg
            </div>
            <div className="flex items-center justify-center rounded bg-gray-800  dark:bg-gray-800">
              dfgfg
            </div>
          </div>
          <div className="flex items-center justify-center mb-4 rounded bg-gray-800 dark:bg-gray-800">
            ggdfg
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
              dfgdfg
            </div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800">
              fdgdfgdf
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ArtistPage;
