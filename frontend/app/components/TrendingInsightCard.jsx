// frontend/app/components/TrendingInsightCard.jsx

'use client';

import { useState } from 'react';

export default function TrendingInsightCard() {
  const [insight, setInsight] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchInsight = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('http://localhost:8000/generate-trending-insight');
      const data = await res.json();

      if (data.insight && typeof data.insight === 'string') {
        // If it's still a string, parse it
        const parsed = JSON.parse(data.insight);
        setInsight(parsed);
      } else if (typeof data.insight === 'object') {
        setInsight(data.insight);
      } else {
        throw new Error('Unexpected response structure');
      }

    } catch (err) {
      setError('⚠️ Failed to load insight: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      backgroundColor: '#fff',
      padding: '2rem',
      borderRadius: '12px',
      boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
      marginTop: '3rem',
      maxWidth: '800px',
      width: '100%'
    }}>
      <h2>🧠 Trending AI Insight</h2>

      <button onClick={fetchInsight} style={{
        backgroundColor: '#0070f3',
        color: '#fff',
        border: 'none',
        padding: '10px 16px',
        borderRadius: '5px',
        cursor: 'pointer',
        marginTop: '1rem'
      }}>
        ✨ Generate AI Insight
      </button>

      {loading && <p style={{ marginTop: '1rem' }}>Loading insight...</p>}

      {error && <p style={{ color: 'red', marginTop: '1rem' }}>{error}</p>}

      {insight && (
        <div style={{ marginTop: '2rem', lineHeight: '1.6', fontSize: '1rem' }}>
          <div dangerouslySetInnerHTML={{ __html: formatText(insight.formatted_post) }} />
          {insight.sources && (
            <div style={{ marginTop: '1rem' }}>
              <strong>🔗 Sources:</strong>
              <ul>
                {insight.sources.map((src, idx) => (
                  <li key={idx}>
                    <a href={src} target="_blank" rel="noopener noreferrer">{src}</a>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function formatText(text) {
  // Make hashtags bold and line breaks readable
  return text
    .replace(/#(\w+)/g, '<strong>#$1</strong>')
    .replace(/\n/g, '<br>');
}
