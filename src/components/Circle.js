import React from 'react';
import '../App.css'
import InputBase from '@mui/material/InputBase';

const handleCircleClick = () => {
  console.log(`Circle clicked!`);
};


const Circle = (props) => {

  const Label = (props) => {
    if (props.id === 1) {
      return (
        <div style={{position: 'absolute', left: window.innerWidth/2-250, top: window.innerHeight/2-250}}>
          <span className="text-2xl font-semibold">{props.name}</span>
          {/* <InputBase placeholder="Enter a name for this circle" /> */}
        </div>
      );
    } else if (props.id === 2) {
      return (
        <div style={{position: 'absolute', left: window.innerWidth/2+250, top: window.innerHeight/2-250}}>
          <span className="text-2xl font-semibold">{props.name}</span>
        </div>
      );
    } else {
      return (
        <div style={{position: 'absolute', left: window.innerWidth/2, top: window.innerHeight/2+200}}>
          <span className="text-2xl font-semibold">{props.name}</span>
        </div>
      );
    };
  }

  const index = props.id;
  return(
    <div key={index} className="flex items-center mb-4">
      <div
        onClick={handleCircleClick}
        style={{
          position: 'absolute',
          left: props.x,
          top: props.y,
          width: '300px',
          height: '300px',
          borderRadius: '50%',
          border: '3px solid black',
          cursor: 'pointer'
        }}
      />
      <Label id={index} name={props.name} />
    </div>
  );
}

export default Circle;
