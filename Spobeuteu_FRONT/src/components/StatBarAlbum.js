import React, { useEffect, useState } from "react";
import CardStats from "./CardStats";
import LoadingSpinner from "./LoadingSpinner";

const StatBarAlbum = (album_uri) => {
  const [popularityData, setPpopularityData] = useState(null);
  const [playlistData, setPlaylistData] = useState(null);
  const [individualTrackData, setIndividualTrackData] = useState(null);
  const [totalTrackData, setTotalTrackData] = useState(null);

  const [isPopularityLoading, setIsPopularityLoading] = useState(true);
  const [isPlaylistLoading, setIsPlaylistLoading] = useState(true);
  const [isIndividualTrackLoading, setIsIndividualTrackLoading] = useState(
    true
  );
  const [isTotalTrackLoading, setIsTotalTrackLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:8000/album-popularity/${album_uri.album_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setPpopularityData({
          Titre: "au classement des albums les plus populaires",
          Value: data,
        });
        setIsPopularityLoading(false);
      });

    fetch(`http://localhost:8000/album-playlist-count/${album_uri.album_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setPlaylistData({
          Titre: "Presence en playlist",
          Value: data,
        });
        setIsPlaylistLoading(false);
      });

    fetch(`http://localhost:8000/album-unique-tracks/${album_uri.album_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setIndividualTrackData({
          Titre: "Tracks de cette album present dans des playlist",
          Value: data,
        });
        setIsIndividualTrackLoading(false);
      });

    fetch(`http://localhost:8000/album-track-presence/${album_uri.album_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setTotalTrackData({
          Titre: "Apparition totale des tracks de cet album dans des playlist",
          Value: data,
        });
        setIsTotalTrackLoading(false);
      });
  }, [album_uri]);

  return (
    <>
      {isPopularityLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={popularityData} />
      )}
      {isPlaylistLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={playlistData} />
      )}
      {isIndividualTrackLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={individualTrackData} />
      )}
      {isTotalTrackLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={totalTrackData} />
      )}
    </>
  );
};

export default StatBarAlbum;
