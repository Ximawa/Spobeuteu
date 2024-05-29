import React, { useEffect, useState } from "react";
import CardStats from "./CardStats";
import LoadingSpinner from "./LoadingSpinner";

const StatBarTrack = (track_uri) => {
  const [popularitytData, setPopularityData] = useState(null);
  const [playlistData, setPlaylistData] = useState(null);
  const [lenghtData, setLenghtData] = useState(null);

  const [isPopularityLoading, setIsPopularityLoading] = useState(true);
  const [isPlaylistLoading, setIsPlaylistLoading] = useState(true);
  const [isLenghtLoading, setIsLenghtLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:8000/track-popularity/${track_uri.track_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setPopularityData({
          Titre: "Au classement des chansons les plus populaires",
          Value: data,
        });
        setIsPopularityLoading(false);
      });

    fetch(
      `http://localhost:8000/track-presence-playlists/${track_uri.track_uri}`
    )
      .then((response) => response.json())
      .then((data) => {
        setPlaylistData({
          Titre: "Presence en playlist",
          Value: data,
        });
        setIsPlaylistLoading(false);
      });

    fetch(`http://localhost:8000/track-length/${track_uri.track_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setLenghtData({
          Titre: "Duree de la chanson",
          Value: `${Math.floor(data / 60)}:${Math.round(data % 60)}`,
        });
        setIsLenghtLoading(false);
      });
  }, [track_uri]);

  return (
    <>
      {isPopularityLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={popularitytData} />
      )}
      {isPlaylistLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={playlistData} />
      )}
      {isLenghtLoading ? <LoadingSpinner /> : <CardStats data={lenghtData} />}
    </>
  );
};

export default StatBarTrack;
