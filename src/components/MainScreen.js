import React from 'react';
import SvgDiagramClicker from './SvgDiagramClicker';

const MainScreen = () => {
    return (
        <div className="relative h-screen w-screen">
            <p className="noselect circle-label mr-48 translate-y-8">Animal</p>
            <p className="noselect circle-label ml-48 translate-y-8">Human</p>
            <div className='h-50 flex justify-center items-center'>
                <SvgDiagramClicker />
            </div>
            <p className="noselect circle-label">Mortal</p>
        </div>
    )
};

export default MainScreen;
