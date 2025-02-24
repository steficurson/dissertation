import React from 'react';
import '../../App.css'


const SyllogismDisplay = (props) => {

  const render_as_text = (syllogism) => {
    return (
      <div className="noselect">
        {syllogism.premise1} <br/>
        {syllogism.premise2} <br/>
        ∴ {syllogism.conclusion}
      </div>
    )
  }

  return(
    <div className="p-6 bg-white rounded-xl shadow-lg items-center max-w-100">
        <h1 className="items-center text-black" style= {{fontSize: "2.0vw"}}>
        {render_as_text(props.syllogism)}
        </h1>
    </div>
  )
}

export default SyllogismDisplay;
