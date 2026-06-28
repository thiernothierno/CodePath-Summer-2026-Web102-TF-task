import React from "react"
import { useEffect, useState } from "react"
const API_KEY = import.meta.env.VITE_APP_API_KEY
const MESSARI_KEY = import.meta.env.VITE_MESSARI_APP_API_KEY

function CryptoNews() {

    const [newsList, setNewsList] = useState([])
    useEffect(() => {
        const messariCryptoNews = async () => {
            const response = await fetch("https://api.messari.io/topics/v1/current?sort=trending&page=1&limit=10",
            {
                "headers" : {
                    "x-messari-api-key" : MESSARI_KEY
                }
            })
            const data = await response.json()
            setNewsList(data)
            console.log(data)
        }
    
    messariCryptoNews().catch(console.error)
    }, [])

    return (
        <div>
        <h3>Crypto News</h3>
            <ul className="side-list">
                {newsList && newsList.map((article) => 
                <li className="news-article" key={article.title}><a href={article.url}>{article.title}</a></li>
           
                )}
            </ul>
        </div>
    )
    
}

export default CryptoNews