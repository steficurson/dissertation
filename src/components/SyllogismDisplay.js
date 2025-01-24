import React from 'react';
import '../App.css'


const SyllogismDisplay = (props) => {

  const render_as_text = (syllogism) => {
    return (
      <div class="noselect">
        {syllogism.premise1} <br/>
        {syllogism.premise2} <br/>
        ∴ {syllogism.conclusion}
      </div>
    )
  }

  return(
    <div className="p-6 bg-white rounded-xl shadow-lg flex items-center gap-x-6 max-w-160">
        <h1 className="text-3xl text-black">
        {render_as_text(props.syllogism)}
        </h1>
    </div>
  );
}

export default SyllogismDisplay;
