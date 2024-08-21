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
          <div className="text_section text_odd">
            <h2 className="heading_section">Intelligent Feature Selection and Reduction</h2>
            <p className="details_section">Our platform harnesses cutting-edge algorithms to intelligently select and reduce features from your dataset. This process ensures that only the most relevant and impactful features are included, streamlining your models and eliminating unnecessary complexity. By focusing on the essential variables, our platform enhances model performance, making it more efficient and easier to interpret, ultimately leading to more accurate and insightful predictions.</p>
          </div>
          <div className="image_section">
            <img src="/ai.png" alt="Feature 1" />
          </div>
        </div>
        <div ref={el => cardsRef.current[1] = el} className="card_section">
          <div className="text_section text_even">
            <h2 className="heading_section">Automated Model Selection and Development</h2>
            <p className="details_section">Simplify and accelerate your workflow with our advanced automated model selection and development tools. These tools intelligently analyze your data and automatically select the most suitable models, ensuring optimal performance for your specific requirements. By tailoring the models to your unique needs, our platform not only saves time but also enhances the accuracy and effectiveness of your predictive analytics, allowing you to focus on strategic decision-making rather than the complexities of model development.</p>
          </div>
          <div className="image_section">
            <img src="/ai2.png" alt="Feature 2" />
          </div>
        </div>
        <div ref={el => cardsRef.current[2] = el} className="card_section">
          <div className="text_section text_odd">
            <h2 className="heading_section">Seamless AWS S3 Service for Models</h2>
            <p className="details_section">Effortlessly deploy, manage, and scale your models with our seamless integration into AWS S3. Our platform provides a robust and reliable storage solution that ensures your data and models are securely stored and easily accessible. With AWS S3's scalable architecture, you can efficiently handle growing volumes of data and models, allowing you to focus on innovation while we manage the complexities of storage and deployment.</p>
          </div>
          <div className="image_section">
            <img src="/ai3.png" alt="Feature 3" />
          </div>
        </div>
        <div ref={el => cardsRef.current[3] = el} className="card_section">
          <div className="text_section text_even">
            <h2 className="heading_section">Smooth Integration onto Client Server</h2>
            <p className="details_section">Our platform guarantees a seamless and efficient integration process, allowing you to deploy models directly into your client applications with ease. Designed for maximum compatibility, our solution minimizes the effort required to integrate sophisticated models into your existing infrastructure. Whether you're deploying on-premises or in the cloud, our platform ensures that your models are up and running quickly, reducing downtime and accelerating your time to market.</p>
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
