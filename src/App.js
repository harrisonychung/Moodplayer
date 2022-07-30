import React, {useState, useEffect} from 'react';
import {Route, BrowserRouter, Redirect} from 'react-router-dom';
import Generate from './Components/Generate';
import Logout from './Components/Logout';
import Signin from './Components/Signin';
import About from './Components/About';
import ClimbingBoxLoader from "react-spinners/ClimbingBoxLoader";
import {Navbar, Nav, NavDropdown} from "react-bootstrap";
import {LinkContainer} from "react-router-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css'
import './App.css';
import './Navbar.css';

function App() {
    const [loading, setLoading] = useState(false);



    useEffect(() => {
      setLoading(true)
      setTimeout(() => {  
        setLoading(false)
      }, 1000)
    }, [])



  return (
      <div className="App">
        {loading ?

        <ClimbingBoxLoader 
        color={"#17FF03"} 
        loading={loading} 
        size={50} />
        :
      <div className = "Navbar">
      <BrowserRouter>
      <Navbar collapseOnSelect expand="lg" variant="dark">
  <Navbar.Brand href="http://localhost:3000/Generate?access_token=BQAzr1OT1aKXld6NBjUZ2g15uD7NdLgINA2nL5tI0FAmcoGYvMH1xxIlxFAKxjW53SUjCQFjGfwZt0oBzMuSXVznxGCz1G0Q3cSQE8P9bapLWxX-pM1heiIvpGi4idSL8bhFbsM2LEChNi3p2VIxjHob0_hc2r2hjFQ_WnBiedjj3WCLSlrDPp1wF4sxB3oj7dPMY2IRgdtfyDS2-hS_yuvHrp7UoXgim2PM5g&expires_at=1622734082&expires_in=3600&refresh_token=AQDm7fZ9CxD4dTezZD_MZDR1bdPg8Ma2QD66-4tA28G0hkajIO66yt1vFIGJ859vQLv7oWmOu7DcUKWZFu1FEwHGJZw1l5F1N3Fl7Y9yrb6lQOjFfdHdAWv51Wn4CpdbSHA&scope=playlist-modify-private,playlist-modify-public,user-top-read,user-follow-read&token_type=Bearer">MoodPlayer</Navbar.Brand>
  <Navbar.Toggle aria-controls="responsive-navbar-nav" />
  <Navbar.Collapse id="responsive-navbar-nav">
    <Nav className="NavbarLinks">
      <LinkContainer to= "/Generate?access_token=BQAzr1OT1aKXld6NBjUZ2g15uD7NdLgINA2nL5tI0FAmcoGYvMH1xxIlxFAKxjW53SUjCQFjGfwZt0oBzMuSXVznxGCz1G0Q3cSQE8P9bapLWxX-pM1heiIvpGi4idSL8bhFbsM2LEChNi3p2VIxjHob0_hc2r2hjFQ_WnBiedjj3WCLSlrDPp1wF4sxB3oj7dPMY2IRgdtfyDS2-hS_yuvHrp7UoXgim2PM5g&expires_at=1622734082&expires_in=3600&refresh_token=AQDm7fZ9CxD4dTezZD_MZDR1bdPg8Ma2QD66-4tA28G0hkajIO66yt1vFIGJ859vQLv7oWmOu7DcUKWZFu1FEwHGJZw1l5F1N3Fl7Y9yrb6lQOjFfdHdAWv51Wn4CpdbSHA&scope=playlist-modify-private,playlist-modify-public,user-top-read,user-follow-read&token_type=Bearer">
      <Nav.Link>Generate</Nav.Link>
      </LinkContainer>
      <LinkContainer to= "/Signin">
      <Nav.Link>Sign In</Nav.Link>
      </LinkContainer>
      <NavDropdown title="About" id="collasible-nav-dropdown">
        <NavDropdown.Item href="/About">Attributes</NavDropdown.Item>
        <NavDropdown.Divider />
        <NavDropdown.Item href="/Logout">Logout</NavDropdown.Item>
      </NavDropdown>
    </Nav>
  </Navbar.Collapse>
      </Navbar>
      <Route path="/Generate">
        <Generate />
      </Route>
      <Route path="/Signin">
        <Signin /> 
      </Route>
      <Route path="/Logout">
        <Logout />
      </Route>
      <Route path="/About">
        <About />
      </Route>
      </BrowserRouter>
        </div>
        }
      </div>
  

      
  )
  };
export default App;
  

{/* <React.Fragment>
        <div className="spotifyPlayer">
      <SpotifyPlayer
      uri="spotify:playlist:01HFS0rjiMRnRe2zpyHz6i?si=d80a3459ee2b4dee"
      size={size}
      theme="black"
      view="coverart"
      />
      </div>
      </React.Fragment> */}

  


 
  
