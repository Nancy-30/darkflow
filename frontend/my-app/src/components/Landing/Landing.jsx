import React, { useRef } from 'react';
import { useScroll, useTransform, motion } from 'framer-motion';
import './Landing.css';
import Input from '../Input/Input'; 
import Section2 from '../Section2/Section2';

export default function Landing() {
  const inputRef = useRef(null);
  const targetRef = useRef();

  const { scrollYProgress } = useScroll({
    target: targetRef,
    offset: ["end end", "end center"]
  })

  const opacity = useTransform(scrollYProgress, [0, 1], [1, 0])
  const scale = useTransform(scrollYProgress, [0, 0.6], [1, 0.8]);

  const scrollToInput = () => {
    if (inputRef.current) {
      inputRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section

    >
      <motion.div
        style={{ opacity }}
        ref={targetRef}
        className="landing-container">
        <motion.div style={{ scale, opacity }} className="hero-section">

          <motion.div
            whileInView={{ opacity: 1, y: 0 }}
            initial={{ opacity: 0, y: -100 }}
            transition={{ duration: 1 }}
            className="hero-text">
            <h1>Accelerate Your</h1>
            <h1><span>ML</span> Work<span>Flow</span></h1>
            <p>Unlock the power of machine learning with our cutting-edge platform. Streamline your workflow, automate processes</p>
            <button className="cta-button" onClick={scrollToInput}>Get Started</button>
          </motion.div>

          <motion.div
            whileInView={{ opacity: 1, y: 0 }}
            initial={{ opacity: 0, y: 100 }}
            transition={{ duration: 1 }} className="hero-image">
            <img src="/landing3.jpeg" alt="AI potential" />
          </motion.div>

        </motion.div>
      </motion.div>


      <Section2 />
      <Input ref={inputRef} />
    </section >
  );
}
