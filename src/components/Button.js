import React from 'react';
import '../App.css'

const Button = (props) => {
  return(
    <div className = "relative inline-block group">
      <button
        onClick={props.onClick}
        disabled={props.disabled}
        className={props.text == "Previous" ?
          `w-32 ml-2 mr-2 h-12 text-2xl bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded disabled:bg-gray-400 disabled:cursor-not-allowed`
        :
          `w-32 ml-2 mr-2 h-12 text-2xl bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded disabled:bg-gray-400 disabled:cursor-not-allowed`
      }
      >
        <p className="noselect">{props.text}</p>
      </button>
      {props.disabled && (
        <div className="absolute top-full transform mt-2 px-3 py-1 text-sm text-white bg-black rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none">
          You can't click this yet sorry
        </div>
      )}
    </div>
  );
}
export default Button;
