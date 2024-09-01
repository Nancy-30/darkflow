import React from 'react'
import "./data_visual.css"
export default function Data_visual() {
  return (
    <div className='main-container'>
        <h1 className='main-heading'>Data Visualization</h1>
        <div className='plots'>
            <div className='plot'>
                <div className='plot-graph'>Correlation plot</div>
                <h2 className='plot-heading'>Correlation</h2>
            </div>
            <div className='plot'>
                <div className='plot-graph'>Pair Plot</div>
                <h2 className='plot-heading'>Pair Plot</h2>
            </div>
            <div className='plot'>
                <div className='plot-graph'>Histogram</div>
                <h2 className='plot-heading'>Histogram</h2>
            </div>
            <div className='plot'>
                <div className='plot-graph'>PCA Biplot</div>
                <h2 className='plot-heading'>PCA Biplot</h2>
            </div>
        </div>
    </div>
  )
}
