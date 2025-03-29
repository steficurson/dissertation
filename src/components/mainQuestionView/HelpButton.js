import { React, useState } from 'react';
import HelpTutorial from './HelpTutorial';

const HelpButton = (props) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const toggleModal = () => {
    setIsModalOpen(!isModalOpen);
  };

  return (
    <div className="relative">
      <span
        className="w-12 ml-2 mr-2 h-12 animate-customPing absolute rounded-full bg-gray-400 opacity-75 pointer-events-none"
      ></span>
      <button
        onClick={toggleModal}
        className="w-12 ml-2 mr-2 h-12 text-3xl bg-gray-500 font-bold text-white rounded-full hover:bg-gray-600 relative z-10"
      >
        <p className="noselect">?</p>
      </button>

      <HelpTutorial isOpen={isModalOpen} onClose={toggleModal} />
    </div>
  );

}

export default HelpButton;
