import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ProfileCreationPage from './pages/ProfileCreationPage';
import ProfileEditPage from './pages/ProfileEditPage'; // Import the new ProfileEditPage

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path="/" element={<ProfileCreationPage />} />
          <Route path="/profile/:cvId/edit" element={<ProfileEditPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
