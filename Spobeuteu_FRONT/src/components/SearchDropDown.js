import React, { useState } from "react";

const SearchDropDown = () => {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState({});

  const handleInputChange = async (e) => {
    const value = e.target.value;
    setQuery(value);

    if (value) {
      try {
        const response = await fetch(
          `http://localhost:8000/artist-list/${value}`
        );
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setSuggestions(data);
        console.log(suggestions);
      } catch (error) {
        console.error("Erreur lors de la récupération des suggestions:", error);
      }
    } else {
      setSuggestions({});
    }
  };

  return (
    <div className="relative w-full">
      <input
        type="text"
        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        placeholder="Search..."
        value={query}
        onChange={handleInputChange}
      />
      {Object.keys(suggestions).length > 0 && (
        <ul className="absolute z-10 w-full bg-white border border-gray-300 rounded-lg mt-1 max-h-64 overflow-y-auto">
          {Object.entries(suggestions).map(([id, name]) => (
            <li
              key={id}
              className="px-4 py-2 hover:bg-gray-200 cursor-pointer"
              onClick={() => {
                setQuery(name);
                setSuggestions({});
              }}
            >
              {name}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SearchDropDown;
