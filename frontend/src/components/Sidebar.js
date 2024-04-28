import React, { useState } from 'react';
//import { Link } from 'react-router-dom'; // Import Link from react-router-dom
//import AboutPage from './AboutPage'; // Import the AboutPage component
import './Sidebar.css'

function Sidebar() {
  const [currentPage, setCurrentPage] = useState('main-menu'); // Set default page to load
  const [isOpen, setIsOpen] = useState(true); // State to track if the sidebar is open

  // Function to toggle the sidebar
  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  const renderPageContent = () => {
    switch (currentPage) {
      case 'about':
        return (
          <div>
            <h2>About Page</h2>
            <button onClick={() => setCurrentPage('main-menu')}>Back to Main Menu</button>
          </div>
        );
      case 'how-to-use':
        return (
          <div>
            <h2>How to Use</h2>
            <p>
              To use the chatbot, enter a question in the input box below or ask it to 
              perform a specific task that is available through Langchain agents. Click 
              the button below to learn more about us.
            </p>
            <button onClick={() => setCurrentPage('main-menu')}>Back to Main Menu</button>
          </div>
        );
      case 'features':
        return (
          <div>
            <h2>Features</h2>
            <p>
              The chatbot is able to incorporate relevant information through a Retrieval 
              Model. This is done by querying a Postgres Vector Database, which we can store 
              embedded vectors obtained from pdfs and other word documents. The Langchain LLM 
              also uses Langchain agents which allows you to utilize HuggingFact models within 
              the transformer. These tasks include (include tasks here).
            </p>
            <button onClick={() => setCurrentPage('main-menu')}>Back to Main Menu</button>
          </div>
        );
      case 'faqs':
        return (
          <div>
            <h2>FAQs</h2>
            <p>This is the FAQs page content.</p>
            <button onClick={() => setCurrentPage('main-menu')}>Back to Main Menu</button>
          </div>
        );
      case 'main-menu':
        return renderMainMenu();
      default:
        return null; // Return null for unknown pages
    }
  };

  const renderMainMenu = () => {
    return (
      <div>
        <h1>F.A.S.T</h1>
        <h2>Cyber Research Chatbot</h2>
        <ul>
          <li onClick={() => setCurrentPage('about')}>About Us</li>
          <li onClick={() => setCurrentPage('how-to-use')}>How to Use</li>
          <li onClick={() => setCurrentPage('features')}>Features</li>
          <li onClick={() => setCurrentPage('faqs')}>FAQs</li>
        </ul>
      </div>
    );
  };

  return (
    <div className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
      <div className="toggle-btn" onClick={toggleSidebar}>
        {isOpen ? <span>&#x25C0;</span> : <span>&#x25B6;</span>}
      </div>
      {renderPageContent()}
    </div>
  );
}

export default Sidebar;