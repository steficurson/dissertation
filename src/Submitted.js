import React from "react";


import { useLocation } from 'react-router-dom';

const Submitted = () => {
  const location = useLocation();
  const { state } = location;
  const result = state?.result; // access result from state provided

  if (!result) {
    return <div>problem!!!!!</div>;
  }

  return (
    <div>
      <h2>Server Response:</h2>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}


export default Submitted;
