// const fs = require('fs');
const Cat = require('./../models/catModel')

exports.getAllCats = async (req, res) => {
    try {
        const cats = await Cat.find();
        res.status(200).json({
            status: 'success',
            resulets: cats.length,
            data: {
                cats
            }
        })
    } catch (err) {
        res.status(400).json({
            status: 'fail',
            message: err
        })
    }
}
exports.postCat = async (req, res) => {
    try {
        const newCat = await Cat.create(req.body);
        res.status(201).json({
            status: 'success',
            data: {
                cat: newCat
            }
        })
    } catch (err) {
        res.status(400).json({
            status: 'fail',
            message: err
        })
    }
}

exports.getCat = async (req, res) => {
    try {
        const cat = await Cat.findById(req.params.id);
        res.status(201).json({
            status: 'success',
            data: {
                cat
            }
        })
    } catch (err) {
        res.status(400).json({
            status: 'fail',
            message: err
        })
    }
}

exports.updateCat = async (req, res) => {
    try {
        const cat = await Cat.findByIdAndUpdate(req.params.id);
        res.status(201).json({
            status: 'success',
            data: {
                cat
            }
        })
    } catch (err) {
        res.status(400).json({
            status: 'fail',
            message: err
        })
    }
}

exports.deleteCat = async (req, res) => {
    try {
        await Cat.findByIdAndDelete(re.params.id);
        res.status(201).send('Deleted!😘')

    } catch (err) {
        res.status(400).json({
            status: 'fail',
            message: err
        })
    }
}