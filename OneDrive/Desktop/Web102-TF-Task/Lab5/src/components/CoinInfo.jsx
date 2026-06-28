import React from "react";
import { useState } from "react";

const CoinInfo = ({id, image, name, symbol, price}) => {

    return (
        <div>
            <li className="main-list" key={id}>
                <img
                    className="icons"
                    src={image}
                    alt={`Small icon for ${name} crypto coin`}
                />
                {name} ({symbol})
                {price ? ` $${price} USD` : null}
            </li>
        </div>
    )

}





export default CoinInfo