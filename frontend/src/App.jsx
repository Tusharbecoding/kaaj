import React, { useState } from "react";
import SearchForm from "./components/SearchForm";
import ResultsTable from "./components/ResultsTable";
import Header from "./components/Header";
import styles from "./styles/App.module.css";

function App() {
  const [data, setData] = useState([]);

  const handleResults = (results) => {
    setData(results);
  };

  return (
    <div className={styles.app}>
      <Header title="Florida Business Search" />
      <SearchForm onResults={handleResults} />
      <ResultsTable data={data} />
    </div>
  );
}

export default App;
