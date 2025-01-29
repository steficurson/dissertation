import React, { useState, useEffect } from 'react';
import './App.css';
import SyllogismDisplay from './components/SyllogismDisplay';
import MainScreen from './components/MainScreen';

function App() {
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
          <MainScreen syllogism={currentSyllogism}/>
          <div className="absolute bottom-4 left-4">
            <SyllogismDisplay syllogism={currentSyllogism}/>
          </div>
    </div>
  );
}

export default App;
