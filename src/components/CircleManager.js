import React, { useState } from 'react';
import SvgDiagramClicker from './SvgDiagramClicker';

const CircleManager = () => {
    return (
        <div className="relative h-screen w-screen flex justify-center items-center">
            <SvgDiagramClicker />
        </div>
    )
};

export default CircleManager;
