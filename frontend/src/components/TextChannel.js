import React, { useState } from 'react';
import './TextChannel.css'

function TextChannel() {
    const [message, setMessage] = useState("");
    const [gptResponse, setGPTResponse] = useState("response");

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
        <div>
          <p>{gptResponse}</p>
          <form onSubmit={messageSubmit}>
            <label >
              Message: 
              <input 
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                className="space-between"
                placeholder="Type a question here"
              />
            </label>
            <button type="submit" className="space-between">Send Message</button>
          </form>
        </div>
    )
}

export default TextChannel;