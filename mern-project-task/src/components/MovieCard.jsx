import React from "react";

const MovieCard = ({ movie }) => {
  return (
    <div style={styles.card}>
      <img
        src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
        alt={movie.title}
        style={styles.poster}
      />
      <h3>{movie.title}</h3>
      <p>⭐ {movie.vote_average}</p>
    </div>
  );
};

const styles = {
  card: {
    width: "200px",
    margin: "10px",
    padding: "10px",
    background: "#1e1e1e",
    color: "#fff",
    borderRadius: "8px",
    textAlign: "center",
  },
  poster: {
    width: "100%",
    borderRadius: "4px",
  },
};

export default MovieCard;