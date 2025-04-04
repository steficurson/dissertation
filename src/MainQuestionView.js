import React, { useState, useEffect, useRef } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import './styles/App.css';

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
  const navigate = useNavigate();

  const handleAnswerSelection = (answer) => {
    setCurrentSelectedAnswer(answer);
  };

  const updateCurrentQuestionState = (index, sectionStates, lineStates, selectedAnswer, syllogism) => {
    console.log("Updating question state: ", index);
    setQuestionStates(prevStates => {
      const newStates = [...prevStates];
      newStates[index] = { "index": index, sectionStates, lineStates, selectedAnswer, syllogism };
      return newStates;
    });
  };


  const nextQuestion = () => {
    const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
    updateCurrentQuestionState(currentIndex, svgDiagramRef.current.sectionStates, svgDiagramRef.current.lineStates, currentSelectedAnswer, currentSyllogism);
    console.log("Submitting answers: ", JSON.stringify(questionStates));

    if (syllogismsInTutorial.length > 0 && currentIndex < syllogismsInTutorial.length) {
      const nextIndex = (currentIndex + 1);
      restoreQuestionState(nextIndex);
      setCurrentSyllogism(syllogismsInTutorial[nextIndex]);
    }
  }

  const prevQuestion = () => {
    const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
    updateCurrentQuestionState(currentIndex, svgDiagramRef.current.sectionStates, svgDiagramRef.current.lineStates, currentSelectedAnswer);
    console.log("Submitting answers: ", JSON.stringify(questionStates));

    if (syllogismsInTutorial.length > 0 && currentIndex > 0) {
      const prevIndex = currentIndex - 1
      restoreQuestionState(prevIndex);
      setCurrentSyllogism(syllogismsInTutorial[prevIndex]);
    }
  }

  const submitAnswers = async () => {
    //update the state of the current question before submitting
    const currentIndex = syllogismsInTutorial.indexOf(currentSyllogism);
    const newQuestionStates = [...questionStates];
    newQuestionStates[currentIndex] = { "index": currentIndex, sectionStates: svgDiagramRef.current.sectionStates, lineStates: svgDiagramRef.current.lineStates, selectedAnswer: currentSelectedAnswer, syllogism: currentSyllogism };

    console.log("Submitting answers: ", JSON.stringify({
      questionStates: newQuestionStates,
      tutorialId: tutorialWeek,
    }))

    try {
      const response = await fetch('/api/check', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          questionStates: newQuestionStates,
          tutorialId: tutorialWeek
        }),
      });
      //         body: JSON.stringify({
      //   questionStates: newQuestionStates,
      //   tutorialId: tutorialWeek
      // }),

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Server responded with error: ${errorText}`);
      }
      const result = await response.json();
      console.log('Server response:', result);

      navigate('/submitted', { state: { result } });
    } catch (error) {
      console.error('Error exporting data:', error);
    }
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
            <Button text={"Submit"} onClick={submitAnswers} disabled={currentSelectedAnswer === null}/>
          :
            <Button text={"Next"}  onClick={nextQuestion} disabled={currentSelectedAnswer === null}/>
          }
        </div>
      </div>
    </div>
  );
}

export default MainQuestionView;
