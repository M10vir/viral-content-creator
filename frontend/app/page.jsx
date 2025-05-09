// frontend/app/page.jsx

import TrendingInsightCard from './components/TrendingInsightCard';

export default function HomePage() {
  return (
    <main style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      minHeight: '100vh',
      backgroundColor: '#f5f5f5',
      fontFamily: 'Arial, sans-serif',
      padding: '2rem'
    }}>
      <h1 style={{ fontSize: '3rem', color: '#333', textAlign: 'center' }}>
        M10 Viral Content Creator 🚀
      </h1>
      <p style={{ fontSize: '1.25rem', marginTop: '1rem', color: '#555', textAlign: 'center' }}>
        Create research-backed, AI-powered viral posts for LinkedIn & beyond.
      </p>

      <TrendingInsightCard />
    </main>
  );
}
