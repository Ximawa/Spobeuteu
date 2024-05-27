import React from "react";
import CardStats from "./CardStats";

const StatBar = () => {
  return (
    <div className="grid grid-cols-3 justify-between gap-4">
      <CardStats />
      <CardStats />
      <CardStats />
    </div>
  );
};

export default StatBar;
