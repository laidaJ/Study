let url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=75_4u2Hw4PN7HIsAJLaKpSqrmfVtRYCTuTCS38g9aLVG9t8hWyIl4wm_e3Mj_8u66ECWQFqcJP6zjwBuvq7hKfpMONx_ojl0SnHqz_TswjIox9kiDT8RFcrVm7hkdIXGJaABAOXA&type=jsapi';

fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });