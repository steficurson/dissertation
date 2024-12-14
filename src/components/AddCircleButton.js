import React from 'react';
import '../App.css'


const AddCircleButton = (props) => {
  return(
    <div className = "relative inline-block group">
      <button
        onClick={props.onAddCircle}
        disabled={props.disabled}
        className="bg-blue-500 w-40 h-12 text-2xl hover:bg-blue-700 text-white font-bold py-2 px-4 rounded
        disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        Add Circle
      </button>
      {props.disabled && (
        <div className="absolute top-full transform mt-2 px-3 py-1 text-sm text-white bg-black rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none">
          You can only add up to 3 circles.
        </div>
      )}
    </div>
  );
}

export default AddCircleButton;
