import React, { useState } from "react";
import "./Stats.css";

export default function Stats() {
  const [selectedModel, setSelectedModel] = useState(null);

  const handleButtonClick = (model) => {
    setSelectedModel(model);
  };

  const renderModelDetails = () => {
    switch (selectedModel) {
      case 'KNN':
        return (
          <>
            <div className="model-container">
              <h3>Accuracy</h3>
              <p>90%</p>
            </div>
            <div className="model-container">
              <h3>Precision & Recall</h3>
              <p>Precision: 88%</p>
              <p>Recall: 85%</p>
            </div>
            <div className="model-container">
              <h3>Model Details</h3>
              <p>This model is a K-Nearest Neighbors classifier...</p>
            </div>
          </>
        );
      case 'SVM':
        return (
          <>
            <div className="model-container">
              <h3>Accuracy</h3>
              <p>92%</p>
            </div>
            <div className="model-container">
              <h3>Precision & Recall</h3>
              <p>Precision: 90%</p>
              <p>Recall: 89%</p>
            </div>
            <div className="model-container">
              <h3>Model Details</h3>
              <p>This model is a Support Vector Machine classifier...</p>
            </div>
          </>
        );
      case 'Random Forest':
        return (
          <>
            <div className="model-container">
              <h3>Accuracy</h3>
              <p>88%</p>
            </div>
            <div className="model-container">
              <h3>Precision & Recall</h3>
              <p>Precision: 85%</p>
              <p>Recall: 83%</p>
            </div>
            <div className="model-container">
              <h3>Model Details</h3>
              <p>This model is a Random Forest classifier...</p>
            </div>
          </>
        );
      case 'Logistic Regression':
        return (
          <>
            <div className="model-container">
              <h3>Accuracy</h3>
              <p>84%</p>
            </div>
            <div className="model-container">
              <h3>Precision & Recall</h3>
              <p>Precision: 80%</p>
              <p>Recall: 78%</p>
            </div>
            <div className="model-container">
              <h3>Model Details</h3>
              <p>This model is a Logistic Regression classifier...</p>
            </div>
          </>
        );
      default:
        return (
          <>
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
          </>
        );
    }
  };

  return (
    <div className="visualization-page">
      <h2 className="heading">Visualization:<span> Name of the Dataset</span></h2>
      
      <div className="grid-container">
        {/* Graph Containers */}
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
        {/* Repeat for other graph containers */}
      </div>
      
      <div className="button-container">
        <p className="find_model">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum ratione saepe ipsa, accusantium perferendis incidunt sunt officiis quaerat. Cupiditate, omnis?</p>
        <button
          className="find-model-button"
          onClick={() => handleButtonClick('Linear Regression')}
        >
          {selectedModel ? 'Change Model' : 'Find your best model'}
        </button>
      </div>

      {selectedModel && (
        <div className="model-section">
          <h2 className="model-name">Model Name: <span>{selectedModel}</span></h2>

          {renderModelDetails()}

          <div className="toggle-buttons">
            <button className="toggle-button" onClick={() => handleButtonClick('KNN')}>KNN</button>
            <button className="toggle-button" onClick={() => handleButtonClick('SVM')}>SVM</button>
            <button className="toggle-button" onClick={() => handleButtonClick('Random Forest')}>Random Forest</button>
            <button className="toggle-button" onClick={() => handleButtonClick('Logistic Regression')}>Logistic Regression</button>
          </div>
        </div>
      )}
    </div>
  );
}
