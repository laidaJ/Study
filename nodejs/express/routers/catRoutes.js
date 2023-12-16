//引入modules
const express = require('express');
const catController = require('./../control/catControllers')
const router = express.Router();

router.route('/')
    .get(catController.getAllCats)
    .post(catController.postCat)

router.route('/:id')
    .get(catController.getCat)
    .patch(catController.updateCat)
    .delete(catController.deleteCat)

module.exports = router;