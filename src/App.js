import React, { useState, useEffect } from 'react';
import './App.css';
import SyllogismDisplay from './components/SyllogismDisplay';
import CircleManager from './components/CircleManager';

function App() {
  const [currentDay, setCurrentDay] = useState("...uhhh...");
  const [syllogismsInTutorial, setSyllogismsInTutorial] = useState([])
  const [currentSyllogism, setCurrentSyllogism] = useState("No syllogism retrieved.");
  const [tutorialWeek, setTutorialWeek] = useState(1);


  // component libraries (yarninstall) look up component (chakra ui?)
  useEffect(() => {
    fetch(`/api/syllogisms?tutorial_week=${encodeURIComponent(tutorialWeek)}`).then(res => res.json()).then(data => {
      setSyllogismsInTutorial(data.syllogisms);
    });
  }, [tutorialWeek]);

  useEffect(() => {
    if (syllogismsInTutorial.length > 0) {
      setCurrentSyllogism(syllogismsInTutorial[0]);
    }
  }, [syllogismsInTutorial]);

  return (
    <div className="App relative h-screen">
          <CircleManager/>
          <div className="absolute bottom-4 left-4">
            <SyllogismDisplay syllogism={currentSyllogism}/>
          </div>
    </div>
  );
}

export default App;
