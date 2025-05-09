// frontend/app/page.jsx

import AutoPromptGenerator from './components/AutoPromptGenerator';

export default function HomePage() {
  return (
    <main style={{
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      minHeight: '100vh',
      backgroundColor: '#f5f5f5',
      fontFamily: 'Arial, sans-serif',
      padding: '2rem'
    }}>
      <h1 style={{ fontSize: '3rem', color: '#333', textAlign: 'center' }}>
        Welcome to M10 Viral Content Creator 🚀
      </h1>
      <p style={{ fontSize: '1.5rem', marginTop: '1rem', color: '#555', textAlign: 'center' }}>
        Build viral posts across LinkedIn, Instagram, Twitter, TikTok effortlessly!
      </p>

      <AutoPromptGenerator />
    </main>
  );
}
