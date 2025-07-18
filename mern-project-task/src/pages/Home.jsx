import React, { useEffect, useState } from "react";
import { fetchPopularMovies } from "../api/tmdb";
import MovieCard from "../components/MovieCard";

const Home = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const loadMovies = async () => {
      const data = await fetchPopularMovies();
      setMovies(data);
    };
    loadMovies();
  }, []);

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>🎬 Popular Movies</h1>
      <div style={styles.grid}>
        {movies.map((movie) => (
          <MovieCard key={movie.id} movie={movie} />
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: {
    padding: "20px",
    background: "#121212",
    minHeight: "100vh",
  },
  heading: {
    color: "#fff",
    fontSize: "2rem",
    marginBottom: "20px",
  },
  grid: {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "center",
  },
};

export default Home;