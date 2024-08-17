import React, { useRef } from 'react';
import './Landing.css';
import Input from './Input'; // Ensure the correct path to Input component
import Section2 from './Section2';

export default function Landing() {
  const inputRef = useRef(null);

  const scrollToInput = () => {
    if (inputRef.current) {
      inputRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <>
      <div className="landing-container">
        <div className="hero-section">
          <div className="hero-text">
            <h1>Accelerate Your</h1>
            <h1><span>ML</span> Work<span>Flow</span></h1>
            <p>Unlock the power of machine learning with our cutting-edge platform. Streamline your workflow, automate processes</p>
            <button className="cta-button" onClick={scrollToInput}>Get Started</button>
          </div>
          <div className="hero-image">
            <img src="/landing3.jpeg" alt="AI potential" />
          </div>
        </div>
      </div>
      <Section2 />
      <Input ref={inputRef} />
    </>
  );
}
