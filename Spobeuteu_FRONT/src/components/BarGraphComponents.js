import React from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const BarGraphComponents = ({ data, options }) => {
  // For debug
  // console.log(data);
  return (
    <div>
      <Bar data={data} options={options} />
    </div>
  );
};

export default BarGraphComponents;
