import { useState } from "react";
import axios from "axios";

function SearchForm({ onResults }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const submitForm = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/api/search", null, {
        params: { business_name: query },
      });
      onResults(res.data);
    } catch (error) {
      console.error("Error fetching data:", error);
      onResults([]);
    } finally {
      setLoading(false);
    }
  };

  const formStyles = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    marginBottom: "20px",
  };

  const inputStyles = {
    width: "300px",
    padding: "10px",
    marginBottom: "10px",
    borderRadius: "5px",
    border: "1px solid #ccc",
    fontSize: "16px",
  };

  const buttonStyles = {
    padding: "10px 20px",
    borderRadius: "5px",
    backgroundColor: "#4CAF50",
    color: "#fff",
    border: "none",
    cursor: "pointer",
    fontSize: "16px",
    transition: "background-color 0.3s",
  };

  const buttonHoverStyles = {
    backgroundColor: "#45a049",
  };

  return (
    <form onSubmit={submitForm} style={formStyles}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter business name"
        style={inputStyles}
        disabled={loading}
      />
      <button
        type="submit"
        style={buttonStyles}
        onMouseEnter={(e) =>
          (e.target.style.backgroundColor = buttonHoverStyles.backgroundColor)
        }
        onMouseLeave={(e) =>
          (e.target.style.backgroundColor = buttonStyles.backgroundColor)
        }
        disabled={loading}
      >
        {loading ? "Loading..." : "Search"}
      </button>
    </form>
  );
}

export default SearchForm;
