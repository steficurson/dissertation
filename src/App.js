import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import MainQuestionView from './MainQuestionView';
import Submitted from './Submitted';


function App() {
  return (
    <Router basename="/">
      <Routes>
        <Route path="/" element={<MainQuestionView />} />
        <Route path="/submitted" element={<Submitted />} />
      </Routes>
    </Router>
  );
}

export default App;
