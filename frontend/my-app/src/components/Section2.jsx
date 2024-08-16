import React, { forwardRef } from 'react';
import './Section2.css';

const Section2 = forwardRef((props, ref) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
    alert('Estimate submitted!');
    onClose();
  };

  return (
    <>
      <div className="parent_section">
        <h1 className="header_section">Our Key Features</h1>
        <p className="details_header_section">Discover the essential features of our platform that drive intelligent decision-making and seamless integration into your operations.</p>
      </div>
      <div className="container_section">
        <div className="card_section">
          <h2 className="heading_section">Intelligent Feature Selection and Reduction</h2>
          <p className="details_section">Our platform utilizes advanced algorithms to automatically select and reduce features, ensuring that your models are optimized for performance without unnecessary complexity.</p>
        </div>
        <div className="card_section">
          <h2 className="heading_section">Automated Model Selection and Development</h2>
          <p className="details_section">Streamline your workflow with our automated model selection and development tools, which choose the best-performing models tailored to your specific needs.</p>
        </div>
        <div className="card_section">
          <h2 className="heading_section">Seamless AWS S3 Service for Models</h2>
          <p className="details_section">Easily deploy and manage your models with our seamless integration with AWS S3, providing a reliable and scalable storage solution for your data and models.</p>
        </div>
        <div className="card_section">
          <h2 className="heading_section">Smooth Integration onto Client Server</h2>
          <p className="details_section">Our platform ensures a smooth and efficient integration process, enabling you to deploy models directly into your client applications with minimal effort and maximum compatibility.</p>
        </div>
      </div>
    </>
  );
});

export default Section2;
