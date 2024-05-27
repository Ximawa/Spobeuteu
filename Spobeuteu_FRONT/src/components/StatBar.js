import React, { useEffect, useState } from "react";
import CardStats from "./CardStats";

const StatBar = () => {
  const [playlistData, setPlaylistData] = useState({
    Titre: "Nombre de playlists",
    Value: 0,
  });
  const [trackData, setTrackData] = useState({
    Titre: "Nombre de tracks",
    Value: 0,
  });
  const [artistData, setArtistData] = useState({
    Titre: "Nombre d'artistes",
    Value: 0,
  });
  const [albumData, setAlbumData] = useState({
    Titre: "Nombre d'albums",
    Value: 0,
  });

  useEffect(() => {
    fetch("http://localhost:8000/playlist-count")
      .then((response) => response.json())
      .then((data) => {
        setPlaylistData({
          Titre: "Nombre de playlists",
          Value: data,
        });
      });

    fetch("http://localhost:8000/track-count")
      .then((response) => response.json())
      .then((data) => {
        setTrackData({
          Titre: "Nombre de tracks",
          Value: data,
        });
      });

    fetch("http://localhost:8000/artist-count")
      .then((response) => response.json())
      .then((data) => {
        setArtistData({
          Titre: "Nombre d'artistes",
          Value: data,
        });
      });

    fetch("http://localhost:8000/album-count")
      .then((response) => response.json())
      .then((data) => {
        setAlbumData({
          Titre: "Nombre d'albums",
          Value: data,
        });
      });
  }, []);

  return (
    <>
      <CardStats data={playlistData} />
      <CardStats data={artistData} />
      <CardStats data={albumData} />
      <CardStats data={trackData} />
    </>
  );
};

export default StatBar;
