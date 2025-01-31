import React, { useState, forwardRef, useImperativeHandle } from 'react';
import SvgDiagram from './SvgDiagram';
import { SVG_SECTION_PATHS, SVG_SECTION_CROSS_PATHS, SVG_LINE_PATHS, SVG_LINE_CROSS_PATHS } from './SvgPathConstants';

const SECTION_STATES = {
    DEFAULT: 'default',
    SELECTED: 'selected',
    CROSSED: 'crossed'
  };

const LINE_STATES = {
    DEFAULT: 'default',
    CROSSED: 'crossed'
  };

const SECTION_COLOURS_CONFIG = {
    [SECTION_STATES.DEFAULT]: 'white',
    [SECTION_STATES.SELECTED]: 'grey',
    [SECTION_STATES.CROSSED]: 'white'
  };

const initialSectionState = Object.entries(SVG_SECTION_PATHS).reduce(
    (acc, [key]) => {
        acc[key] = { state: SECTION_STATES.DEFAULT };
        return acc;
    },
    {}
  );

const initialLineState = Object.entries(SVG_LINE_PATHS).reduce(
    (acc, [key]) => {
        acc[key] = { state: LINE_STATES.DEFAULT };
        return acc;
    },
    {}
  );

const SvgDiagramClicker =  forwardRef((props, ref) => {
  const [sectionStates, setSectionStates] = useState(initialSectionState);
  const [lineStates, setLineStates] = useState(initialLineState);

  const exportStates = async () => {
    try {
      const response = await fetch('/api/check', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          sectionStates: sectionStates,
          lineStates: lineStates
        })
      });

      if (!response.ok) throw new Error('Export failed');
      const result = await response.json();
      console.log('Server response:', result);
    } catch (error) {
      console.error('Error exporting data:', error);
    }
  };

  const resetStates = () => {
    exportStates();
    setSectionStates(initialSectionState);
    setLineStates(initialLineState);
  };

   // expose reset method to parent
   useImperativeHandle(ref, () => ({
    resetStates
  }));

  const sectionClickHandler = (partId) => {
    setSectionStates((prevSections) => {
      const currentState = prevSections[partId].state;
      let newState, showCross;

      switch (currentState) {
        case SECTION_STATES.DEFAULT:
          newState = SECTION_STATES.SELECTED;
          showCross = false;
          break;
        case SECTION_STATES.SELECTED:
          newState = SECTION_STATES.CROSSED;
          showCross = true;
          break;
        case SECTION_STATES.CROSSED:
          newState = SECTION_STATES.DEFAULT;
          showCross = false;
          break;
      }

      return {
        ...prevSections,
        [partId]: { state: newState, showCross: showCross }
      };
    });
  };

  const lineClickHandler = (partId) => {
    setLineStates((prevLines) => {
      const currentState = prevLines[partId].state;
      let newState;

      switch (currentState) {
        case LINE_STATES.DEFAULT:
          newState = LINE_STATES.CROSSED;
          break;
        case LINE_STATES.CROSSED:
          newState = LINE_STATES.DEFAULT;
          break;
      }

      return {
        ...prevLines,
        [partId]: { state: newState }
      };
    });
  };

  const getSectionColour = (section) => SECTION_COLOURS_CONFIG[section.state];
  const showCross = (section) => section.state === SECTION_STATES.CROSSED;

  return (
    <SvgDiagram
      sectionClickHandler={sectionClickHandler}
      lineClickHandler={lineClickHandler}
      sectionStates={sectionStates}
      lineStates={lineStates}
      getSectionColour={getSectionColour}
      showCross={showCross}
      sectionPaths={SVG_SECTION_PATHS}
      sectionCrossPaths={SVG_SECTION_CROSS_PATHS}
      linePaths={SVG_LINE_PATHS}
      lineCrossPaths={SVG_LINE_CROSS_PATHS}
    />
  );
});

export default SvgDiagramClicker;
