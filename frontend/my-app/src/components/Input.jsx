import React, { forwardRef } from 'react';
import './Input.css';

const Input = forwardRef((props, ref) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
    alert('Estimate submitted!');
    onClose();
  };
  return (
    <div className="info-modal-overlay" ref={ref}>
      <div className="info-modal-content">
        <div className="info-text">
          <h1>Unlock the Future of Machine Learning</h1>
          <br />
          <p>Discover the Power of ML-Ops: Effortlessly Manage and Scale Your</p>
          <p>Propel Your Business Forward with Our Innovative ML Solutions</p>
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
            Estimate
          </button>
        </form>
      </div>
      </div>
    </div>
  );
});

export default Input;
