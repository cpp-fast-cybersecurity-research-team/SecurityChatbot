import './App.css';
import Sidebar from './Sidebar';
import React, { useEffect, useState } from 'react';
import TextChannel from './components/TextChannel';


function App() {
  const [data, setData] = useState(null);

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

  return (
    <div className="App">
      <Sidebar />
      
      <header className="App-header">

        <img src={'http://localhost:3000/Cybersecurity_Logo.png'} className="App-logo" alt="logo" />

       </header>

      <div>
        <p>FAST Cybersecurity Research Team Chatbot</p>
      </div>

      {/* <div>
        <p>Data from Flask: {JSON.stringify(data, null, 2)}</p>
      </div> */}

      <TextChannel/>
        
    </div>
  );
}

export default App;
