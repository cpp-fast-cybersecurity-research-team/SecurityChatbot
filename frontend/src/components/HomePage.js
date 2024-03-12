import React from 'react';
import './HomePage.css'

function HomePage() {
    return (
        <div class='home-page-container'>
            <div class='home-page-sidebar'></div>
            <div class='home-page-main'>
                <img src='' class="home-page-image"></img>
                <h3 class="home-page-title">Fast Cyber Research Team Chatbot</h3>
                <div class="home-page-input">
                    <textarea required="required" placeholder="Message Chatbot..."></textarea>
                    <button class="home-page-button"></button>
                </div>
            </div>
        </div>
    )
}

export default HomePage;