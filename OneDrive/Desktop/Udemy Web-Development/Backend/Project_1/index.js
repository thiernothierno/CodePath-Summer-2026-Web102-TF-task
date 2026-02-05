import express from "express";
import axios from "axios";
import bodyParser  from "body-parser";


const app = express();
const port = 3000;
const JOKE_API = "https://v2.jokeapi.dev/joke";

app.use(bodyParser.urlencoded({extended : true}));
app.use(express.static("public"));

const categories = ["Programming", "Misc", "Pun", "Dark", "Spooky"];
const flags = ["nsfw", "religious", "political", "racist", "sexist", "explicit"];

const random_categorie = categories[Math.floor(Math.random(categories) * categories.length)];
console.log(random_categorie);
const random_flag = flags[Math.floor(Math.random(flags) * flags.length)];
console.log(random_flag)

app.get("/random", async(req, res) =>{
    try{
        const response = await axios.get(`${JOKE_API}/${random_categorie}/${random_flag}`);
        const joke = response.data;
        if (joke['type'] === 'single'){
            console.log(joke['joke']);
            res.json(joke['joke'])
        }

        else {
           const data = {
            "setup" : joke['setup'],
            "delivery" : joke['delivery']
           }
           console.log(data)
           res.json(data)
        }
        
    } catch(error){
        res.status(500).json({message : "Error fetching data."})
    }   
});

app.get("/joke/:id", async(req, res) => {
    try{
        const response = await axios.get(`${JOKE_API}/Any`);

    } catch(error){
        res.status(500).json({message: "ID not found."})
    }
})






app.listen(port, () => {
    console.log(`Server running on port ${port}`)
})