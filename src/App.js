import React, { useState, useEffect, useRef } from 'react';
import './App.css';
import SyllogismDisplay from './components/SyllogismDisplay';
import MainScreen from './components/MainScreen';
import Button from './components/Button';
import ValidityInputButton from './components/ValidityInputButton';
import HelpButton from './components/HelpButton';

function App() {
  const [syllogismsInTutorial, setSyllogismsInTutorial] = useState([])
  const [currentSyllogism, setCurrentSyllogism] = useState("No syllogism retrieved.");
  const [tutorialWeek, setTutorialWeek] = useState(1);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const svgDiagramRef = useRef(null);


  const handleAnswerSelection = (answer) => {
    setSelectedAnswer(answer);
  };

  const nextQuestion = () => {
    console.log("Answer: ", selectedAnswer); //TODO: send answer to backend
    setSelectedAnswer(null);

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
    console.log("Answer: ", selectedAnswer); //TODO: send answer to backend
    setSelectedAnswer(null);

    const nrSyllogismsInTutorial = syllogismsInTutorial.length;
    if (nrSyllogismsInTutorial > 0) {
      const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
      if (currentIndex === 0) {
        return;
      }
      const prevIndex =currentIndex - 1
      setCurrentSyllogism(syllogismsInTutorial[prevIndex]);

      if (svgDiagramRef.current) {
        svgDiagramRef.current.resetStates();
      }
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
      <div className="absolute top-4 left-4">
        <HelpButton/>
      </div>
      <div className="absolute bottom-4 left-4">
        <SyllogismDisplay syllogism={currentSyllogism}/>
        <div className="mt-4">
        <ValidityInputButton handleClick={handleAnswerSelection} selectedAnswer={selectedAnswer}/>
        </div>
      </div>
      <div className="absolute bottom-4 right-4 flex flex-col items-end">
        <div className="flex justify-end">
          {(syllogismsInTutorial.indexOf(currentSyllogism) !== 0) &&
            <Button text={"Previous"} onClick={prevQuestion} disabled={false} className="mr-2"/>
          }
          {(syllogismsInTutorial.indexOf(currentSyllogism) === syllogismsInTutorial.length - 1) ?
            <Button text={"Submit"} onClick={null} disabled={selectedAnswer === null}/>
          :
            <Button text={"Next"}  onClick={nextQuestion} disabled={selectedAnswer === null}/>
          }
        </div>
      </div>
    </div>
  );
}

export default App;
