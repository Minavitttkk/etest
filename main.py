from flask import Flask, request
import random,string
import hashlib
import secrets
import string
app = Flask(__name__)

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


@app.route('/reg', methods=['GET'])
def reg():
    return  """
    local bytes ={ 215, 2, 0, 0, 0, 0, 0, 18, 0, 0, 0, 79, 110, 82, 101, 103, 105, 115, 116, 114, 97, 116, 105, 111, 110, 68, 97, 116, 97, 4, 0, 0, 0, 115, 16, 0, 0, 0, math.random(97,122), math.random(97,122), math.random(97,122), math.random(97,122), math.random(97,122), math.random(97,122), 64, math.random(97,122), 109, math.random(97,122), 105, 108, 46, math.random(97,122), 111, 109, 115, string.len(getpassword()), 0, 0, 0,}
    	for i = 0,tonumber(string.len(getpassword())) do 
     		local tempis = i;
 			local isbite = string.byte(getpassword(),tempis)
			table.insert(bytes,isbite)
    	end 
	local str = table.concat(bytes, ",")
	sendTable(bytes)
    """


@app.route('/login', methods=['GET'])
def login():
    return  """
   local bs = bitStream.new()
    bs:writeInt8(215)
    bs:writeInt16(2)
    bs:writeInt32(0)
    bs:writeInt32(#'OnAuthorizationStart')
    bs:writeString('OnAuthorizationStart')
    bs:writeInt32(2)
    bs:writeInt8(115)
    bs:writeInt32(#getpassword())
    bs:writeString(getpassword())
    bs:sendPacketEx(1, 9, 0)
    """


@app.route('/hardware', methods=['GET'])
def  hardware():
    rint_ = random.randint(7,200)
    genhar = randomword(rint_)
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