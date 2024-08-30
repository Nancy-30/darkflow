import React, { useEffect, useRef } from 'react';
import './Section2.css';
import { motion } from 'framer-motion';
import AI from '/ai.png';
import AI2 from '/ai2.png';
import AI3 from '/ai3.png';
import AI4 from '/ai4.webp';

const Section2 = React.forwardRef((props, ref) => {
  const cardsRef = useRef([]);

  useEffect(() => {
    const options = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1,
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, options);

    cardsRef.current.forEach((card) => observer.observe(card));

    return () => {
      cardsRef.current.forEach((card) => observer.unobserve(card));
    };
  }, []);

  // Key features JSON
  const features = [
    {
      id: 1,
      heading: 'Intelligent Feature Selection and Reduction',
      desc: 'Our platform harnesses cutting-edge algorithms to intelligently select and reduce features from your dataset...',
      image: AI,
    },
    {
      id: 2,
      heading: 'Automated Model Selection and Development',
      desc: 'Simplify and accelerate your workflow with our advanced automated model selection and development tools...',
      image: AI2,
    },
    {
      id: 3,
      heading: 'Seamless AWS S3 Service for Models',
      desc: 'Effortlessly deploy, manage, and scale your models with our seamless integration into AWS S3...',
      image: AI3,
    },
    {
      id: 4,
      heading: 'Smooth Integration onto Client Server',
      desc: 'Our platform guarantees a seamless and efficient integration process, allowing you to deploy models directly into your client applications...',
      image: AI4,
    },
  ];

  return (
    <>
      <div className="parent_section">
        <motion.div
          whileInView={{ opacity: 1, y: 0 }}
          initial={{ opacity: 0, y: -100 }}
          transition={{ duration: 1 }}
          className="heading1_div"
        >
          <h1 className="header_section">
            Our Key <span>Features</span>
          </h1>
          <p className="details_header_section">
            Discover the essential features of our platform that drive intelligent decision-making and seamless integration into your operations.
          </p>
        </motion.div>
      </div>

      <div className="container_section">
        {features.map((feature, index) => (
          <div key={index} ref={(el) => (cardsRef.current[index] = el)} className="card_section">
            {/* text div */}
            <motion.div
              className={`text_section ${index % 2 === 0 ? 'text_odd' : 'text_even'}`}
              whileInView={{ opacity: 1, x: 0 }}
              initial={{ opacity: 0, x: index % 2 === 0 ? -100 : 100 }}
              transition={{ duration: 1 }}
            >
              <h2 className="heading_section">{feature.heading}</h2>
              <p className="details_section">{feature.desc}</p>
            </motion.div>

            {/* image div */}
            <motion.div
              whileInView={{ opacity: 1, x: 0 }}
              initial={{ opacity: 0, x: index % 2 === 0 ? 100 : -100 }}
              transition={{ duration: 1 }}
              className="image_section"
            >
              <img src={feature.image} alt={feature.id} />
            </motion.div>
          </div>
        ))}
      </div>
    </>
  );
});

export default Section2;
