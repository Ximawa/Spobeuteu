import React, { useEffect, useState } from "react";
import CardStats from "./CardStats";
import LoadingSpinner from "./LoadingSpinner";

const StatBarPlaylist = (playlist_pid) => {
  const [trackData, setTrackData] = useState(null);
  const [artistData, setArtistData] = useState(null);
  const [albumData, setAlbumData] = useState(null);
  const [durationData, setDurationData] = useState(null);

  const [isTrackLoading, setIsTrackLoading] = useState(true);
  const [isArtistLoading, setIsArtistLoading] = useState(true);
  const [isAlbumLoading, setIsAlbumLoading] = useState(true);
  const [isDurationLoading, setIsDurationLoading] = useState(true);

  useEffect(() => {
    fetch(
      `http://localhost:8000/playlist-track-count/${playlist_pid.playlist_pid}`
    )
      .then((response) => response.json())
      .then((data) => {
        setTrackData({
          Titre: "chansons dans la playlist",
          Value: data,
        });
        setIsTrackLoading(false);
      });

    fetch(
      `http://localhost:8000/playlist-unique-artist-count/${playlist_pid.playlist_pid}`
    )
      .then((response) => response.json())
      .then((data) => {
        setArtistData({
          Titre: "Artistes uniques dans la playlist",
          Value: data,
        });
        setIsArtistLoading(false);
      });

    fetch(
      `http://localhost:8000/playlist-unique-album-count/${playlist_pid.playlist_pid}`
    )
      .then((response) => response.json())
      .then((data) => {
        setAlbumData({
          Titre: "Albums uniques dans la playlist",
          Value: data,
        });
        setIsAlbumLoading(false);
      });

    fetch(
      `http://localhost:8000/playlist-avg-track-duration/${playlist_pid.playlist_pid}`
    )
      .then((response) => response.json())
      .then((data) => {
        setDurationData({
          Titre: "Duree moyenne des chansons dans la playlist",
          Value: `${Math.floor(data / 60)}:${Math.round(data % 60)}`,
        });
        setIsDurationLoading(false);
      });
  }, [playlist_pid]);

  return (
    <>
      {isArtistLoading ? <LoadingSpinner /> : <CardStats data={artistData} />}
      {isTrackLoading ? <LoadingSpinner /> : <CardStats data={trackData} />}
      {isAlbumLoading ? <LoadingSpinner /> : <CardStats data={albumData} />}
      {isDurationLoading ? (
        <LoadingSpinner />
      ) : (
        <CardStats data={durationData} />
      )}
    </>
  );
};

export default StatBarPlaylist;
