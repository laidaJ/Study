const app = require('./app');
const mongoose = require('mongoose')
const dotenv = require('dotenv')

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

const port = 3000;
app.listen(port, () => {
    console.log(`App is running on ${port}`)
})