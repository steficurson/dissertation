import React from 'react';
import Modal from 'react-modal';
import clickSectionDemo from '../images/ClickSectionDemo.gif';

const Tutorial = ({ isOpen, onClose }) => {
  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onClose}
      contentLabel="Help Tutorial Modal"
      className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-6 rounded-lg shadow-lg max-w-3xl w-md"
      overlayClassName="fixed inset-0 bg-black bg-opacity-50"
    >
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold">How to use</h2>
        <button
          onClick={onClose}
          className="text-2xl font-bold"
        >
          ×
        </button>
      </div>
      <div className="flex justify-between items-start">
        <div className="w-80">
          <h2 className="text-l font-bold">Sections</h2>
          <p>Click on a section to shade it, indicating that an element exists in the section.</p>
          <p>A second click will place a cross in the section, indictating that the section is empty.</p>
          <p>A final click resets the section.</p>
        </div>
        <img src={clickSectionDemo}
            alt="Gif demonstrating clicking on a section to change its state"
            className="h-36 w-36 ml-2"/>
      </div>
      <br></br>
      <div className="flex justify-between items-start">
        <div className="w-80">
          <h2 className="text-l font-bold">Lines</h2>
          <p>Click on a section to shade it, indicating that an element exists in the section.</p>
          <p>A second click will place a cross in the section, indictating that the section is empty.</p>
          <p>A final click resets the section.</p>
        </div>
        <img src={clickSectionDemo}
            alt="Gif demonstrating clicking on a section to change its state"
            className="h-36 w-36 ml-2"/>
      </div>

    </Modal>
  );
}


export default Tutorial;
