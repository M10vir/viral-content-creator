// frontend/app/page.jsx

export default function HomePage() {
  return (
    <main style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      justifyContent: 'center', 
      alignItems: 'center', 
      height: '100vh', 
      backgroundColor: '#f5f5f5', 
      fontFamily: 'Arial, sans-serif' 
    }}>
      <h1 style={{ fontSize: '3rem', color: '#333' }}>
        Welcome to M10 Viral Content Creator 🚀
      </h1>
      <p style={{ fontSize: '1.5rem', marginTop: '1rem', color: '#555' }}>
        Build viral posts across LinkedIn, Instagram, Twitter, TikTok effortlessly!
      </p>
    </main>
  );
}
