import React, { useEffect, useState } from "react";

import BarGraphComponents from "../components/BarGraphComponents";
import StatBar from "../components/StatBar";
import SidebarMain from "../components/SidebarMain";
import LoadingSpinner from "../components/LoadingSpinner";

const HomePage = () => {
  const [chartData1, setChartData1] = useState({
    labels: [],
    datasets: [],
  });
  const [chartData2, setChartData2] = useState({
    labels: [],
    datasets: [],
  });
  const [chartData3, setChartData3] = useState({
    labels: [],
    datasets: [],
  });
  const [chartData4, setChartData4] = useState({
    labels: [],
    datasets: [],
  });
  const [chartData5, setChartData5] = useState({
    labels: [],
    datasets: [],
  });

  const [chartOptions1, setChartOptions1] = useState({});
  const [chartOptions2, setChartOptions2] = useState({});
  const [chartOptions3, setChartOptions3] = useState({});
  const [chartOptions4, setChartOptions4] = useState({});
  const [chartOptions5, setChartOptions5] = useState({});

  const [isLoading, setIsLoading] = useState(true);
  const [isLoading2, setIsLoading2] = useState(true);
  const [isLoading3, setIsLoading3] = useState(true);
  const [isLoading4, setIsLoading4] = useState(true);
  const [isLoading5, setIsLoading5] = useState(true);

  useEffect(() => {
    // Remplacer l'URL par celle de votre API
    fetch("http://localhost:8000/word-popularity")
      .then((response) => response.json())
      .then((data) => {
        // Transformer les données reçues pour qu'elles soient compatibles avec Chart.js
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);

        setChartData1({
          labels: labels,
          datasets: [
            {
              label: "Repetitions",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });
        setIsLoading(false);
        setChartOptions1({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text:
                "100 mots les plus populaires dans les titres des playlists",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });

    fetch("http://localhost:8000/artist-popularity")
      .then((response) => response.json())
      .then((data) => {
        console.log("fetch artist-popularity");
        // Transformer les données reçues pour qu'elles soient compatibles avec Chart.js
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);

        setChartData2({
          labels: labels,
          datasets: [
            {
              label: "Nombre d'apparation dans les playlists",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });
        setIsLoading2(false);
        setChartOptions2({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text: "10 artistes les plus populaires dans les playlists",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });

    fetch("http://localhost:8000/track-popularity")
      .then((response) => response.json())
      .then((data) => {
        // Transformer les données reçues pour qu'elles soient compatibles avec Chart.js
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);

        setChartData3({
          labels: labels,
          datasets: [
            {
              label: "Nombres d'apparition dans les playlists",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });
        setIsLoading3(false);
        setChartOptions3({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text: "10 chanson les plus populaires dans les playlists",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });

    fetch("http://localhost:8000/average-tracks-length")
      .then((response) => response.json())
      .then((data) => {
        // Transformer les données reçues pour qu'elles soient compatibles avec Chart.js
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);

        setChartData4({
          labels: labels,
          datasets: [
            {
              label: "Nombre de tracks",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });
        setIsLoading4(false);
        setChartOptions4({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text:
                "Repartition de la duree des tracks dans les playlists (interval de 15s)",
            },
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        });
      });

    fetch("http://localhost:8000/album-popularity")
      .then((response) => response.json())
      .then((data) => {
        // Transformer les données reçues pour qu'elles soient compatibles avec Chart.js
        const labels = data.map((item) => item.text);
        const values = data.map((item) => item.value);

        setChartData5({
          labels: labels,
          datasets: [
            {
              label: "Nombre d'apparition dans les playlists",
              data: values,
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        });
        setIsLoading5(false);
        setChartOptions5({
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text: "10 albums les plus populaires dans les playlists",
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
        <h1 className="mb-4 text-4xl font-extrabold pb-4 leading-none tracking-tight text-gray-300 md:text-5xl lg:text-6xl dark:text-white">
          Spotify million playlist dataset analysis
        </h1>
        <div className="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="grid grid-cols-4 gap-4 mb-4">
            <StatBar />
          </div>
          <div className="flex items-center justify-center mb-4 rounded bg-gray-800 dark:bg-gray-800">
            {isLoading ? (
              <LoadingSpinner />
            ) : (
              <BarGraphComponents data={chartData1} options={chartOptions1} />
            )}
          </div>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
              {isLoading2 ? (
                <LoadingSpinner />
              ) : (
                <BarGraphComponents data={chartData2} options={chartOptions2} />
              )}
            </div>
            <div className="flex items-center justify-center rounded bg-gray-800  dark:bg-gray-800">
              {isLoading3 ? (
                <LoadingSpinner />
              ) : (
                <BarGraphComponents data={chartData3} options={chartOptions3} />
              )}
            </div>
          </div>
          <div className="flex items-center justify-center mb-4 rounded bg-gray-800 dark:bg-gray-800">
            {isLoading4 ? (
              <LoadingSpinner />
            ) : (
              <BarGraphComponents data={chartData4} options={chartOptions4} />
            )}
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="flex items-center justify-center rounded bg-gray-800 dark:bg-gray-800">
              {isLoading5 ? (
                <LoadingSpinner />
              ) : (
                <BarGraphComponents data={chartData5} options={chartOptions5} />
              )}
            </div>
            <div className="flex items-center justify-center rounded bg-gray-800 h-28 dark:bg-gray-800"></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
