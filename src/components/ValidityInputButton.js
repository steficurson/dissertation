import React from 'react';

const ValidityInputButton = ({ handleClick, selectedAnswer }) => {
  const getButtonClass = (answer) => {
    const baseClass = "w-40 ml-2 mr-2 mt-2 h-12 text-2xl text-white font-bold py-2 px-4 rounded";
    const selectedClass = answer === selectedAnswer ? "bg-blue-900 border-2 border-black rounded" : "bg-blue-500 border-2 border-blue-500 rounded hover:bg-blue-600 hover:border-blue-600";
    return `${baseClass} ${selectedClass}`;
  }

  return(
    <div className='relative inline-block group'>
      <h1 className="noselect text-xl text-black">Is this syllogism valid?</h1>
      <button
        className={getButtonClass(true)}
        onClick={() => handleClick(selectedAnswer === true ? null : true)}
      >
        <p className="noselect">Yes</p>
      </button>
      <button
        className={getButtonClass(false)}
        onClick={() => handleClick(selectedAnswer === false ? null : false)}
      >
        <p className="noselect">No</p>
      </button>
    </div>
  );
}

export default ValidityInputButton;
