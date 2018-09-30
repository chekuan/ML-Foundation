import numpy as np
import json


with open('imdb_word_index.json') as f:
    word_data = json.load(f)
    word_frequent_sorted = sorted(word_data.items(), key=lambda kv: kv[1])

x_train_array = np.load('./imdb/x_train.npy')
y_train_array = np.load('./imdb/y_train.npy')

data_positive = np.count_nonzero(y_train_array==1)
data_negative = np.count_nonzero(y_train_array==0)


### Top 100 Frequent Words
word_100 = []
for i in range(100):
	word_100.append(word_frequent_sorted[i][0])

word_data_table = dict()
for i in range(len(x_train_array)):
	for j in set(x_train_array[i]):
		if j <= 100:
			if j not in word_data_table:
				word_data_table[j] = [0,0]
			if y_train_array[i]==1:
				word_data_table[j][0]+=1
			elif y_train_array[i]==0:
				word_data_table[j][1]+=1
#print(word_data_table)

likelihood_table = dict()
for i in range(1,101):
	positive = float(word_data_table[i][0])/float(data_positive)
	negative = float(word_data_table[i][1])/float(data_negative)
	likelihood_table[i] = [positive, negative]
	#print(positive,negative)
#print(likelihood_table)

x_test = np.load('./imdb/x_test.npy')
predict_ans = []
for comment in x_test:
	prob_positive = 0.5
	prob_negative = 0.5
	for word_index in comment:
		if word_index<=100:
			prob_positive += likelihood_table[word_index][0]
			prob_negative += likelihood_table[word_index][1]

	if prob_positive>prob_negative:
		predict_ans.append(1)
	else:
		predict_ans.append(0)

y_test = list(np.load('./imdb/y_test.npy'))

correct = 0
TP = 0
TN = 0
for i in range(len(y_test)):
	if predict_ans[i]==y_test[i]:
		correct+=1
		if predict_ans[i]==1:
			TP+=1
		elif predict_ans[i]==0:
			TN+=1

FN = y_test.count(1)-TP
FP = y_test.count(0)-TN

accuracy = float(correct)/float(len(y_test))
precision = float(TP)/float(TP+FP)
recall = float(TP)/float(TP+FN)

f = open('report.txt','w')

f.write("<Top100>\n")
f.write("accuracy: "+str(accuracy)+"\n")
f.write("precision: "+str(precision)+"\n")
f.write("recall: "+str(recall)+"\n")
f.write("\n\n")


### Top 1000

word_1000 = []
for i in range(1000):
	word_1000.append(word_frequent_sorted[i][0])

word_data_table = dict()
for i in range(len(x_train_array)):
	for j in set(x_train_array[i]):
		if j <= 1000:
			if j not in word_data_table:
				word_data_table[j] = [0,0]
			if y_train_array[i]==1:
				word_data_table[j][0]+=1
			elif y_train_array[i]==0:
				word_data_table[j][1]+=1

likelihood_table = dict()
for i in range(1,1001):
	positive = float(word_data_table[i][0])/float(data_positive)
	negative = float(word_data_table[i][1])/float(data_negative)
	likelihood_table[i] = [positive, negative]


x_test = np.load('./imdb/x_test.npy')
predict_ans = []
for comment in x_test:
	prob_positive = 0.5
	prob_negative = 0.5
	for word_index in comment:
		if word_index<=1000:
			prob_positive += likelihood_table[word_index][0]
			prob_negative += likelihood_table[word_index][1]

	if prob_positive>prob_negative:
		predict_ans.append(1)
	else:
		predict_ans.append(0)

correct = 0
TP = 0
TN = 0
for i in range(len(y_test)):
	if predict_ans[i]==y_test[i]:
		correct+=1
		if predict_ans[i]==1:
			TP+=1
		elif predict_ans[i]==0:
			TN+=1

FN = y_test.count(1)-TP
FP = y_test.count(0)-TN

accuracy = float(correct)/float(len(y_test))
precision = float(TP)/float(TP+FP)
recall = float(TP)/float(TP+FN)

f.write("<Top1000>\n")
f.write("accuracy: "+str(accuracy)+"\n")
f.write("precision: "+str(precision)+"\n")
f.write("recall: "+str(recall)+"\n")
f.write("\n\n")


### Top 10000

word_10000 = []
for i in range(10000):
	word_1000.append(word_frequent_sorted[i][0])

word_data_table = dict()
for i in range(len(x_train_array)):
	for j in set(x_train_array[i]):
		if j <= 10000:
			if j not in word_data_table:
				word_data_table[j] = [0,0]
			if y_train_array[i]==1:
				word_data_table[j][0]+=1
			elif y_train_array[i]==0:
				word_data_table[j][1]+=1

likelihood_table = dict()
for i in range(1,10001):
	positive = float(word_data_table[i][0])/float(data_positive)
	negative = float(word_data_table[i][1])/float(data_negative)
	likelihood_table[i] = [positive, negative]
	

x_test = np.load('./imdb/x_test.npy')
predict_ans = []
for comment in x_test:
	prob_positive = 0.5
	prob_negative = 0.5
	for word_index in comment:
		if word_index<=10000:
			prob_positive += likelihood_table[word_index][0]
			prob_negative += likelihood_table[word_index][1]

	if prob_positive>prob_negative:
		predict_ans.append(1)
	else:
		predict_ans.append(0)

correct = 0
TP = 0
TN = 0
for i in range(len(y_test)):
	if predict_ans[i]==y_test[i]:
		correct+=1
		if predict_ans[i]==1:
			TP+=1
		elif predict_ans[i]==0:
			TN+=1

FN = y_test.count(1)-TP
FP = y_test.count(0)-TN

accuracy = float(correct)/float(len(y_test))
precision = float(TP)/float(TP+FP)
recall = float(TP)/float(TP+FN)

f.write("<Top10000>\n")
f.write("accuracy: "+str(accuracy)+"\n")
f.write("precision: "+str(precision)+"\n")
f.write("recall: "+str(recall)+"\n")
f.write("\n\n")
