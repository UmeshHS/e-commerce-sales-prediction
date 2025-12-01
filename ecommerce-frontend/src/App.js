import React, { useState } from "react";
import axios from "axios";
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from "recharts";

export default function DemandPrediction() {
  const [formData, setFormData] = useState({
    product_id: 101,
    store_id: 1,
    price: 250,
    promotion: 1,
    stock_level: 50,
    day_of_week: 2,
    month: 8,
    review: "Customers love the product but feel it's a bit costly",
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("https://e-commerce-sales-prediction-f0ro.onrender.com", {
        ...formData,
        product_id: parseInt(formData.product_id),
        store_id: parseInt(formData.store_id),
        price: parseFloat(formData.price),
        promotion: parseInt(formData.promotion),
        stock_level: parseInt(formData.stock_level),
        day_of_week: parseInt(formData.day_of_week),
        month: parseInt(formData.month),
        review: formData.review,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error fetching prediction:", error);
    }
  };

  // Sentiment color handler
  const getSentimentColor = (sentiment) => {
    if (sentiment === "Positive") return "green";
    if (sentiment === "Negative") return "red";
    return "orange"; // Neutral
  };

  return (
    <div style={{ backgroundColor: "#e0e0e0", minHeight: "100vh", padding: "30px" }}>
      <div style={{
        maxWidth: "700px",
        margin: "auto",
        background: "#fff",
        padding: "25px",
        borderRadius: "12px",
        boxShadow: "0 6px 18px rgba(0,0,0,0.2)"
      }}>
        <h1 style={{ textAlign: "center", color: "#333" }}>📊 Demand Prediction & Prescription</h1>
        <form onSubmit={handleSubmit}>
          {["product_id", "store_id", "price", "promotion", "stock_level", "day_of_week", "month"].map((field) => (
            <div key={field} style={{ marginBottom: "15px" }}>
              <label style={{ display: "block", fontWeight: "bold", marginBottom: "5px" }}>
                {field.replace("_", " ").toUpperCase()}
              </label>
              <input
                type="text"
                name={field}
                value={formData[field]}
                onChange={handleChange}
                style={{
                  width: "100%",
                  padding: "10px",
                  borderRadius: "8px",
                  border: "1px solid #aaa"
                }}
              />
            </div>
          ))}

          {/* Review input */}
          <div style={{ marginBottom: "15px" }}>
            <label style={{ display: "block", fontWeight: "bold", marginBottom: "5px" }}>
              Customer Review / Feedback
            </label>
            <textarea
              name="review"
              value={formData.review}
              onChange={handleChange}
              rows="3"
              style={{
                width: "100%",
                padding: "10px",
                borderRadius: "8px",
                border: "1px solid #aaa"
              }}
            />
          </div>

          <button
            type="submit"
            style={{
              width: "100%",
              padding: "12px",
              background: "#333",
              color: "#fff",
              border: "none",
              borderRadius: "8px",
              fontSize: "16px",
              cursor: "pointer"
            }}
          >
            🔮 Predict & Prescribe
          </button>
        </form>

        {result && (
          <div style={{
            marginTop: "25px",
            padding: "20px",
            borderRadius: "10px",
            background: "#f9f9f9",
            border: "1px solid #ccc"
          }}>
            <h2 style={{ color: "#222" }}>Results</h2>
            <p><b>Predicted Units Sold:</b> {result.predicted_units_sold}</p>
            <p>
              <b>Sentiment:</b>{" "}
              <span style={{ color: getSentimentColor(result.sentiment), fontWeight: "bold" }}>
                {result.sentiment}
              </span>
            </p>
            <p><b>Recommendation:</b> {result.recommendation}</p>

            {/* Chart */}
            <div style={{ marginTop: "20px", height: "300px" }}>
              <ResponsiveContainer width="100%" height="100%">
                <BarChart
                  data={[
                    { name: "Predicted Demand", value: result.predicted_units_sold },
                    { name: "Stock Level", value: formData.stock_level }
                  ]}
                  margin={{ top: 20, right: 20, left: 0, bottom: 5 }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="value" fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
