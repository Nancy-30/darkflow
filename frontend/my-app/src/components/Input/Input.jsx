import React, { forwardRef } from 'react';
import { useNavigate } from 'react-router-dom';
import './Input.css';

const Input = forwardRef((props, ref) => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
    alert('Estimate submitted!');
    
    navigate('/stats'); 
  };

  return (
    <div className="info-modal-overlay" ref={ref}>
      <div className="parent2_section">
        <div className="heading_div">
          <h1 className="header_section">Elevate Your Machine<span> Learning </span>Capabilities </h1>
          <p className="details_header_section">
          Harness the power of our cutting-edge machine learning technology to revolutionize your business operations and stay ahead.
          </p>
        </div>
      </div>

      <div className="info-modal-content">
        <div className="info-text">
          <h1>Unlock the Future of Machine Learning</h1>
          <br />
          <p>Discover the Power of ML-Ops: Effortlessly Manage and Scale Your</p>
          <p>Propel Your Business Forward with Our Innovative ML Solutions</p>
          <img src="/Input2.gif" alt="Ai animation" className="gif-animation" />
        </div>
        
        <div className="modal-content">
          <h2>Get Started</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="csvFile">Upload CSV File</label>
              <input type="file" id="csvFile" name="csvFile" accept=".csv" required />
            </div>
            <div className="form-group">
              <label htmlFor="primaryKey">Primary Key Column</label>
              <input type="text" id="primaryKey" name="primaryKey" required />
            </div>
            <div className="form-group">
              <label htmlFor="targetColumn">Target Column</label>
              <input type="text" id="targetColumn" name="targetColumn" required />
            </div>
            <button type="submit" className="submit-button">
              Let's Go
            </button>
          </form>
        </div>
      </div>
    </div>
  );
});

export default Input;
