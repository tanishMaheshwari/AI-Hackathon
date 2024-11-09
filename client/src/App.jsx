import { useState } from "react";
import "./App.css";
import TitleBar from "./components/TitleBar";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <TitleBar />
      <div className="App">
        <h1>Counter</h1>
        <p>{count}</p>
        <button onClick={() => setCount(count + 1)}>Increment</button>
        <button onClick={() => setCount(count - 1)}>Decrement</button>
      </div>
    </>
  );
}

export default App;
