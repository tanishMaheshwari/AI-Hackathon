import React from "react";
import "./TitleBar.css";
import ViteLogo from "../assets/react.svg";
import LoginButton from "./LoginButton";
const TitleBar = () => {
  return (
    <div>
      <div className="title-bar-container">
        <div className="title-logo-container">
          <a href="/" className="title-logo-link">
            <img src={ViteLogo} alt="Logo"></img>
            <h1 className="title">AI Hackathon</h1>
          </a>
        </div>
        <div className="title-bar-links-container">
          <ul className="title-bar-links">
            <li>
              <a href="/">Home</a>
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
        <div className="login-button-container">
          <LoginButton
            action={() => {
              alert("Clicked the Login Button");
            }}
            innerText="Login / Sign Up"
          />
        </div>
      </div>
    </div>
  );
};

export default TitleBar;
