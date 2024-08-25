import React, { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import Landing from './components/Landing/Landing';
import Footer from './components/Footer/Footer';
import Stats from './components/Stats/Stats';
import FirstPage from './components/FirstPage/FirstPage';

export default function Home() {
  const [showFirstPage, setShowFirstPage] = useState(true);
  useEffect(() => {
    const timer = setTimeout(() => {
      setShowFirstPage(false);
    }, 2000); // Display FirstPage for 2 seconds

    return () => clearTimeout(timer); // Clean up the timer on unmount
  }, []);

  return (
    <>
      {showFirstPage ? (
        <FirstPage />
      ) : (
        <>
          <Navbar />
          <main>
            <Routes>
              <Route path="/" element={<Landing />} />
              <Route path="/stats" element={<Stats />} />
            </Routes>
          </main>
          <Footer />
        </>
      )}
    </>
  );
}
