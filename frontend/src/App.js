import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Import Routes
import Sidebar from './components/Sidebar'; // Import SideBar component
import AboutPage from './Pages/AboutPage'; // Import AboutPage component
import TextChannel from './components/TextChannel'; // Import AboutPage component
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [showAboutPage, setShowAboutPage] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/');  
        console.log(response)
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const toggleAboutPage = () => {
    setShowAboutPage(!showAboutPage);
  };

  return (
    <Router>
      <div className="App">
        <Sidebar toggleAboutPage={toggleAboutPage} showAboutPage={showAboutPage} />
          
        {showAboutPage ? (
          <AboutPage />
        ) : (
          <header className="App-header">
            <img src={'http://localhost:3000/Cybersecurity_Logo.png'} 
              className="App-logo" alt="logo" />
        
            <div>
              <p>FAST Cybersecurity Research Team Chatbot</p>
            </div>

            {/* <div>
              <p>Data from Flask: {JSON.stringify(data, null, 2)}</p>
            </div> */}

            <TextChannel/>
          </header>
        )}

        <Routes>
          <Route path="/about" element={<AboutPage />} />
          {/* Define other routes here */}
        </Routes>

      </div>
    </Router>
  );
}

export default App;