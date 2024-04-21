import React, { useState } from 'react';
import './TextChannel.css'
import MessageBox from './MessageBox.js';

function TextChannel() {
    const [inputMessage, setInputMessage] = useState("");
    const [messageHistory, setMessageHistory] = useState([
      { 
        id: 1, 
        text: "How can I help you today?", 
        isUserMessage: false
      }
    ])

    function createMessage(message, isUserMessage) {
      const newMessage = {
        id: Math.random(),
        text: message,
        isUserMessage: isUserMessage
      }
      setMessageHistory(prevMessages => [...prevMessages, newMessage])
    }

      const messageSubmit = async (e) => { 
        e.preventDefault();
        createMessage(inputMessage, true)
        try {
          const response = await fetch('http://localhost:5000/ask', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              question: inputMessage
            }),
          });
          if (response.ok) {
            //GPT makes a response
            console.log('Message Sent Successfully!');
            const data = await response.json();
    
            console.log(data.gptResponse)
            createMessage(data.gptResponse[0].trim(), false)
            // console.log(messageHistory)
          } else {
            console.error('Failed to send message:', response.statusText);
            // Handle error
          }
        } catch (error) {
          console.error('Error:', error);
        }
        setInputMessage('');
      };

    return (
        <div>
          {/* <p>{gptResponse}</p> */}
          <div className="textbox-container">
            {messageHistory.map(message => (
              <MessageBox 
                id={message.id}
                text={message.text} 
                isUserMessage={message.isUserMessage}
              />
            ))}
          </div>
          <form onSubmit={messageSubmit}>
            <label >
              Message: 
              <input 
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
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