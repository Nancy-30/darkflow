import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import Landing from './components/Landing/Landing';
import Footer from './components/Footer/Footer';
import Stats from './components/Stats/Stats'; 

export default function Home() {
  return (
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
  );
}
