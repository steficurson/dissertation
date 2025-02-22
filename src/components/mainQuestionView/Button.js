import React from 'react';
import '../../App.css';

const Button = (props) => {
  const getTextClass = (text) => {
    return text == "Previous" ? "noselect" : "noselect font-bold";
    }

  return(
    <div className="relative inline-block group">
      {props.disabled && (
        <div className="absolute bottom-full w-32 text-wrap left-1/2 transform -translate-x-1/2 mb-2 px-3 py-1 text-sm text-white bg-black rounded-md opacity-0 group-hover:opacity-100 transition-opacity duration-300 delay-200 pointer-events-none whitespace-nowrap">
          Select an answer to continue
        </div>
      )}
      <button
        onClick={props.onClick}
        disabled={props.disabled}
        className={"w-32 ml-2 mr-2 h-12 text-2xl bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded disabled:bg-gray-400 disabled:cursor-not-allowed"}
      >
        <p className={getTextClass(props.text)}>{props.text}</p>
      </button>
    </div>
  );
}

export default Button;
