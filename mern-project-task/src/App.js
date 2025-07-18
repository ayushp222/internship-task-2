import React, { useEffect, useState } from 'react';
import { getTrendingMovies } from './api/tmdb';

function App() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const data = await getTrendingMovies();
        setMovies(data);
      } catch (error) {
        console.error("Error fetching trending movies:", error);
      }
    };

    fetchMovies();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Trending Movies</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '15px' }}>
        {movies.map(movie => (
          <div key={movie.id} style={{ width: '200px' }}>
            <img
              src={`https://image.tmdb.org/t/p/w300${movie.poster_path}`}
              alt={movie.title}
              style={{ width: '100%', borderRadius: '10px' }}
            />
            <h4>{movie.title}</h4>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
