import React, { useEffect, useState } from "react";

import BarGraphComponents from "../components/BarGraphComponents";
import StatBar from "../components/StatBar";

const HomePage = () => {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [],
  });
  const [chartOptions, setChartOptions] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Remplacer l'URL par celle de votre API
    fetch("http://localhost:8000/word-popularity")
      .then((response) => response.json())
      .then((data) => {
        // Transformer les données reçues pour qu'elles soient compatibles avec Chart.js
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);

        setChartData({
          labels: labels,
          datasets: [
            {
              label: "My Dataset",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });

        setChartOptions({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text: "Chart.js Bar Chart",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });
  }, []);

  return (
    <div>
      <div className="grid grid-cols-3 gap-4">
        <div className="col-span-3">
          <StatBar />
        </div>
        <div className="col-span-3">
          <BarGraphComponents data={chartData} options={chartOptions} />
        </div>
      </div>
    </div>
  );
};

export default HomePage;
