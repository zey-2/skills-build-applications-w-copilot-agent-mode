import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://turbo-palm-tree-pgrq7xqvqvf74v6-8000.app.github.dev/api/users/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setUsers(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
        setError('Failed to load users. Please try again later.');
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
      <h1 className="display-4 mb-4">Users</h1>
      
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {users.length > 0 ? (
            users.map(user => (
              <tr key={user._id || user.id}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.age}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="3" className="text-center">No users found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Users;