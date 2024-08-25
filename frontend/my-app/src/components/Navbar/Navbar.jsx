import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; 

export default function Navbar() {
  return (
    <nav>
      <Link to ="/">
        <img src="/logo.png" height="40rem" alt="" />
      </Link>
      <div className="nav-links">
        {/* <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/products">Products</Link>
        <Link to="/partners">Partners</Link> */}
        <button className="start-button">
          Pricing
        </button>
      </div>
    </nav>
  );
}
