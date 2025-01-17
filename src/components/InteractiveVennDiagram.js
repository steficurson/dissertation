import React, { useState } from 'react';

const InteractiveVennDiagram = ({ circles }) => {
  const [shaded, setShaded] = useState({
    '12': false,
    '23': false,
    '13': false,
    '123': false
  });

  const toggleShade = (region) => {
    setShaded(prev => ({ ...prev, [region]: !prev[region] }));
  };

  return (
    <svg width="400" height="300" viewBox="0 0 400 300">
      <defs>
        {circles.map((circle, index) => (
          <clipPath id={`circle${index + 1}`} key={`clip${index}`}>
            <circle cx={circle.x} cy={circle.y} r="85" />
          </clipPath>
        ))}
      </defs>

      {circles.map((circle, index) => (
        <circle
          key={index}
          cx={circle.x}
          cy={circle.y}
          r="85"
          fill="transparent"hg f s
          stroke="black"
          strokeWidth="3"
        />
      ))}

      <path
        d="M0 0h400v300h-400z"
        clipPath="url(#circle1) url(#circle2)"
        fill={shaded['12'] ? 'rgba(255,0,0,0.5)' : 'transparent'}
        onClick={() => toggleShade('12')}
      />
      <path
        d="M0 0h400v300h-400z"
        clipPath="url(#circle2) url(#circle3)"
        fill={shaded['23'] ? 'rgba(0,255,0,0.5)' : 'transparent'}
        onClick={() => toggleShade('23')}
      />
      <path
        d="M0 0h400v300h-400z"
        clipPath="url(#circle1) url(#circle3)"
        fill={shaded['13'] ? 'rgba(0,0,255,0.5)' : 'transparent'}
        onClick={() => toggleShade('13')}
      />
      <path
        d="M0 0h400v300h-400z"
        clipPath="url(#circle1) url(#circle2) url(#circle3)"
        fill={shaded['123'] ? 'rgba(255,255,0,0.5)' : 'transparent'}
        onClick={() => toggleShade('123')}
      />
    </svg>
  );
};

export default InteractiveVennDiagram;
