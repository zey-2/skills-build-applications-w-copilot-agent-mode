import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://turbo-palm-tree-pgrq7xqvqvf74v6-8000.app.github.dev/api/leaderboard/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setLeaderboard(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError('Failed to load leaderboard. Please try again later.');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="text-center mt-5"><div className="spinner-border" role="status"></div></div>;
  }

  if (error) {
    return <div className="alert alert-danger" role="alert">{error}</div>;
  }

  return (
    <div>
      <h1 className="display-4 mb-4">Leaderboard</h1>
      
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Rank</th>
            <th>Team</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.length > 0 ? (
            leaderboard.map((entry, index) => (
              <tr key={entry._id || entry.id}>
                <td>{index + 1}</td>
                <td>{entry.team}</td>
                <td>{entry.points}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="3" className="text-center">No leaderboard entries found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;