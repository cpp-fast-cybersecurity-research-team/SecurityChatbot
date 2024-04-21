import React, { useState } from 'react';
import './MessageBox.css'

function MessageBox(props) {
    const { id, text, isUserMessage } = props;
    
    return (
        <div key={id} className={isUserMessage ? "user-message" : "gpt-message"}> 
            <div className="message-box">
                {text}
            </div>
        </div>
    )
}

export default MessageBox;