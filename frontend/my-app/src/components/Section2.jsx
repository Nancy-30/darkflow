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
      <h1 className="header_section">Lorem <span>ipsum</span> dolor <span></span></h1>
      <p className="details_header_section">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Deserunt, eos. Possimus dolorum tempore vel voluptates quia voluptatibus voluptate fuga ipsa minus repellendus consequatur voluptatum vero nihil assumenda, aperiam accusantium molestiae!</p>
    </div>
      <div className="container_section">
        <div className="card_section">
          <h2 className="heading_section">Lorem, ipsum dolor.</h2>
          <p className="details_section">Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam repellat totam fuga beatae rerum a fugiat magnam quasi ratione omnis aliquid quisquam perferendis corporis officia, velit facilis impedit ullam placeat ea temporibus iure quibusdam optio.</p>
        </div>
        <div className="card_section">
          <h2 className="heading_section">Lorem, ipsum dolor.</h2>
          <p className="details_section">Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam repellat totam fuga beatae rerum a fugiat magnam quasi ratione omnis aliquid quisquam perferendis corporis officia, velit facilis impedit ullam placeat ea temporibus iure quibusdam optio.</p>
        </div>
        <div className="card_section">
          <h2 className="heading_section">Lorem, ipsum dolor.</h2>
          <p className="details_section">Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam repellat totam fuga beatae rerum a fugiat magnam quasi ratione omnis aliquid quisquam perferendis corporis officia, velit facilis impedit ullam placeat ea temporibus iure quibusdam optio.</p>
        </div>
        <div className="card_section">
          <h2 className="heading_section">Lorem, ipsum dolor.</h2>
          <p className="details_section">Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam repellat totam fuga beatae rerum a fugiat magnam quasi ratione omnis aliquid quisquam perferendis corporis officia, velit facilis impedit ullam placeat ea temporibus iure quibusdam optio.</p>
        </div>
      </div>
    </>
  );
});

export default Section2;
