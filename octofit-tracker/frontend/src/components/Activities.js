import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://turbo-palm-tree-pgrq7xqvqvf74v6-8000.app.github.dev/api/activities/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setActivities(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
        setError('Failed to load activities. Please try again later.');
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
      <h1 className="display-4 mb-4">Activities</h1>
      
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Type</th>
            <th>Duration (minutes)</th>
            <th>User</th>
          </tr>
        </thead>
        <tbody>
          {activities.length > 0 ? (
            activities.map(activity => (
              <tr key={activity._id || activity.id}>
                <td>{activity.type}</td>
                <td>{activity.duration}</td>
                <td>{activity.user}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="3" className="text-center">No activities found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;