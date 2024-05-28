import React from "react";

const CardStats = ({ data }) => {
  const formattedNumber = data.Value.toLocaleString("fr-FR");
  return (
    <div>
      <a className="block max-w-sm p-6 h-full border border-gray-200 rounded-lg shadow bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
        <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-300 dark:text-white">
          {formattedNumber}
        </h5>
        <p className="font-normal text-gray-300 dark:text-gray-400">
          {data.Titre}
        </p>
      </a>
    </div>
  );
};

export default CardStats;
