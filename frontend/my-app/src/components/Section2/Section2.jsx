import React, { useEffect, useRef } from 'react';
import './Section2.css';
import { motion } from 'framer-motion';
import AI from '/ai.png';
import AI2 from '/ai2.png';
import AI3 from '/ai3.png';
import AI4 from '/ai4.webp'

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

  // key features json 
  const features = [
    {
      id: 1,
      heading: "Intelligent Feature Selection and Reduction",
      desc: "Our platform harnesses cutting-edge algorithms to intelligently select and reduce features from your dataset. This process ensures that only the most relevant and impactful features are included, streamlining your models and eliminating unnecessary complexity. By focusing on the essential variables, our platform enhances model performance, making it more efficient and easier to interpret, ultimately leading to more accurate and insightful predictions.",
      image: AI
    },

    {
      id: 2,
      heading: "Automated Model Selection and Development",
      desc: "Simplify and accelerate your workflow with our advanced automated model selection and development tools. These tools intelligently analyze your data and automatically select the most suitable models, ensuring optimal performance for your specific requirements. By tailoring the models to your unique needs, our platform not only saves time but also enhances the accuracy and effectiveness of your predictive analytics, allowing you to focus on strategic decision-making rather than the complexities of model development.",
      image: AI2
    },

    {
      id: 3,
      heading: "Seamless AWS S3 Service for Models",
      desc: "Effortlessly deploy, manage, and scale your models with our seamless integration into AWS S3. Our platform provides a robust and reliable storage solution that ensures your data and models are securely stored and easily accessible. With AWS S3's scalable architecture, you can efficiently handle growing volumes of data and models, allowing you to focus on innovation while we manage the complexities of storage and deployment.",
      image: AI3
    },

    {
      id: 4,
      heading: "Smooth Integration onto Client Server",
      desc: "Our platform guarantees a seamless and efficient integration process, allowing you to deploy models directly into your client applications with ease. Designed for maximum compatibility, our solution minimizes the effort required to integrate sophisticated models into your existing infrastructure. Whether you're deploying on-premises or in the cloud, our platform ensures that your models are up and running quickly, reducing downtime and accelerating your time to market.",
      image: AI4
    },

  ]

  return (
    <>
      <div className="parent_section">
        <motion.div
          whileInView={{ opacity: 1, y: 0 }}
          initial={{ opacity: 0, y: -100 }}
          transition={{ duration: 1 }}
          className='heading_div'>
          <h1 className="header_section">Our Key <span>Features</span></h1>
          <p className="details_header_section">Discover the essential features of our platform that drive intelligent decision-making and seamless integration into your operations.</p>
        </motion.div>
      </div>

      <div className="container_section">

        {
          features.map((feature, index) => (
            <div key={index} ref={el => cardsRef.current[index] = el} className="card_section">

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
                className="image_section">
                <img src={feature.image} alt={feature.id} />
              </motion.div>
            </div>
          ))
        }

      </div>
    </>
  );
});

export default Section2;
