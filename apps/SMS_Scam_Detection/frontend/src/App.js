import React, { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [sender, setSender] = useState("unknown");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeSMS = async () => {
    if (!message.trim()) {
      alert("Please enter an SMS message.");
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("https://sms-scam-detection-app.onrender.com/scam/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
          sender_known: sender,
        }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({
        decision: "Error",
        confidence: "Low",
        key_evidence: ["Could not connect to backend API."],
        recommended_actions: ["Make sure FastAPI backend is running."],
      });
    } finally {
      setLoading(false);
    }
  };

  const getDecisionClass = () => {
    if (!result) return "";
    if (result.decision?.toLowerCase().includes("scam")) return "danger";
    if (result.decision?.toLowerCase().includes("legitimate")) return "safe";
    return "warning";
  };

  return (
    <div className="app">
      <div className="hero">
        <div className="badge">AI + Cybersecurity</div>
        <h1>SMS Scam Detection System</h1>
        <p>
          Analyze suspicious SMS messages using a Hugging Face LLM and receive
          a structured scam risk assessment.
        </p>
      </div>

      <div className="container">
        <div className="card input-card">
          <h2>Analyze SMS</h2>

          <label>SMS Message</label>
          <textarea
            placeholder="Example: Your bank account will be blocked. Click this link now..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <label>Sender Status</label>
          <select value={sender} onChange={(e) => setSender(e.target.value)}>
            <option value="known">Known Sender</option>
            <option value="unknown">Unknown Sender</option>
            <option value="unsure">Unsure</option>
          </select>

          <button onClick={analyzeSMS} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze Message"}
          </button>
        </div>

        <div className="card info-card">
          <h2>What it checks</h2>
          <ul>
            <li>Urgency or pressure language</li>
            <li>Suspicious links</li>
            <li>Requests for money, OTP, or personal data</li>
            <li>Impersonation of banks, ATO, or delivery services</li>
          </ul>
        </div>
      </div>

      {result && (
        <div className={`result-card ${getDecisionClass()}`}>
          <h2>Analysis Result</h2>

          <div className="result-grid">
            <div>
              <span>Decision</span>
              <strong>{result.decision}</strong>
            </div>

            <div>
              <span>Confidence</span>
              <strong>{result.confidence}</strong>
            </div>
          </div>

          <div className="reason-box">
            <span>Key Evidence</span>
            <p>{result.key_evidence?.[0]}</p>
          </div>

          {result.recommended_actions && (
            <div className="actions-box">
              <span>Recommended Actions</span>
              <ul>
                {result.recommended_actions.map((action, index) => (
                  <li key={index}>{action}</li>
                ))}
              </ul>
            </div>
          )}

          <p className="disclaimer">
            {result.disclaimer || "This is not professional or legal advice."}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;