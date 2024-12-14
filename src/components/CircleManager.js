import React, { useState } from 'react';
import AddCircleButton from './AddCircleButton';
import Circle from './Circle';

const CircleManager = () => {
    const [circles, setCircles] = useState([]);

    const addCircle = () => {
        if (circles.length >= 3) {
            return;
        }
        const circleName = prompt('Enter a name for this circle:');
        setCircles(prevCircles => {
            if (prevCircles.length === 0) {
                return [...prevCircles, { id: 1, name: circleName, x: window.innerWidth/2-200, y: window.innerHeight/2-250 }];
            } else if (prevCircles.length === 1) {
                return [...prevCircles, { id: 2, name: circleName, x: window.innerWidth/2, y: window.innerHeight/2-250 }];
            } else {
                return [...prevCircles, { id: 3, name: circleName, x: window.innerWidth/2-100, y: window.innerHeight/2-100}];
            }
        });

    };

    return (
    <div className="relative h-screen">
        <div className="absolute top-4 right-4">
            <AddCircleButton onAddCircle={addCircle} disabled={circles.length >= 3}/>
        </div>
        <div id="circle-container">
            {circles.map(circle => (
                <Circle id={circle.id} name={circle.name} x={circle.x} y={circle.y} />
            ))}
        </div>
    </div>
    );
};

export default CircleManager;
