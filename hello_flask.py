#전제조건:아나콘다가 설치되어있는 것에서만 돌아갈 수 있다.
#D:\Dev\py_projects\[2주차]>touch hello_flask.py
'''[확인]
D:\Dev\py_projects\[2주차]>python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask import Flask
#파이썬 인터프리터환경이 된다.
#이때 flask가 잘되는지를 확인을 한번 해본다.
>>> exit()
'''
from flask import Flask, render_template  #Flask는 대문자!! 
#render=표현한다. template 폴더에 있는 것!(html을 다룰 때)


app=Flask(__name__) #이 파일을 실행하게 된다면 __main__이 들어가게 될것임


#http://www.naver.com/ #.com뒤에있는 /(슬래쉬)는 라우트(루트)라고 한다.
#http://localhost:5000/ #flask의 포트번호는 5000이다.(내컴퓨터에서 시도할때는 localhost로 사용을 해서 쓸수있지만, 나중에 domain을 살때는 그 도메인을 적으면된다.
# 이때 웹서버는 대부분 ":80" 이라는 80번포트를 사용하기때문에 :80을 생략하고 쓴다.
#  즉, http://www.naver.com:80/ 이라고 표현해서 나타낼 수 있다.)




#http://localhost:5000 을 내 컴퓨터에서 쓸예정이다! html을 전송하는 방식으로 web에서 땡겨오겠다.
@app.route("/") #/는 경로(라우트,루트)를 의미
                #@(골뱅이)는 데코레이터(전처리)과정을 하는 역할을 한다.
#브라우저에 /가 오게되면 def index()를 하면되고
def index(): #@로 특정한 url을 호출하는데 여기 바로 밑에있는 def index()를 호출하게 된다.
    return "hello flask!" #그렇기에 return된 것이 여기서 보여지게 되는 것이다.

"""[cmd 결과]
D:\Dev\py_projects\[2주차]>python hello_flask.py
 * Serving Flask app "hello_flask" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 """

'''[web 결과]
 여기서 나온 것을 이용해서 브라우저에서 링크를 입력하는 부분에
 http://127.0.0.1:5000/ 를 넣어주면,
 hello flask!라고 창에 등록이 된것을 확인할 수 있게된다.
'''

'''[web 결과]
여기서 나온것을 이용해서 브라우저에서 링크를 입력하는 부분에
http://127.0.0.1:5000/abc 를 넣어주면,
abc페이지입니다.라는 것을 확인할 수 있다.
'''

'''
ctrl+c를 누르면 이것이 연결되는 것을 끊어서
다시 브라우저에 
http://127.0.0.1:5000/
http://127.0.0.1:5000/abc
를 넣어도 작동이 안됨을 확인할 수 있게된다.
'''


#http://localhost:5000/hello
@app.route("/hello")
#브라우저에 /abc가 오게되면 def abc()를 실행하면된다.
def abc(): #def의 이름(ex_abc)이 중요한것이 아니라 그냥 @바로 아래 있는 것을 이용하는 것이 포인트.
    return render_template("hello.html") #templates에 있는 hello.html이라는 것을 보여주도록 만든다.
#결국 내가 만들부분은 def부분에서 무엇을 넣으면될지만 고민하면된다. 조립식으로 이것이 들어간다고 생각하면된다!
'''[web결과]
Hello world
#hello.html의 body부분에 있는 것이 뿌려지게된다.
'''


if __name__=="__main__": #자기 자신의 폴더에서 이를 실행할때는 아래를 실행해라.
    app.run(debug=True) #내소스를 고치고 저장하면 자동 리스타트와 에러 메제지를 자세히 표현하는 역할을 하게 된다. * Debug mode: off
    #app.run() #app에 있는 객체를 실행하여라. * Debug mode: off

'''[주의]
현재 cmd창에 이것이 떠있는데, 또 다른 것을 쓰면 안됨!
'''