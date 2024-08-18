import React from "react";
import "./Footer.css";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-column">
            <img src="/tablogo.png" alt="logo"/>
            <h3>© 2024 DarkFlow</h3>
            <p>All rights reserved.</p>
        </div>
        <div className="footer-column">
          <h3>Quick Links</h3>
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#product">Product</a>
          <a href="#contact">Contact</a>
        </div>
        <div className="footer-column">
          <h3>Connect with Us</h3>
          <div className="footer-column-social">
            <a href="#twitter"><i className="fab fa-twitter"></i> Twitter</a>
            <a href="#linkedin"><i className="fab fa-linkedin"></i> LinkedIn</a>
            <a href="#instagram"><i className="fab fa-instagram"></i> Instagram</a>
            <a href="#facebook"><i className="fab fa-facebook"></i> Facebook</a>
          </div>
        </div>
        <div className="footer-column">
          <h3>Legal</h3>
          <a href="#terms">Terms</a>
          <a href="#privacy">Privacy</a>
          <a href="#cookie-policy">Cookie Policy</a>
          <a href="#sitemap">Sitemap</a>
        </div>
      </div>
    </footer>
  );
}
