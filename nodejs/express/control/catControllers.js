const fs = require('fs');

const cats = JSON.parse(fs.readFileSync(`${__dirname}/../json/cats.json`))

//设置routers回调函数
module.exports.getAllCats = (req, res) => {
    res.status(200).json({
        status: 'success',
        resulets: cats.length,
        data: {
            cats
        }
    })
}
module.exports.postCat = (req, res) => {
    const newId = cats[cats.length - 1].id + 1;
    const newCat = Object.assign({ id: newId }, req.body);
    cats.push(newCat);

    fs.writeFile(
        `${__dirname}/../json/cats.json`,
        JSON.stringify(cats),
        err => {
            if (err) {
                return res.status(404), json({ error: 'error' });
            } else
                res.status(201).json({
                    status: 'success',
                    data: {
                        cats: newCat
                    }
                });
        })
}

module.exports.getCat = (req, res) => {
    const catId = req.params.id * 1;
    const myCat = cats.find(el => el.id === catId);
    if (catId > cats.length - 1) {
        res.status(404).send('Id is not right')
    } else
        res.status(200).json({
            status: 'success',
            data: {
                cat: myCat
            }
        });
}
/*
const patchRoute = (req, res) => {
    const catId = req.params.id;
    if (catId > cats.length - 1) {
        res.status(404).send('cat is not right')
    } else {
        const myCat = cats[catId];
        cats.splice(catId, 1, "req.body");
        res.status(201).json(myCat)
    }
}
*/
module.exports.deleteCat = (req, res) => {
    const catId = req.params.id;
    if (catId > cats.length - 1) {
        res.status(404).send('Id is not right')
    } else {
        res.status(201).json({
            status: 'success',
            delete: cats[catId]
        })
        cats.splice(catId, 1)
    }
}