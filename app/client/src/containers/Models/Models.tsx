import { useState } from "react";

export const Models = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState("");
  const [data, setData] = useState(null);

  const handleButtonClick = async () => {
    setLoading(true);
    setResult("");
    setData(null);
    try {
      const response = await fetch("http://localhost:5000/analyze-network", {
        method: "POST",
      });
      const resData = await response.json();
      setResult(resData.message || "Analysis complete");
      setData(resData.data);
    } catch {
      setResult("Error occurred while performing analysis.");
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center gap-5 min-h-[48rem]">
      <h1 className="font-semibold text-center text-5xl">
        Network Analysis & IDS
      </h1>
      <button
        onClick={handleButtonClick}
        className="px-6 py-3 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75"
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Run Network Analysis"}
      </button>
      {result && (
        <div className="mt-6 p-4 bg-white rounded-lg shadow-md w-3/4 md:w-1/2 text-center">
          <p className="text-gray-700 font-semibold">{result}</p>
          {data && (
            <div className="mt-4 text-left text-gray-600">
              <p>CPU Usage: {data[0]}%</p>
              <p>Memory Usage: {data[1]}%</p>
              <p>Disk Usage: {data[2]}%</p>
              <p>Bytes Sent: {data[3]}</p>
              <p>Bytes Received: {data[4]}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
