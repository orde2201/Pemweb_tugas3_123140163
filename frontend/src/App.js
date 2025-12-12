import React from 'react';
import ReviewForm from './components/ReviewForm';
import './App.css';

function App() {
  return (
    <div className="App">
      {/* Sidebar Navigation Header */}
      <header className="App-header">
        <div>
          <h1>
            🤖 AI Review<br/>Dashboard
          </h1>
          <div className="header-divider"></div>
          <p className="header-subtitle">
            Powerful AI-driven analysis to understand customer sentiments and insights from reviews
          </p>
        </div>
       
      </header>

      {/* Main Content */}
      <main>
        <div className="content-wrapper">
          <ReviewForm />
        </div>
      </main>
    </div>
  );
}

export default App;