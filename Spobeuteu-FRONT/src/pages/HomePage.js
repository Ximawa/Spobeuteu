import React, { useEffect, useState } from "react";
import axios from "axios";
import { ClipLoader } from "react-spinners";

import GraphPage from "../components/GraphPage";

const HomePage = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8000/word-popularity"
        );
        setData(response.data);
      } catch (error) {
        console.error("Error fetching the data", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  });

  const loadingStyle = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    height: "100vh",
    textAlign: "center",
  };

  return (
    <div>
      {loading ? (
        <div style={loadingStyle}>
          <ClipLoader color="#123abc" loading={loading} size={50} />
          <p>Loading...</p>
        </div>
      ) : (
        <div>
          <GraphPage data={data} />
        </div>
      )}
    </div>
  );
};

export default HomePage;
