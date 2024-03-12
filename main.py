from flask import Flask, request
import random,string
import hashlib
import secrets
import string
app = Flask(__name__)

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))





@app.route('/login', methods=['GET'])
def login():
    return  """
   
    

   local bs = bitStream.new()
    bs:writeInt8(215);
    bs:writeInt16(2);
    bs:writeInt32(0);
    bs:writeInt32(#'OnAuthorizationStart');
    bs:writeString('OnAuthorizationStart');
    bs:writeInt32(2);
    bs:writeInt8(115);
    bs:writeInt32(#getpassword());
    bs:writeString(getpassword());
    bs:sendPacketEx(1, 9, 0);

    """


@app.route('/hardware', methods=['GET'])
def  hardware():
    genhar = randomword(52)
    combo_str  =  genhar + "71QNzN7t8v"
    sha1_hash = hashlib.sha1(combo_str.encode("utf-8")).hexdigest().upper()
    print(genhar,",",sha1_hash)
    hwstr = ("""
 local hwidarray ={ 
    {"%s","%s"},
}
  	math.randomseed(os.time()); randomhwid = math.random(1, #hwidarray);
	local bs = bitStream.new()
    bs:writeInt8(215)
    bs:writeInt16(1)
    bs:writeInt32(51)
    bs:writeInt8(0)
    bs:writeInt32(#hwidarray[randomhwid][1])
    bs:writeString(hwidarray[randomhwid][1])
	bs:writeInt32(#hwidarray[randomhwid][2])
    bs:writeString(hwidarray[randomhwid][2])
    bs:sendPacketEx(1, 9, 0);

    """ % (genhar,sha1_hash))


    return  hwstr

if __name__ == '__main__':
    app.run()