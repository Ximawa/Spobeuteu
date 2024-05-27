import React from "react";
import WordCloud from "react-d3-cloud";
import { scaleOrdinal } from "d3-scale";
import { schemeCategory10 } from "d3-scale-chromatic";

const schemeCategory10ScaleOrdinal = scaleOrdinal(schemeCategory10);

const WordCloudComponents = ({ data }) => {
  return (
    <div>
      <WordCloud
        data={data}
        font="Times"
        fontStyle="italic"
        fontWeight="bold"
        fontSize={(word) => Math.log2(word.value) * 5}
        spiral="rectangular"
        rotate={(word) => word.value % 360}
        padding={5}
        random={Math.random}
        fill={(d, i) => schemeCategory10ScaleOrdinal(i)}
      />
    </div>
  );
};

export default WordCloudComponents;
