import React, { useState } from "react";
import "./Stats.css";

export default function Stats() {
  const [showModelSection, setShowModelSection] = useState(false);

  const handleButtonClick = () => {
    setShowModelSection(true);
  };

  return (
    <div className="visualization-page">
      <h2 className="heading">Visualization:<span> Name of the Dataset</span></h2>
      
      <div className="grid-container">
        <div className="graph-container">
          <div className="graph">Graph 1</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 2</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 3</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 4</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 5</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 6</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 7</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 8</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
        <div className="graph-container">
          <div className="graph">Graph 9</div>
          <p className="name_of_graph">Lorem ipsum dolor sit.</p>
        </div>
      </div>
      
      <div className="button-container">
        <p className="find_model">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum ratione saepe ipsa, accusantium perferendis incidunt sunt officiis quaerat. Cupiditate, omnis?</p>
        <button className="find-model-button" onClick={handleButtonClick}>
          Find your best model
        </button>
      </div>

      {showModelSection && (
        <div className="model-section">
          <div className="model-container">
            <h3>Accuracy</h3>
            <p>85%</p>
          </div>
          <div className="model-container">
            <h3>Precision & Recall</h3>
            <p>Precision: 82%</p>
            <p>Recall: 78%</p>
          </div>
          <div className="model-container">
            <h3>Model Details</h3>
            <p>This model is a Random Forest classifier...</p>
          </div>

          <div className="toggle-buttons">
            <button className="toggle-button">Model 1</button>
            <button className="toggle-button">Model 2</button>
            <button className="toggle-button">Model 3</button>
          </div>
        </div>
      )}
    </div>
  );
}
