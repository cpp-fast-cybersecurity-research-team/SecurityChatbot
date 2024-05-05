import React, { useState, useEffect} from 'react';
import './TextChannel.css'
import MessageBox from './MessageBox.js';

function TextChannel({setHasUserSentFirstMessage,hasUserSentFirstMessage}) {
    const [inputMessage, setInputMessage] = useState("");
    const [messageHistory, setMessageHistory] = useState([
      { 
        id: 1, 
        text: "How can I help you today?", 
        isUserMessage: false
      }
    ])


    useEffect(() => {
      console.log('hasUserSentFirstMessage:', hasUserSentFirstMessage);
    }, [hasUserSentFirstMessage]); 

    function createMessage(message, isUserMessage) {
      const newMessage = {
        id: Math.random(),
        text: message,
        isUserMessage: isUserMessage
      }
      setMessageHistory(prevMessages => [newMessage, ...prevMessages])
    }

      const messageSubmit = async (e) => { 
        e.preventDefault();
        if(inputMessage.trim() != "") {
          createMessage(inputMessage, true)

          if(!hasUserSentFirstMessage)
            {
              setHasUserSentFirstMessage(true);
            }


          try {
            setInputMessage('');
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
        }
      };

    return (
        <div>
          <div className="textbox-container">
            {messageHistory.map(message => (
              <MessageBox 
                id={message.id}
                text={message.text} 
                isUserMessage={message.isUserMessage}
              />
            ))}
          </div>
          <form onSubmit={messageSubmit} className="flex-box">
            <input 
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Type a question here"
              />
            <button type="submit">Send Message</button>
          </form>
        </div>
    )
}

export default TextChannel;