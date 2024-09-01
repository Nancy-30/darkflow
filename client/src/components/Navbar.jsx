import React from 'react'
import Logo from "../assets/Home/logo.png"
export default function Navbar() {
    return (
        <div className='flex items-center justify-between mt-2'>
            <ul className='text-white flex items-center gap-12'>
                <li className=''><img src={Logo} className="h-8" alt="logo" /></li>
                <li>Features</li>
                <li>Pricing</li>
                <li>FAQ</li>
            </ul>
            <button className='bg-white p-2 rounded-md'>Get Started</button>
        </div>
    )
}
