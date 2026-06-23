import React from "react"
import inputsInfo from "../../inputInfo"

function APIForm({inputs, handleChange, onSubmit}){

  
    return (
        <div>
            <h2>Select Your Image Attributes</h2>
            <form className="form-container" onSubmit={onSubmit}>
                {inputs &&
                    Object.entries(inputs).map(([category, value], index) => (
                    <li className="form" key={index}>
                        <h2>{category} </h2>
                        <input
                        type="text"
                        name={category}
                        value={value}
                        placeholder="Input this attribute..."
                        onChange={handleChange}
                        className="textbox"
                        />
                        <br></br>
                        <br></br> 
                        <p> {inputsInfo[index]}</p>
                    </li>
                    ))}
                    <button type="submit" className="button">
                    Take that Pic! 🎞 
                    </button>
            </form>
        </div>

    )
}



export default APIForm