import React from 'react';
import {Link} from 'react-router-dom';

export default function NavBar() {
  return (
    <nav>
      <a className="App-link">SPOTIFY LOGO HERE</a>
      <Link style={{color:"green"}} to="/Signup">Signup</Link>
      <Link style={{color:"green"}} to="/Login">Login</Link>
      <Link style={{color:"green"}} to="/Logout">Logout</Link>
    </nav>
  )
}
