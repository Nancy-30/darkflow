import React, { useState } from 'react';
import './Landing.css';
import Footer from './Footer';
import Modal from './Modal';

export default function Landing() {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleModalOpen = () => {
    setIsModalOpen(true);
  };

  const handleModalClose = () => {
    setIsModalOpen(false);
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
            <button className="landing-button-primary" onClick={handleModalOpen}>
              Get Started
            </button>
            <button className="landing-button-secondary">Learn More</button>
          </div>
        </div>
      </section>
      <Footer />
      <Modal isOpen={isModalOpen} onClose={handleModalClose} />
    </>
  );
}
