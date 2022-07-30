import React, { useState, useEffect } from 'react';
import { useLocation } from "react-router-dom";
//import * as ReactBootStrap from 'react-bootstrap';
import Spinner from 'react-bootstrap/Spinner';
import RangeSlider from 'react-bootstrap-range-slider';
// import Wave from 'react-wavify';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';


export default function Login() {

  const [valence, setValence] = useState(.5);
  const [energy, setEnergy] = useState(.5);
  const [danceability, setDanceability] = useState(.5);
  const [token_info, setToken_info] = useState({});
  const [loading, setLoading] = useState(false)


  function useQuery() {
    return new URLSearchParams(useLocation().search);
  }

  const query = useQuery();

  useEffect(() => {

    let token_info_obj = {}; // { access_token: "asdasa" }
    for (const [key, value] of query) { // token_type, "type"
      const new_obj = {
        [key]: value
      }; // { token_type: "type" }
      token_info_obj = Object.assign(token_info_obj, new_obj); 
      // 1. { access_token: "asdasa" } 2. { token_type: "type" } 3. merge #2 into #1 4. { access_token: "asdasa", token_type: "type" etc }
    }
    setToken_info(token_info_obj); // token_info = { expires: '', access_token: '', ... }
  }, [])

  const sendMood = async () => {
    const userData = JSON.stringify({
      valence: valence,
      energy: energy,
      danceability: danceability,
      token_info: token_info,
    })

    const config = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: userData,
      mode: 'cors',
    }
    const response = await fetch("http://localhost:5000/generateplaylist", config);
    const data = await response.json()
    setLoading(true);

    

  };
  ;
  function setMood(valence, energy, danceability) {
    setValence(valence)
    setEnergy(energy)
    setDanceability(danceability)
  }

  // const Wave = () => (
  //   <Wave fill='#f79902'
  //         paused={false}
  //         options={{
  //           height: 20,
  //           amplitude: 20,
  //           speed: 0.15,
  //           points: 3
  //         }}
  //   />
  // )

  return (
    <div className="Login">
      <h1>Welcome to Moodplayer</h1>
      {/* <Wave/> */}
      {loading ? danceability : <Spinner animation="border" /> }
      <h2>Please select values from 0.0 to 1.0</h2>
      <button className="relaxedButton" onClick={e => setMood(.9, .2, .1)}>Relaxed</button>
      <button className="energizedButton" onClick={e => setMood(.9, .9, .8)}>Energized</button>
      <button className="DefiantButton" onClick={e => setMood(.2, .8, .3)}>Defiant</button>
      <button className="melancholicButton" onClick={e => setMood(.3, .1, .1)}>Melancholic</button>
      <h3>Valence</h3>
        <RangeSlider value={valence} min={0.0} max={1.0} step={.1} variant='success' onChange={changeEvent => setValence(changeEvent.target.value)}/> 
      <h3>Energy</h3>
        <RangeSlider value={energy} min={0.0} max={1.0} step={.1} variant='success' onChange={changeEvent => setEnergy(changeEvent.target.value)}/>
      <h3>Danceability</h3>
        <RangeSlider value={danceability} min={0.0} max={1.0} step={.1} variant='success' onChange={changeEvent => setDanceability(changeEvent.target.value)}/>
        <div className="button">
        <button onClick={sendMood}>Submit</button>
        </div>
    </div>
  );
}


