import React, { useState } from 'react';

function App() {
 const [currentPage, setCurrentPage] = useState('about'); // Set default page to load

 const renderPage = () => {
   switch (currentPage) {
     case 'about':
       return <AboutPage />;
     case 'how-to-use':
       return <HowToUsePage />;
     case 'features':
       return <FeaturesPage />;
     case 'faqs':
       return <FAQsPage />;
     default:
       return null; // Return null for unknown pages
   }
 };

 return (
   <div className="App">
     <Sidebar setCurrentPage={setCurrentPage} />
     <div className="content">{renderPage()}</div>
   </div>
 );
}

function Sidebar({ setCurrentPage }) {
 return (
   <div className="sidebar">
     <h2>FAST Cyber Research Chatbot</h2>
     <ul>
       <li onClick={() => setCurrentPage('about')}>About Page</li>
       <li onClick={() => setCurrentPage('how-to-use')}>How to Use</li>
       <li onClick={() => setCurrentPage('features')}>Features</li>
       <li onClick={() => setCurrentPage('faqs')}>FAQs</li>
     </ul>
   </div>
 );
}

function AboutPage() {
 return null; // return nothing
}

function HowToUsePage() {
 return null; // Return nothing
}

function FeaturesPage() {
 return null; // Return nothing
}

function FAQsPage() {
 return null; // Return nothing
}

export default App;