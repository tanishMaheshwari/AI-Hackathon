import React from "react";
import "./TitleBar.css";

const TitleBar = () => {
  return (
    <div>
      <div className="title-bar-container">
        <h1 className="title-bar">AI Hackathon</h1>
        <ul className="title-bar-links">
          <li>
            <a href="">Home</a>
          </li>
          <li>
            <a href="/predict">Predict</a>
          </li>
          <li>
            <a href="/about">About</a>
          </li>
          <li>
            <a href="/contact">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default TitleBar;
