import React from 'react';
import SvgDiagramClicker from './SvgDiagramClicker';

const MainScreen = () => {
    return (
        <div className="relative h-screen w-screen flex justify-center items-center">
            <p className="noselect circle-label" id="circle-label-a">Animal</p>
            <SvgDiagramClicker />
            <p className="noselect circle-label" id="circle-label-b">Human</p>
            <p className="noselect circle-label" id="circle-c">Mortal</p>
        </div>
    )
};

export default MainScreen;
