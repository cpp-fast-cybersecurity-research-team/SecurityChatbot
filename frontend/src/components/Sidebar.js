import React, { useState } from 'react';
import './Sidebar.css';

function Sidebar({ toggleAboutPage, showAboutPage }) {
  const [isOpen, setIsOpen] = useState(true); // State to track if the sidebar is open
  const [currentPage, setCurrentPage] = useState('main-menu'); // Set default page to load

  // Function to toggle the sidebar
  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  // Function to handle menu item click
  const handleMenuItemClick = (page) => {
    setCurrentPage(page);
  };

  return (
    <div className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
      <div className="toggle-btn-container" onClick={toggleSidebar}>
        <div className="toggle-btn">
          {isOpen ? <span>&#x25C0;</span> : <span>&#x25B6;</span>}
        </div>
      </div>
      
      <div className="menu">
        <h1>F.A.S.T.</h1>
        <h2>Cyber Research Chatbot</h2>
        <ul>
          <li>
            <text className={`about-button ${!showAboutPage ? '' : 'active'}`} onClick={toggleAboutPage}>
              {showAboutPage ? "Chatbot ↩" : "About Us"}
            </text>
          </li>
          <li onClick={() => handleMenuItemClick('welcome')}>Welcome</li>
          <li onClick={() => handleMenuItemClick('how-to-use')}>How to Use</li>
          <li onClick={() => handleMenuItemClick('features')}>Features</li>
          <li onClick={() => handleMenuItemClick('faqs')}>FAQs</li>
        </ul>
      </div>

      <div className="border"></div>
      
      <div className="content">
        {currentPage === 'welcome' && (
          <div>
            <h2>Welcome</h2>
            <p>
              Welcome to the 2024 FAST Cyber Research Project! This website 
              itself runs using React.js for the frontend and Flask for the 
              backend and is currently only available through localhost. This 
              application uses the Langchain framework in order to incorporate 
              a customized chatbot, designed to answer user questions regarding 
              cybersecurity and other related features.
            </p>
          </div>
        )}
        {currentPage === 'how-to-use' && (
          <div>
            <h2>How to Use</h2>
            <p>
              To use the chatbot, enter a question in the input box below 
              or ask it to perform a specific task that is available through 
              Langchain agents.
            </p>
          </div>
        )}
        {currentPage === 'features' && (
          <div>
            <h2>Features</h2>
            <p>
              The chatbot is able to incorporate relevant information through a 
              Retrieval Model. This is done by querying a Postgres Vector Database, 
              which we can store embedded vectors obtained from pdfs and other word 
              documents. The Langchain LLM also uses Langchain agents which allows 
              you to utilize HuggingFact models within the transformer. These tasks 
              include (include tasks here).
            </p>
          </div>
        )}
        {currentPage === 'faqs' && (
          <div>
            <h2>FAQs</h2>
            <p>This is the FAQs page content.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Sidebar;