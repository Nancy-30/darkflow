import React from 'react';

function Footer() {
  return (
    <footer className="bg-black text-white py-6 border-t-white border-t-[0.5px] mt-10">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <h2 className="text-lg font-bold">DarkFlow</h2>
            <p className="text-sm">&copy; 2024 DarkFlow. All rights reserved.</p>
          </div>
          <nav className="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-4">
            <a href="/" className="">Home</a>
            <a href="#" className="">Contact</a>
          </nav>
        </div>
      </div>
    </footer>
  );
}

export default Footer;