import React from "react";


import { useLocation } from 'react-router-dom';

const Submitted = () => {
  const location = useLocation();
  const { state } = location;
  const result = state?.result.result; // access result from state provided

  if (!result) {
    return <div className="text-3xl font-bold">Error: results could not be loaded correctly.</div>;
  }

  const answerToString = (main_answer_correct, selected_answer) => {
    return (<div>
      The student <span className="font-bold">{main_answer_correct ? "correctly" : "incorrectly"}</span> assessed the syllogism as {selected_answer ? "valid" : "invalid"}.
      </div>);
  }

  const totallyCorrect = (result) => {
    return Object.keys(result.incorrect_sections).length === 0 && Object.keys(result.incorrect_lines).length === 0;
  }

  const displayResult = () => {
    return Object.entries(result).map((question, index) => (
      <div key={index} className="border p-2 mt-4 bg-gray-200">
        <h3 className="text-xl font-bold"> Question {index+1}</h3>
        <p> {answerToString(question[1].main_answer_correct, question[1].selected_answer)}</p>

        {totallyCorrect(question[1]) &&
          <p> The Venn diagram was marked correctly.</p>
        }
        {!totallyCorrect(question[1]) &&
          <div>
            <p> The Venn diagram had {Object.keys(question[1].incorrect_sections).length} sections marked incorrectly and {Object.keys(question[1].incorrect_lines).length} lines marked incorrectly.</p>
            {Object.keys(question[1].incorrect_sections).length !== 0 &&
            <div className="mt-2">
              <p> Incorrect sections: </p>
              <ul class="list-disc list-inside">
              {Object.entries(question[1].incorrect_sections).map(([section, value]) => (
                <li key={section}>
                  Line {section} should have been <i>{value.expected}</i> but was marked as <i>{value.actual}</i>
                </li>
              ))}
              </ul>
            </div>
            }
            {Object.keys(question[1].incorrect_lines).length !== 0 &&
            <div className="mt-2">
              <p> Incorrect lines: </p>
              <ul class="list-disc list-inside">
              {Object.entries(question[1].incorrect_lines).map(([line, value]) => (
                <li key={line}>
                  Line {line} should have been <i>{value.expected}</i> but was marked as <i>{value.actual}</i>
                </li>
              ))}
              </ul>
            </div>
            }
          </div>
        }

        <div>
          <p className="text-m mt-4 font-bold">Suggested mark: {question[1].suggested_mark}</p>
        </div>
      </div>
    ));
  }

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-bold">Automarker results</h2>
      {displayResult()}
    </div>
  );
}


export default Submitted;
