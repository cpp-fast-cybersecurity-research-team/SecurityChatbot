import './App.css';
import React, { useEffect, useState } from 'react';
import TextChannel from './components/TextChannel';

import Media from './components/Media.jsx';

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
        <img src={'http://localhost:3000/Cybersecurity_Logo.png'} className="App-logo" alt="logo" />


        <div>
          <p>FAST Cybersecurity Research Team Chatbot</p>
          <Media icon="https://cppfast.org/wp-content/uploads/2015/05/hdr.png" url="https://campsite.bio/calpolyfast"/>
          <Media icon="https://cdn.campsite.bio/eyJidWNrZXQiOiJjYW1wc2l0ZS1iaW8tc3RvcmFnZSIsImtleSI6IkNhbFBvbHlGQVNULzk2ZmQ2OGFhLWM4ODEtNGZmYi05YjhjLWEwODliZWNiOWQyMC5wbmciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjIwMH19fQ==" url="https://campsite.bio/calpolyfast"/>
          <Media icon="https://raw.githubusercontent.com/cpp-fast-cybersecurity-research-team/SecurityChatbot/371197dd241cd8a11e9065bba8ab9063d382e1c2/frontend/public/Cybersecurity_Logo.png" url="https://campsite.bio/calpolyfast"/>
        
        </div>
        
        <div>
          <p>Data from Flask: {JSON.stringify(data, null, 2)}</p>
        </div>

        <TextChannel/>
        
      </header>
    </div>
  );
}

export default App;
