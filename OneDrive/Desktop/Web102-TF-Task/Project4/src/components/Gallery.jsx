import React from "react";

const Gallery = ({ images }) => {

    return (
        <div>
            <h2></h2>
            <h2> Your Screenshot Gallery!</h2>
            <div>
                {images && images.length > 0 ? (
                    
                    images.map((pic, index) => (
                    <li className="gallery" key={index}>
                        <img
                        className="gallery-screenshot"
                        src={pic}
                        alt="Undefined screenshot from query"
                        width="500"
                        />
                    </li>
                    ))

                ): (
                    <div> 
                        <h2>No screenshot made. </h2>
                    </div>
                )}
            </div>


        </div>
    )



};

export default Gallery;