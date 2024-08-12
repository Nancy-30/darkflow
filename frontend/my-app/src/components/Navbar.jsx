import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; 

export default function Navbar() {
  return (
    <nav>
      <div className="text-title">
        Asccelerate
      </div>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/products">Products</Link>
        <Link to="/partners">Partners</Link>
        <button className="start-button">
          Get  Started
        </button>
      </div>
    </nav>
  );
}
