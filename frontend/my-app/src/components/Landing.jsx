import React, { useRef } from 'react';
import './Landing.css';
import Input from './Input'; // Ensure the correct path to Input component

export default function Landing() {
  const inputRef = useRef(null);

  const scrollToInput = () => {
    if (inputRef.current) {
      inputRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <>
      <section className="landing-section">
        <div className="landing-container">
          <span className="landing-title">Accelerate Your</span>
          <span className="landing-subtitle">ML Workflow</span>
          <div className="landing-text">
            Unlock the power of machine learning with our cutting-edge platform.
            Streamline your workflow, automate processes
          </div>
          <div className="landing-buttons">
            <button className="landing-button-primary" onClick={scrollToInput}>
              Get Started
            </button>
            <button className="landing-button-secondary">Learn More</button>
          </div>
        </div>
      </section>
      <Input ref={inputRef} />
    </>
  );
}
