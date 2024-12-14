import React, { useState } from 'react';

const AddStudent = () => {
  const [studentName, setStudentName] = useState('');
  const [studentId, setStudentId] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const newStudent = {
      name: studentName,
      age: studentId,
    };

    fetch('/api/students', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newStudent),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Success:', data);
        // reset form fields
        setStudentName('');
        setStudentId('');
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={studentName}
        onChange={(e) => setStudentName(e.target.value)}
        placeholder="Enter name"
        required
      />
      <input
        type="number"
        value={studentId}
        onChange={(e) => setStudentId(e.target.value)}
        placeholder="Enter student ID"
        required
      />
      <button type="submit">Add Student</button>
    </form>
  );
};

export default AddStudent;
