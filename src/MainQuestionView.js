import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';

import './App.css';

import SyllogismDisplay from './components/mainQuestionView/SyllogismDisplay';
import MainScreen from './components/mainQuestionView/MainScreen';
import Button from './components/mainQuestionView/Button';
import ValidityInputButton from './components/mainQuestionView/ValidityInputButton';
import HelpButton from './components/mainQuestionView/HelpButton';

const MainQuestionView = () => {
  const [syllogismsInTutorial, setSyllogismsInTutorial] = useState([])
  const [currentSyllogism, setCurrentSyllogism] = useState("No syllogism retrieved.");
  const [tutorialWeek, setTutorialWeek] = useState(1);

  const [questionStates, setQuestionStates] = useState([]);
  const [currentSelectedAnswer, setCurrentSelectedAnswer] = useState(null);
  const svgDiagramRef = useRef(null);


  const handleAnswerSelection = (answer) => {
    setCurrentSelectedAnswer(answer);
  };

  const updateCurrentQuestionState = (index, sectionStates, lineStates, selectedAnswer) => {
    console.log("Updating question state: ", index);
    setQuestionStates(prevStates => {
      const newStates = [...prevStates];
      newStates[index] = { sectionStates, lineStates, selectedAnswer };
      return newStates;
    });
  };


  const nextQuestion = () => {
    console.log("Answer: ", currentSelectedAnswer); //TODO: send answer to backend
    const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
    updateCurrentQuestionState(currentIndex, svgDiagramRef.current.sectionStates, svgDiagramRef.current.lineStates, currentSelectedAnswer);

    if (syllogismsInTutorial.length > 0 && currentIndex < syllogismsInTutorial.length) {
      const nextIndex = (currentIndex + 1);
      restoreQuestionState(nextIndex);
      setCurrentSyllogism(syllogismsInTutorial[nextIndex]);
    }
  }

  const prevQuestion = () => {
    console.log("Answer: ", currentSelectedAnswer); //TODO: send answer to backend
    const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
    updateCurrentQuestionState(currentIndex, svgDiagramRef.current.sectionStates, svgDiagramRef.current.lineStates, currentSelectedAnswer);

    if (syllogismsInTutorial.length > 0 && currentIndex > 0) {
      const prevIndex = currentIndex - 1
      restoreQuestionState(prevIndex);
      setCurrentSyllogism(syllogismsInTutorial[prevIndex]);
    }
  }

  const submitAnswers = () => {
      //TODO: send all answers to backend to all question states
  }

  const restoreQuestionState = (index) => {
    if (questionStates.length > 0) {
      const state = questionStates[index];
      if (state) { //if the question has been (partially) answered before
        const { sectionStates, lineStates, selectedAnswer } = state;
        svgDiagramRef.current.setSectionStates(sectionStates);
        svgDiagramRef.current.setLineStates(lineStates);
        setCurrentSelectedAnswer(selectedAnswer);
        return; //exit early so we don't reset the states
      }
    }
    svgDiagramRef.current.resetStates(true);
    setCurrentSelectedAnswer(null);
  };

  useEffect(() => {
    fetch(`/api/questions?tutorial_week=${encodeURIComponent(tutorialWeek)}`).then(res => res.json()).then(data => {
      setSyllogismsInTutorial(data.questions);
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
        <ValidityInputButton handleClick={handleAnswerSelection} selectedAnswer={currentSelectedAnswer}/>
        </div>
      </div>
      <div className="absolute bottom-4 right-4 flex flex-col items-end">
        <div className="flex justify-end">
          {(syllogismsInTutorial.indexOf(currentSyllogism) !== 0) &&
            <Button text={"Previous"} onClick={prevQuestion} disabled={false} className="mr-2"/>
          }
          {(syllogismsInTutorial.indexOf(currentSyllogism) === syllogismsInTutorial.length - 1) ?
          <Link to="/submitted">
            <Button text={"Submit"} onClick={null} disabled={currentSelectedAnswer === null}/>
          </Link>
          :
            <Button text={"Next"}  onClick={nextQuestion} disabled={currentSelectedAnswer === null}/>
          }
        </div>
      </div>
    </div>
  );
}

export default MainQuestionView;
