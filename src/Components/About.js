// import React from 'react';
// import {Jumbotron, Container, DropdownButton, Dropdown} from 'react-bootstrap'
import React from 'react';
import {useRef} from 'react';
import Flippy, { FrontSide, BackSide } from 'react-flippy';
import SpotifyPlayer from 'react-spotify-player';


export default function About() {
  const ref = useRef();
  const size = {
    width: '50%',
    height: 80,
  }
  
  return (
    <React.Fragment>
      <div className="dataFlip">
      <Flippy
      flipOnHover={false} // default false
      flipOnClick={true} // default false
      flipDirection="vertical" // horizontal or vertical
      ref={ref} // to use toggle method like ref.curret.toggle()
      // if you pass isFlipped prop component will be controlled component.
      // and other props, which will go to div
      style={{ width: '500px', height: '500px' }}
  >
    <FrontSide style={{ backgroundColor: 'linear-gradient(#c074b2, #1f2027);'}} >
      Valence <br />
      {/* <button onClick={() => { ref.current.toggle(); }}> Click To Flip</button> */}
    </FrontSide>
    <BackSide style={{ backgroundColor: 'linear-gradient(#c074b2, #1f2027);'}}>
    <p>Valence is a measure from 0.0 to 1.0 
        describing the musical positivity conveyed by a track.
         Tracks with high valence sound more positive 
          while tracks with low valence sound more 
           negative (e.g. sad, depressed, angry). <br></br>
           <br></br>
          Heartbreak Anniversary by Giveon is a track with low valence. </p>
    
    </BackSide>
    <div className="spotifyPlayer">
      <SpotifyPlayer
      uri="spotify:track:3FAJ6O0NOHQV8Mc5Ri6ENp"
      size={size}
      theme="black"
      view="coverart"
      />
      </div>
  </Flippy>

  <Flippy
      flipOnHover={false} // default false
      flipOnClick={true} // default false
      flipDirection="vertical" // horizontal or vertical
      ref={ref} // to use toggle method like ref.curret.toggle()
      // if you pass isFlipped prop component will be controlled component.
      // and other props, which will go to div
      style={{ width: '500px', height: '500px' }}
  >
    <FrontSide style={{ backgroundColor: 'linear-gradient(#c074b2, #1f2027);'}} >
      Energy <br />
      {/* <button onClick={() => { ref.current.toggle(); }}> Click To Flip</button> */}
    </FrontSide>
    <BackSide style={{ backgroundColor: 'linear-gradient(#c074b2, #1f2027);'}}>
    <p>Energy is a measure from 0.0 to 1.0 
           and represents a perceptual measure of intensity and activity. 
           Typically, energetic tracks feel fast, loud, and noisy. 
           For example, death metal has high energy, while a Bach prelude 
           scores low on the scale. Perceptual features contributing to this attribute 
           include dynamic range, perceived loudness, timbre, onset rate, and general entropy. <br></br>
           <br></br>
          Rockstar by DaBaby is a track with high energy.</p>
    
    </BackSide>
    <div className="spotifyPlayer">
      <SpotifyPlayer
      uri="spotify:track:7ytR5pFWmSjzHJIeQkgog4"
      size={size}
      theme="black"
      view="coverart"
      />
      </div>
  </Flippy>

  <Flippy
      flipOnHover={false} // default false
      flipOnClick={true} // default false
      flipDirection="vertical" // horizontal or vertical
      ref={ref} // to use toggle method like ref.curret.toggle()
      // if you pass isFlipped prop component will be controlled component.
      // and other props, which will go to div
      style={{ width: '500px', height: '500px' }}
  >
    <FrontSide style={{ backgroundColor: 'linear-gradient(#c074b2, #1f2027);'}} >
      Danceability <br />
      {/* <button onClick={() => { ref.current.toggle(); }}> Click To Flip</button> */}
    </FrontSide>
    <BackSide style={{ backgroundColor: 'linear-gradient(#c074b2, #1f2027);'}}>
    <p>Danceability describes how suitable a track is for
           dancing based on a combination of musical elements including tempo,
           rhythm stability, beat strength, and overall regularity. 
           A value of 0.0 is least danceable and 1.0 is most danceable.<br></br>
           <br></br>
           Butter by BTS is a track with high danceability.</p>
    
    </BackSide>
    <div className="spotifyPlayer">
      <SpotifyPlayer
      uri="spotify:track:2bgTY4UwhfBYhGT4HUYStN"
      size={size}
      theme="black"
      view="coverart"
      />
      </div>
  </Flippy>
      </div>
      </React.Fragment>
  )
}

// export default function About() {
//   return (
//       <div className="About">
//       <h1>Attributes</h1>

//       <div className="about-content">
//       <Jumbotron fluid>
//         <Container>
//         <DropdownButton id="valenceButton" title="Valence">
//           <Dropdown.Item>
//       <p>Valence: Valence is a measure from 0.0 to 1.0 <br></br>
//        describing the musical positiveness conveyed by a track.<br></br>
//         Tracks with high valence sound more positive <br></br> 
//         (e.g. happy, cheerful, euphoric), <br></br>
//          while tracks with low valence sound more <br></br>
//           negative (e.g. sad, depressed, angry). </p>
//         </Dropdown.Item>
//         </DropdownButton>
//       </Container>
//       </Jumbotron>

//       <Jumbotron fluid>
//         <Container>
//         <DropdownButton id="energyButton" title="Energy">
//           <Dropdown.Item>
//           <p>Energy: Energy is a measure from 0.0 to 1.0 <br></br>
//            and represents a perceptual measure of intensity and activity. <br></br>
//           Typically, energetic tracks feel fast, loud, and noisy. <br></br> 
//           For example, death metal has high energy, while a Bach prelude <br></br>
//           scores low on the scale. Perceptual features contributing to this attribute <br></br>
//            include dynamic range, perceived loudness, timbre, onset rate, and general entropy.</p>  
//           </Dropdown.Item>
//           </DropdownButton>
//         </Container>
//         </Jumbotron>

//       <Jumbotron fluid>
//         <Container>
//       <DropdownButton id="danceabilityButton" title="Danceability">
//         <Dropdown.Item>
//         <p>Danceability: Danceability describes how suitable a track is for <br></br>
//           dancing based on a combination of musical elements including tempo,<br></br>
//           rhythm stability, beat strength, and overall regularity. <br></br>
//           A value of 0.0 is least danceable and 1.0 is most danceable.</p>
//         </Dropdown.Item>
//       </DropdownButton>
//       </Container>
//       </Jumbotron>
//       </div>
//       </div>
//   )
