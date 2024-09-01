import React from 'react';
import Navbar from '../components/Navbar';
import Landing from '../components/Landing';
import Challenges from '../components/Challenges';
import MLOps_work from '../components/MLOps_work';

export default function Home() {
  return (
    <div>
      <Navbar/>
      <Landing />
      <Challenges />
      <MLOps_work />
    </div>
  )
}
