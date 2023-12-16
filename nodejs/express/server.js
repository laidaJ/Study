const mongoose = require('mongoose');
const dotenv = require('dotenv');
const app = require('./app');

dotenv.config({ path: './config.env' });

const DB = process.env.DATABASE.replace('<PASSWORD>', process.env.DATABASE_PASSWORD)
const connectDB = async () => {
    try {
        await mongoose.connect(DB);
        console.log('DB connect success')
    } catch (error) {
        console.error('DB connection error:', error);
    }
}
connectDB();

const catSchema = new mongoose.Schema({
    name: {
        type: String,
        require: [true, 'name needed'],
        unique: true
    },
    age: Number,
    color: String
})

const Cat = mongoose.model('Cat', catSchema)

const testCat = new Cat({
    name: 'naodaida',
    age: 10,
    color: 'white'
})

testCat.save().then(doc => {
    console.log(doc);
}).catch(err => {
    console.log(err)
}
)



const port = 3000;
app.listen(port, () => {
    console.log(`App is running on 127.0.0.1:${port}`);
})