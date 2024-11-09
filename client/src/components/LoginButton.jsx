import React from 'react'
import "./LoginButton.css";
const LoginButton = (props) => {
  return (
    <div>
      <button className='login-button' onClick={props.action} style={props.style}>{props.innerText}</button>
    </div>
  )
}

export default LoginButton
