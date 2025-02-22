import { React, useState } from 'react';
import HelpTutorial from './HelpTutorial';

const HelpButton = (props) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const toggleModal = () => {
    setIsModalOpen(!isModalOpen);
  };

  return(
    <div>
      <button
        onClick={toggleModal}
        className="w-10 ml-2 mr-2 h-10 text-2xl bg-gray-500 font-bold text-white rounded-full hover:bg-gray-600"
      >
        <p className="noselect">?</p>
      </button>

      <HelpTutorial isOpen={isModalOpen} onClose={toggleModal} />
    </div>
  );
}

export default HelpButton;
