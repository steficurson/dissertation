import React from "react";


import { useLocation } from 'react-router-dom';

const Submitted = () => {
  const location = useLocation();
  const { state } = location;
  const result = state?.result.result; // access result from state provided

  if (!result) {
    return <div className="text-3xl font-bold">Error: results could not be loaded correctly.</div>;
  }

  const answerToString = (answer, is_syllogism_valid) => {
    return (<div>
      The student <span className="font-bold">{answer == is_syllogism_valid ? "correctly" : "incorrectly"}</span> assessed the syllogism as {answer ? "valid" : "invalid"}.
      </div>);
  }


  const displayResult = () => {
    return Object.entries(result).map((question, index) => (
      <div key={index} className="border p-2 mt-4 bg-gray-200">
        <h3 className="text-xl font-bold"> Question {question[1].index+1}</h3>
        <p> Main answer correct? {question[1].result.main_answer_correct.toString()}</p>
        <p> {answerToString(question[1].selectedAnswer, question[1].syllogism.valid)}</p>
      </div>
    ));
  }

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-bold">Automarker results</h2>
      {/* <pre>{JSON.stringify(result, null, 2)}</pre> */}
      {displayResult()}
    </div>
  );
}


export default Submitted;
