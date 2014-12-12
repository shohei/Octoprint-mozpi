var socket = require('socket.io')();
socket.on('connection', function(socket){});

socket.on('upload', function(data) {

      var fs = require('fs');
      var writeFile = data.file;
      var writePath = './test.jpg';//Σ(ﾟдﾟ) ｴｯ!? 

      var writeStream = fs.createWriteStream(writePath);
      writeStream.on('drain', function () {} )
                        .on('error', function (exception) {
                        //エラー処理
                             console.log("exception:"+exception);
                         }) 
                        .on('close', function () {
                        //(☞三☞三☞՞ਊ՞)☞三☞三☞書き込み完了時の処理
                        })  
                        .on('pipe', function (src) {}); 

      writeStream.write(writeFile,'binary');//バイナリでお願いする
      writeStreamend();
      //✌( ◔౪◔)✌<ここに書き込み終了時の処理はかかないで
}); 

socket.listen(3000);
console.log('ws server at :3000');
