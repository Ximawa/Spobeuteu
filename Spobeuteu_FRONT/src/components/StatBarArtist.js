import React, { useEffect, useState } from "react";
import CardStats from "./CardStats";
import LoadingSpinner from "./LoadingSpinner";

const StatBarArtist = (artist_uri) => {
  const [playlistData, setPlaylistData] = useState(null);
  const [trackData, setTrackData] = useState(null);
  const [artistData, setArtistData] = useState(null);
  const [albumData, setAlbumData] = useState(null);

  const [isPlaylistLoading, setIsPlaylistLoading] = useState(true);
  const [isTrackLoading, setIsTrackLoading] = useState(true);
  const [isArtistLoading, setIsArtistLoading] = useState(true);
  const [isAlbumLoading, setIsAlbumLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:8000/playlist-count/${artist_uri.artist_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setPlaylistData({
          Titre: "Presence individuelle en playlist",
          Value: data,
        });
        setIsPlaylistLoading(false);
      });

    fetch(`http://localhost:8000/track-count/${artist_uri.artist_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setTrackData({
          Titre: "Nombre de chanson presente en playlist",
          Value: data,
        });
        setIsTrackLoading(false);
      });

    fetch(`http://localhost:8000/album-count/${artist_uri.artist_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setAlbumData({
          Titre: "Nombre d'album present en playlist",
          Value: data,
        });
        setIsAlbumLoading(false);
      });

    fetch(`http://localhost:8000/artist-popularity/${artist_uri.artist_uri}`)
      .then((response) => response.json())
      .then((data) => {
        setArtistData({
          Titre: "au classement des artistes les plus populaires",
          Value: data,
        });
        setIsArtistLoading(false);
      });
  }, [artist_uri]);

  return (
    <>
      {isArtistLoading ? <LoadingSpinner /> : <CardStats data={artistData} />}
      {isPlaylistLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={playlistData} />
      )}
      {isTrackLoading ? <LoadingSpinner /> : <CardStats data={trackData} />}
      {isAlbumLoading ? <LoadingSpinner /> : <CardStats data={albumData} />}
    </>
  );
};

export default StatBarArtist;
