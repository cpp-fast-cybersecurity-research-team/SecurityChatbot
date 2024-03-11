import new_logo from './Cybersecurity_Logo.png';
import './App.css';
import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);
  const [message, setMessage] = useState("message");
  const [gptResponse, setGPTResponse] = useState("response");

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

  const messageSubmit = async (e) => { 
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:5000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: message
        }),
      });

      if (response.ok) {
        console.log('Message Sent Successfully!');
        const data = await response.json();

        console.log(data.gptResponse)
        setGPTResponse(data.gptResponse)
      } else {
        console.error('Failed to send message:', response.statusText);
        // Handle error
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        
        <img src={new_logo} className="App-logo" alt="logo" />

        <div>
          <p>FAST Cybersecurity Research Team Chatbot</p>
        </div>
        
        <div>
          <p>Data from Flask: {JSON.stringify(data, null, 2)}</p>
        </div>

        <div>
          <form onSubmit={messageSubmit}>
            <label>
              Message:
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
              />
            </label>
            <button type="submit">Send Message</button>
          </form>
        </div>

        <div>
          <p>{gptResponse}</p>
        </div>
      </header>
    </div>
  );
}

export default App;
