import React from 'react';
import "./FirstPage.css";
import Darkflow from "/darkflow.mp4";

export default function FirstPage() {
    return (
        <div className="first-page-container">
            <video
                className="first-page-video"
                src={Darkflow}
                autoPlay
                muted
                loop
                playsInline
            >
                Your browser does not support the video tag.
            </video>
        </div>
    )
}
