import * as React from "react";

/**
 * Renders the SVG Venn diagram, with three circles
 * @param sectionClickHandler Handles clicks on sections
 * @param lineClickHandler Handles clicks on lines
 * @param sectionStates Contains the state of each section
 * @param lineStates Contains the state of each line
 * @param getSectionColour Gets the colour of a section
 * @param showCross For each section, whether to show a cross
 * @param sectionPaths Contains the path for each section
 * @param sectionCrossPaths Contains the path for each cross inside a section
 * @param linePaths Contains the path for each line
 * @param lineCrossPaths Contains the path for each cross on a line
 * @returns
 */
const SvgDiagram = ({
    sectionClickHandler, lineClickHandler,
    sectionStates, lineStates,
    getSectionColour,
    showCross,
    sectionPaths, sectionCrossPaths,
    linePaths, lineCrossPaths
  }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    id="svg3"
    width="400"
    height="400"
    fill="none"
    version="1.1"
    viewBox="0 0 124 124"
  >
    <circle
      id="circle1"
      cx="42"
      cy="42"
      r="40"
      fill="none"
      stroke="#000"
      strokeWidth="2"
    ></circle>
    <circle
      id="circle2"
      cx="82"
      cy="42"
      r="40"
      fill="none"
      stroke="#000"
      strokeWidth="2"
    ></circle>
    <circle
      id="circle3"
      cx="62"
      cy="82"
      r="40"
      fill="none"
      stroke="#000"
      strokeWidth="2"
    ></circle>
    {Object.entries(sectionPaths).map(([id, path]) => (
        <g key={id} onClick={() => sectionClickHandler(id)}>
          <path
            id={id}
            fill={getSectionColour(sectionStates[id])}
            strokeWidth="0.535"
            d={path}
            transform="scale(.31)"
          ></path>
          {showCross(sectionStates[id]) && (
            <path
              d={sectionCrossPaths[id]}
              fill="black"
            />
          )}
        </g>
      ))}

    {Object.entries(linePaths).map(([id, path]) => (
        <g key={id} onClick={() => lineClickHandler(id)}>
          <path
            id={id}
            fill="black"
            strokeWidth="0.535"
            d={path}
          ></path>
          {lineStates[id].state === "crossed" && (
            <path
              d={lineCrossPaths[id]}
              fill="black"
            />
          )}
        </g>
      ))}
  </svg>
);

export default SvgDiagram;
