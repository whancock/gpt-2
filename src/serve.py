import os
import tensorflow as tf
from flask import Flask, Response, json
from conditional_samples import interact_model

app = Flask(__name__)

@app.route('/')
def api_root():

	out = interact_model('The pie was')

	# return out

	data = {
		'text': out
	}
	
	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')
	return resp


# def load_model(
# 	model_name='124M',
#     models_dir='models'
# ):

# 	models_dir = os.path.expanduser(os.path.expandvars(models_dir))

# 	with tf.Session(graph=tf.Graph()) as sess:
# 		saver = tf.train.Saver()
# 		ckpt = tf.train.latest_checkpoint(os.path.join(model_name, models_dir))
# 		saver.restore(sess, ckpt)




if __name__ == '__main__':
	# load_model()
	app.run()