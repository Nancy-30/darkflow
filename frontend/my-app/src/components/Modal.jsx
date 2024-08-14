import React, { useState } from 'react';
import './Modal.css';

export default function Modal({ isOpen, onClose }) {
  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
    alert('Estimate submitted!');
    onClose();
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="modal-close" onClick={onClose}>
          &times;
        </button>
        <h2>Get Started</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="primaryKey">Primary Key Column</label>
            <input type="text" id="primaryKey" name="primaryKey" required />
          </div>
          <div className="form-group">
            <label htmlFor="targetColumn">Target Column</label>
            <input type="text" id="targetColumn" name="targetColumn" required />
          </div>
          <div className="form-group">
            <label htmlFor="csvFile">Upload CSV File</label>
            <input type="file" id="csvFile" name="csvFile" accept=".csv" required />
          </div>
          <button type="submit" className="submit-button">
            Estimate
          </button>
        </form>
      </div>
    </div>
  );
}
