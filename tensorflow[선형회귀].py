import tensorflow as tf
#텐서플로우를 불러오고 tf로 줄여서 쓴다

xData = []
yData = []
#x y 값을 담는다

w = tf.Variable(tf.random_uniform([1],-100.100)
#랜덤한 출발 점 하나를 찍는다
b = tf.Variable(tf.random_uniform([1],-100,100)
#랜덤한 출발 점 하나를 찍는다
X = tf.placeholder(tf.float32)
#x값을 placeholder로 설정해준다
Y = tf.placeholder(tf.float32)
#x값을 placeholder로 설정해준다

H = w * X + b
#전체식을 정의해준다
cost = tf.reduce_mean(tf.square(H - Y))
#비용함수를 정의해준다
a = tf.Variable(0.01)
#한번 훈련할때 수정을 얼마나 할지 정해준다
optimizer = tf.train.GradientDescentOptimizer(a)
#미분으로 다가가는 객체를 준다
train = optimizer.minimize(cost)
#비용함수으로 계산할때 최소가 되는 값을 찾는다

init = tf.global_variables_initializer()
#변수를 모두 초기화하는 함수를 만든다
sess = tf.Session()
#세션값을 준다
sess.run(init)
#변수를 모두 초기화한다
for i in range(5001):
    sess.run(train, feed_dict={X : xData, Y : yData})
	#훈련을 시작한다
    if i % 500 == 0 :
        print (i, sess.run(cost, feed_dict={X : xData, Y : yData}), sess.run(w), sess.run(b))
		#(훈련횟수, feed_dict, 현재 w, 현재 b)를 500번마다 출력한다
print (sess.run(H, feed_dict={X: [8]}))    
#x가 8일때 예상 결과를 출력한다