import React from 'react'
import Wave from 'react-wavify'

export default function Animation() {
const App = () => (
  <Wave fill='#f79902'
        paused={false}
        options={{
          height: 15,
          amplitude: 20,
          speed: 0.15,
          points: 3
        }}
  />
)
    }