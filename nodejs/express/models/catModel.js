const mongoose = require("mongoose");

const catSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'A cat need a name'],
        unique: true,
        trim: true
    },
    breed: {
        type: String,
        require: [true, 'breed is needed'],
    },
    age: {
        type: Number,
        require: [true, 'no age, really?'],
    },
    gender: String,
    price: Number,
    mainImage: {
        type: String,
        require: [true, 'Need a image'],
    },
    images: [String],
    birthDate: {
        type: Date,
        require: [true, 'don\'t remember?'],
    },
    createTime: {
        type: Date,
        default: Date.now()
    }
})

const Cat = mongoose.model('Cat', catSchema);

module.exports = Cat;