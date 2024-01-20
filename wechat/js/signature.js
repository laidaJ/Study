// 获取微信的access_token
function getAccess() {
    const appid = 'wx8284fb03f1ecf547';
    const appsecret = 'f2694165b521023d7b207b6efe2a265d';

    fetch('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + appsecret)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}

// 
function getJsapi() {
    let url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=' + '75_4u2Hw4PN7HIsAJLaKpSqrmfVtRYCTuTCS38g9aLVG9t8hWyIl4wm_e3Mj_8u66ECWQFqcJP6zjwBuvq7hKfpMONx_ojl0SnHqz_TswjIox9kiDT8RFcrVm7hkdIXGJaABAOXA' + '&type=jsapi';

    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
function getRandom(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}
const nonceStr = console.log(getRandom(16));
const jsapi_ticket = console.log(getJsapi());
