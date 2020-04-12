import React from "react";
import logo from "./logo.svg";
import "./App.css";

import { logoutUser } from "./Routes";
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <button onClick={logoutUser} className="commonbtn">Logout</button>
      </header>
    </div>
  );
}

export default App;
