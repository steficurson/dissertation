import React, { useState, useEffect, useRef } from 'react';
import './App.css';
import SyllogismDisplay from './components/SyllogismDisplay';
import MainScreen from './components/MainScreen';
import Button from './components/Button';

function App() {
  const [syllogismsInTutorial, setSyllogismsInTutorial] = useState([])
  const [currentSyllogism, setCurrentSyllogism] = useState("No syllogism retrieved.");
  const [tutorialWeek, setTutorialWeek] = useState(1);
  const svgDiagramRef = useRef(null);

  const nextQuestion = () => {
    const nrSyllogismsInTutorial = syllogismsInTutorial.length;
    if (nrSyllogismsInTutorial > 0) {
      const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
      if (currentIndex === syllogismsInTutorial.length - 1) {
        return;
      }
      const nextIndex = (currentIndex + 1);
      setCurrentSyllogism(syllogismsInTutorial[nextIndex]);

      if (svgDiagramRef.current) {
        svgDiagramRef.current.resetStates();
      }
    }
  }

  const prevQuestion = () => {
    const nrSyllogismsInTutorial = syllogismsInTutorial.length;
    if (nrSyllogismsInTutorial > 0) {
      const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
      if (currentIndex === 0) {
        return;
      }
      const prevIndex =currentIndex - 1
      setCurrentSyllogism(syllogismsInTutorial[prevIndex]);
    }
  }

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
          <MainScreen syllogism={currentSyllogism} ref={svgDiagramRef}/>
          <div className="absolute bottom-4 left-4">
            <SyllogismDisplay syllogism={currentSyllogism}/>
          </div>
          <div className="absolute bottom-4 right-4">
            {(syllogismsInTutorial.indexOf(currentSyllogism) !== 0) &&
              <Button text={"Previous"} onClick={prevQuestion} disabled={false}/>
            }
            {(syllogismsInTutorial.indexOf(currentSyllogism) === syllogismsInTutorial.length - 1) ?
              <Button text={"Submit"} onClick={null} disabled={false}/>
            :
              <Button text={"Next"}  onClick={nextQuestion} disabled={false}/>
            }
          </div>
    </div>
  );
}

export default App;
