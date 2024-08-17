import React, { useEffect, useRef } from 'react';
import './Section2.css';

const Section2 = React.forwardRef((props, ref) => {
  const cardsRef = useRef([]);

  useEffect(() => {
    const options = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, options);

    cardsRef.current.forEach(card => observer.observe(card));

    return () => {
      cardsRef.current.forEach(card => observer.unobserve(card));
    };
  }, []);

  return (
    <>
      <div className="parent_section">
        <h1 className="header_section">Our Key <span>Features</span></h1>
        <p className="details_header_section">Discover the essential features of our platform that drive intelligent decision-making and seamless integration into your operations.</p>
      </div>
      <div className="container_section">
        <div ref={el => cardsRef.current[0] = el} className="card_section">
          <div className="text_section">
            <h2 className="heading_section">Intelligent Feature Selection and Reduction</h2>
            <p className="details_section">Our platform utilizes advanced algorithms to automatically select and reduce features, ensuring that your models are optimized for performance without unnecessary complexity.</p>
          </div>
          <div className="image_section">
            <img src="/ai.png" alt="Feature 1" />
          </div>
        </div>
        <div ref={el => cardsRef.current[1] = el} className="card_section">
          <div className="text_section">
            <h2 className="heading_section">Automated Model Selection and Development</h2>
            <p className="details_section">Streamline your workflow with our automated model selection and development tools, which choose the best-performing models tailored to your specific needs.</p>
          </div>
          <div className="image_section">
            <img src="/ai2.png" alt="Feature 2" />
          </div>
        </div>
        <div ref={el => cardsRef.current[2] = el} className="card_section">
          <div className="text_section">
            <h2 className="heading_section">Seamless AWS S3 Service for Models</h2>
            <p className="details_section">Easily deploy and manage your models with our seamless integration with AWS S3, providing a reliable and scalable storage solution for your data and models.</p>
          </div>
          <div className="image_section">
            <img src="/ai3.png" alt="Feature 3" />
          </div>
        </div>
        <div ref={el => cardsRef.current[3] = el} className="card_section">
          <div className="text_section">
            <h2 className="heading_section">Smooth Integration onto Client Server</h2>
            <p className="details_section">Our platform ensures a smooth and efficient integration process, enabling you to deploy models directly into your client applications with minimal effort and maximum compatibility.</p>
          </div>
          <div className="image_section">
            <img src="/ai4.webp" alt="Feature 4" />
          </div>
        </div>
      </div>
    </>
  );
});

export default Section2;
