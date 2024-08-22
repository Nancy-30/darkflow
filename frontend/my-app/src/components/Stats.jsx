import { Button } from "./ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "./ui/card";
import "./Stats.css"; 

export default function Stats() {
  return (
    <div className="container">
      <div className="content-box">
        <div className="header">
          <div className="button_div">
          <button className="header-title">Key</button>
          <button className="header-title">Key</button>
          <button className="header-title">Key</button>
          </div>
          <Button className="download-button">Download Model</Button>
        </div>
        <div className="cards-container">
          <div className="model-section">
            <h3 className="model-title">Model</h3>
            <button className="model-description">Comprehensive Analysis of Model Metrics</button>
            <button className="model-description">Comprehensive Analysis of Model Metrics</button>
            <button className="model-description">Comprehensive Analysis of Model Metrics</button>
            <button className="model-description">Comprehensive Analysis of Model Metrics</button>
            <button className="model-description">Comprehensive Analysis of Model Metrics</button>
          </div>
          <div className="cards-grid">
            <Card className="card">
              <CardHeader>
                <CardTitle className="card-title">Accuracy</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="card-content">The model's prediction accuracy on the test dataset exceeds industry</p>
              </CardContent>
            </Card>
            <Card className="card">
              <CardHeader>
                <CardTitle className="card-title">Model Efficiency</CardTitle>
              </CardHeader>
              <CardContent className="card-content-icon">
                <PowerIcon className="icon" />
                <p className="card-content-text">The model's streamlined architecture delivers</p>
              </CardContent>
            </Card>
            <Card className="card">
              <CardHeader>
                <CardTitle className="card-title">Customize</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="card-content">Explore Variables</p>
                <p className="card-content">View</p>
                <p className="card-content">Dive deeper into the model's performance with interactive charts and</p>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}

function PowerIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M12 2v10" />
      <path d="M18.4 6.6a9 9 0 1 1-12.77.04" />
    </svg>
  );
}
