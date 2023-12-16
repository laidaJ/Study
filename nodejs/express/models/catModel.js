const mongoose = require("mongoose");

const catSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'name needed'],
        unique: true
    },
    age: Number,
    color: String
})

const Cat = mongoose.model('Cat', catSchema);

module.exports = Cat;