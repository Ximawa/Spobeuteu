import React from "react";
import WordCloud from "react-d3-cloud";

const GraphPage = ({ data }) => (
  <WordCloud
    data={data}
    width={500}
    height={500}
    font="Times"
    fontStyle="italic"
    fontWeight="bold"
  />
);

export default GraphPage;
