'use client';
import { useState } from 'react';

export default function AutoPromptGenerator() {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchPrompt = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/generate-auto-prompt');
      const data = await res.json();
      setPrompt(data.auto_prompt);
    } catch (err) {
      console.error(err);
      setPrompt('❌ Failed to fetch auto prompt. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: '2rem', textAlign: 'center' }}>
      <button
        onClick={fetchPrompt}
        disabled={loading}
        style={{
          padding: '0.75rem 1.5rem',
          fontSize: '1rem',
          backgroundColor: '#0070f3',
          color: 'white',
          border: 'none',
          borderRadius: '6px',
          cursor: 'pointer'
        }}
      >
        {loading ? 'Generating...' : '✨ Generate AI Prompt'}
      </button>
      {prompt && (
        <div style={{
          marginTop: '1.5rem',
          padding: '1rem',
          backgroundColor: '#ffffff',
          borderRadius: '8px',
          boxShadow: '0 0 10px rgba(0,0,0,0.1)',
          maxWidth: '600px',
          marginLeft: 'auto',
          marginRight: 'auto',
          color: '#333'
        }}>
          <h3 style={{ marginBottom: '0.5rem', fontWeight: 'bold' }}>Generated Prompt:</h3>
          <p>{prompt}</p>
        </div>
      )}
    </div>
  );
}
