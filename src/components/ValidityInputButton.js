import React from 'react';

const ValidityInputButton = ({ handleClick, selectedAnswer }) => {
  const getButtonClass = (answer) => {
    const baseClass = "w-24 ml-2 mr-2 mt-2 h-12 text-2xl text-white font-bold py-2 px-4 rounded";
    const selectedClass = answer === selectedAnswer ? "bg-gray-700" : "bg-gray-500 hover:bg-gray-600";
    return `${baseClass} ${selectedClass}`;
  }

  return(
    <div className='relative inline-block group'>
      <h1 className="noselect text-xl text-black">Is this syllogism valid?</h1>
      <button
        className={getButtonClass(true)}
        onClick={() => handleClick(selectedAnswer === true ? null : true)}
      >
        Yes
      </button>
      <button
        className={getButtonClass(false)}
        onClick={() => handleClick(selectedAnswer === false ? null : false)}
      >
        No
      </button>
    </div>
  );
}

export default ValidityInputButton;
