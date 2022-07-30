import React from 'react';
import "../App.css"
// import Wave from 'react-wavify'


export default function Signin() {
    const url ="https://accounts.spotify.com/en/login?continue=https:%2F%2Faccounts.spotify.com%2Fauthorize%3Fscope%3Dplaylist-modify-private%252Cplaylist-modify-public%252Cuser-top-read%252Cuser-follow-read%26response_type%3Dcode%26redirect_uri%3Dhttp%253A%252F%252F127.0.0.1%253A5000%252Fapi_callback%26client_id%3D04eba6a8f0b64077965d175049476f60"


    return (
        <React.Fragment>
             {/* <Wave fill='#1DB954'
        paused={false}
        options={{
          height: 40,
          amplitude: 20,
          speed: 1.00,
          points: 3
        }}
        /> */}
        <a href ={url} class="button bttLog" style={{backgroundcolor:"#f14ebd"}}>Click To Sign In Spotify</a>
        </React.Fragment>
    
       
        )
}