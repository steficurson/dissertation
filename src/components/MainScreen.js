import React, {forwardRef} from 'react';
import SvgDiagramClicker from './SvgDiagramClicker';

const MainScreen = forwardRef((props, ref) => {
    const syllogism = props.syllogism;
    return (
        <div className="relative h-screen w-screen">
            <p className="noselect circle-label mr-48 translate-y-8">{syllogism.major_term}</p>
            <p className="noselect circle-label ml-48 translate-y-8">{syllogism.minor_term}</p>
            <div className='h-50 flex justify-center items-center'>
                <SvgDiagramClicker ref={ref}/>
            </div>
            <p className="noselect circle-label">{syllogism.middle_term}</p>
        </div>
    )
});

export default MainScreen;

