#Performed tasks on .csv file
f=open('Infosys.csv','r+')
arr2=[]
c=0
gain=0
loss=0
avg_gain=0
avg_loss=0
for x in f:
	#print(x)
	str1=""
	arr=x.split(',')
	#print(arr)
	if(arr[0]=="Date"):
		c+=1
		continue
	op=float(arr[2])
	cl=float(arr[5])
	diff=round(op-cl,3)
	arr[8]=diff
	if(diff>0):
		arr[9]=diff
		arr[10]=0
		if(c<=14):
			gain+=diff

	elif(diff<0):
		arr[9]=0
		arr[10]=-diff
		if(c<=14):
			loss+=diff
	
	if(c==15):
		avg_gain=gain/14
		avg_loss=abs(loss/14)
		arr[11]=round(avg_gain,2)
		arr[12]=round(avg_loss,2)
		rs=abs(avg_gain/avg_loss)
		rsi=round((100-(100/(1+rs))),2)
		arr[13]=rsi
		#str1+="\n"

	elif(c>15):
		if(diff>0):
			avg_gain=(avg_gain*13+diff)/14
			avg_loss=(avg_loss*13)/14
			str1+="\n"

		elif(diff<0):
			avg_loss=(avg_loss*13-diff)/14
			avg_gain=(avg_gain*13)/14
			str1+="\n"

		arr[11]=round(avg_gain,2)
		arr[12]=round(avg_loss,2)
		rs=abs(avg_gain/avg_loss)
		rsi=round((100-(100/(1+rs))),2)
		arr[13]=rsi

	for x in arr:
		str1=str1+str(x)+","
	str1=str1[:-1]
	arr2.append(str1)
	c+=1
f.truncate(0)
f.write('Date,Time,Open,High,Low,Close,Quantity,Average,Open – Close,Gain,Loss,Avg Gain,Avg Loss,RSI\n')
for x in arr2:
 	f.write(x)
f.close()