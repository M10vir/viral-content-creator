import React, { useState } from "react";
import { fetchAutoPrompt } from "../api/useAutoPrompt";

function PostGeneratorPage() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const autoPrompt = await fetchAutoPrompt();
      setPrompt(autoPrompt);
    } catch (error) {
      console.error("Error generating prompt:", error);
    }
    setLoading(false);
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-semibold mb-4">Auto Prompt Generator</h1>
      <button
        className="px-4 py-2 bg-blue-600 text-white rounded"
        onClick={handleGenerate}
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate Prompt"}
      </button>
      {prompt && (
        <div className="mt-4 bg-gray-100 p-4 rounded shadow">
          <h2 className="text-md font-medium">Generated Prompt:</h2>
          <p className="mt-2">{prompt}</p>
        </div>
      )}
    </div>
  );
}

export default PostGeneratorPage;
