import React, { useEffect, useState } from "react";

import BarGraphComponents from "../components/BarGraphComponents";
import StatBar from "../components/StatBar";
import SidebarMain from "../components/SidebarMain";

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
    <div className="bg-slate-900">
      <SidebarMain />
      <div className="p-4 sm:ml-64">
        <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
          Spotify million playlist dataset analysis
        </h1>
        <div className="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="grid grid-cols-4 gap-4 mb-4">
            <StatBar />
          </div>
          <div className="flex items-center justify-center h-48 mb-4 rounded bg-gray-800 dark:bg-gray-800">
            <BarGraphComponents data={chartData} options={chartOptions} />
          </div>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
          </div>
          <div className="flex items-center justify-center h-48 mb-4 rounded bg-gray-800 dark:bg-gray-800"></div>
          <div className="grid grid-cols-2 gap-4">
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
