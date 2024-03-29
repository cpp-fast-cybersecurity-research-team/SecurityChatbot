import logo from './logo.svg';
import './App.css';
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
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
        <div>
          <p>Data from Flask: {JSON.stringify(data, null, 2)}</p>
        </div>

        <TextChannel/>
        
      </header>
    </div>
  );
}

export default App;
