import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://turbo-palm-tree-pgrq7xqvqvf74v6-8000.app.github.dev/api/workouts/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setWorkouts(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError('Failed to load workouts. Please try again later.');
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
      <h1 className="display-4 mb-4">Workouts</h1>
      
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map(workout => (
            <div className="col-md-6 mb-4" key={workout._id || workout.id}>
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{workout.name}</h5>
                  <p className="card-text">{workout.description}</p>
                </div>
                <div className="card-footer">
                  <button className="btn btn-primary">Start Workout</button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12 text-center">
            <p>No workouts found</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;