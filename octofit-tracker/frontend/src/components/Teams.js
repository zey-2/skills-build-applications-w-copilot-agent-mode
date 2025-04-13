import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://turbo-palm-tree-pgrq7xqvqvf74v6-8000.app.github.dev/api/teams/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setTeams(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
        setError('Failed to load teams. Please try again later.');
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
      <h1 className="display-4 mb-4">Teams</h1>
      
      <div className="row">
        {teams.length > 0 ? (
          teams.map(team => (
            <div className="col-md-6 mb-4" key={team._id || team.id}>
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{team.name}</h5>
                  <h6 className="card-subtitle mb-2 text-muted">Members: {team.members ? team.members.length : 0}</h6>
                  {team.members && team.members.length > 0 && (
                    <ul className="list-group list-group-flush">
                      {team.members.map((member, index) => (
                        <li className="list-group-item" key={index}>
                          {typeof member === 'object' ? member.name || member.email : member}
                        </li>
                      ))}
                    </ul>
                  )}
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12 text-center">
            <p>No teams found</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Teams;