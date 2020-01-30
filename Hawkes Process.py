•	%matplotlib inline  
•	import numpy as np  
•	import pandas as pd  
•	from matplotlib import pyplot as plt  
•	import heapq  
•	from hawkeslib.model.uv_exp import UnivariateExpHawkesProcess as UVHP  
•	  
•	dfs = pd.read_csv('~/Downloads/average_largest payment_debit.csv') # Debits Timstamps  
•	dfs=dfs.drop('Date',axis=1)  
•	L=[]  
•	for i in range(252):  
•	    L.append(0)  
•	for j in range(252):  
•	    L[j]=[L[j]]  
•	    a=np.mean(dfs.iloc[j,:])  
•	    b=np.std(dfs.iloc[j,:])  
•	    k=len(dfs.iloc[0,:])  
•	    for i in range(k):  
•	        if int(dfs.iloc[j,i])>=(a+2*b):  
•	            L[j].append(i)  
•	for i in range(252):  
•	    L[i].pop(0)  
•	  
•	dfs1 = pd.read_csv('~/Downloads/average_largest payment_credit.csv') # Credits Timstamps  
•	dfs1=dfs1.drop('Date',axis=1)  
•	L1=[]  
•	for i in range(252):  
•	    L1.append(0)  
•	for j in range(252):  
•	    L1[j]=[L1[j]]  
•	    a=np.mean(dfs1.iloc[j,:])  
•	    b=np.std(dfs1.iloc[j,:])  
•	    k=len(dfs1.iloc[0,:])  
•	    for i in range(k):  
•	        if int(dfs1.iloc[j,i])>=(a+2*b):  
•	            L1[j].append(i)  
•	for i in range(252):  
•	    L1[i].pop(0)  
•	  
•	L[119]=L[118]  
•	Mu=[]  
•	Alpha=[]  
•	Theta=[]  
•	for i in range(len(L)):  
•	    proc = UVHP()  
•	    proc.fit(np.float64(L[i]), method="em")  
•	    mu, alpha, theta = proc.get_params()  
•	    Mu.append(mu)  
•	    Alpha.append(alpha)  
•	    Theta.append(theta)  
•	      
•	plt.figure(figsize=(15,2))  
•	plt.ylabel("$\lambda^*(t)$")  
•	plt.xlabel("$day$")  
•	plt.plot(np.arange(0, 252, 1), np.array(Mu)*720, 'b-')  
•	  
•	Mu=[]  
•	Alpha=[]  
•	Theta=[]  
•	for i in range(len(L1)):  
•	    proc = UVHP()  
•	    proc.fit(np.float64(L1[i]), method="em")  
•	    mu, alpha, theta = proc.get_params()  
•	    Mu.append(mu)  
•	    Alpha.append(alpha)  
•	    Theta.append(theta)  
•	      
•	plt.figure(figsize=(15,2))  
•	plt.ylabel("$\lambda^*(t)$")  
•	plt.xlabel("$day$")  
•	plt.plot(np.arange(0, 252, 1), np.array(Mu)*720, 'b-')  
•	  
•	Mu_debit=[]  
•	for i in range(10000):  
•	    Mu=[]  
•	    Alpha=[]  
•	    Theta=[]  
•	    for i in range(len(L)):  
•	        proc = UVHP()  
•	        proc.fit(np.float64(L[i]), method="em")  
•	        mu, alpha, theta = proc.get_params()  
•	        Mu.append(mu)  
•	        Alpha.append(alpha)  
•	        Theta.append(theta)  
•	    Mu_debit.append(np.mean(np.array(Mu)*720))  
•	  
•	Mu_credit=[]  
•	for i in range(10000):  
•	    Mu=[]  
•	    Alpha=[]  
•	    Theta=[]  
•	    for i in range(len(L1)):  
•	        proc = UVHP()  
•	        proc.fit(np.float64(L1[i]), method="em")  
•	        mu, alpha, theta = proc.get_params()  
•	        Mu.append(mu)  
•	        Alpha.append(alpha)  
•	        Theta.append(theta)  
•	    Mu_credit.append(np.mean(np.array(Mu)*720))  
•	  
•	Mu_diff=[]  
•	for i in range(10000):  
•	    Mu_diff.append(Mu_debit[i]-Mu_credit[i])  
•	  
•	plt.title("CHAPS Hawkes Simulations")  
•	plt.ylabel("GBP Billions")  
•	plt.xlabel("Simulated Trading Day")  
•	plt.plot(Mu_diff)  
•	  
•	print("95th percentile: $", heapq.nsmallest(500,Mu_diff)[499], "billions")  
•	print("96th percentile: $", heapq.nsmallest(500,Mu_diff)[399], "billions")  
•	print("97th percentile: $", heapq.nsmallest(500,Mu_diff)[299], "billions")  
•	print("98th percentile: $", heapq.nsmallest(500,Mu_diff)[199], "billions")  
•	print("99th percentile: $", heapq.nsmallest(500,Mu_diff)[99], "billions")  

•	# Target 2  
•	dfs = pd.read_csv('~/Downloads/target2debit.csv',header=None) # Debits Timstamps  
•	L=[]  
•	for i in range(255):  
•	    L.append(0)  
•	for j in range(255):  
•	    L[j]=[L[j]]  
•	    a=np.mean(dfs.iloc[j,:])  
•	    b=np.std(dfs.iloc[j,:])  
•	    k=len(dfs.iloc[0,:])  
•	    for i in range(k):  
•	        if int(dfs.iloc[j,i])>=(a+2*b):  
•	            L[j].append(i)  
•	for i in range(255):  
•	    L[i].pop(0)  
•	  
•	dfs1 = pd.read_csv('~/Downloads/target2credit.csv',header=None) # Credits Timstamps  
•	L1=[]  
•	for i in range(255):  
•	    L1.append(0)  
•	for j in range(255):  
•	    L1[j]=[L1[j]]  
•	    a=np.mean(dfs1.iloc[j,:])  
•	    b=np.std(dfs1.iloc[j,:])  
•	    k=len(dfs1.iloc[0,:])  
•	    for i in range(k):  
•	        if int(dfs1.iloc[j,i])>=(a+2*b):  
•	            L1[j].append(i)  
•	for i in range(255):  
•	    L1[i].pop(0)  
•	  
•	Mu=[]  
•	Alpha=[]  
•	Theta=[]  
•	for i in range(len(L)):  
•	    proc = UVHP()  
•	    proc.fit(np.float64(L[i]), method="em")  
•	    mu, alpha, theta = proc.get_params()  
•	    Mu.append(mu)  
•	    Alpha.append(alpha)  
•	    Theta.append(theta)  
•	      
•	plt.figure(figsize=(15,2))  
•	plt.ylabel("$\lambda^*(t)$")  
•	plt.xlabel("$t$")  
•	plt.plot(np.arange(0, 255, 1), np.array(Mu)*330, 'b-')  
•	  
•	L1[21]=L1[20]  
•	L1[24]=L1[23]  
•	L1[94]=L1[93]  
•	L1[200]=L1[199]  
•	Mu=[]  
•	Alpha=[]  
•	Theta=[]  
•	for i in range(len(L1)):  
•	    proc = UVHP()  
•	    proc.fit(np.float64(L1[i]), method="em")  
•	    mu, alpha, theta = proc.get_params()  
•	    Mu.append(mu)  
•	    Alpha.append(alpha)  
•	    Theta.append(theta)  
•	  
•	plt.figure(figsize=(15,2))  
•	plt.ylabel("$\lambda^*(t)$")  
•	plt.xlabel("$t$")  
•	plt.plot(np.arange(0, 255, 1), np.array(Mu)*330, 'b-')  
•	  
•	Mu_debit=[]  
•	for i in range(10000):  
•	    Mu=[]  
•	    Alpha=[]  
•	    Theta=[]  
•	    for i in range(len(L)):  
•	        proc = UVHP()  
•	        proc.fit(np.float64(L[i]), method="em")  
•	        mu, alpha, theta = proc.get_params()  
•	        Mu.append(mu)  
•	        Alpha.append(alpha)  
•	        Theta.append(theta)  
•	    Mu_debit.append(np.mean(np.array(Mu)*330))  
•	  
•	Mu_credit=[]  
•	for i in range(10000):  
•	    Mu=[]  
•	    Alpha=[]  
•	    Theta=[]  
•	    for i in range(len(L1)):  
•	        proc = UVHP()  
•	        proc.fit(np.float64(L1[i]), method="em")  
•	        mu, alpha, theta = proc.get_params()  
•	        Mu.append(mu)  
•	        Alpha.append(alpha)  
•	        Theta.append(theta)  
•	    Mu_credit.append(np.mean(np.array(Mu)*330))  
•	  
•	Mu_diff=[]  
•	for i in range(10000):  
•	    Mu_diff.append(Mu_debit[i]-Mu_credit[i])  
•	  
•	plt.title("Target 2 Hawkes Simulations")  
•	plt.ylabel("Billions")  
•	plt.xlabel("Simulated Trading Day")  
•	plt.plot(Mu_diff)  
•	  
•	print("95th percentile: $", heapq.nsmallest(500,Mu_diff)[499], "billions")  
•	print("96th percentile: $", heapq.nsmallest(500,Mu_diff)[399], "billions")  
•	print("97th percentile: $", heapq.nsmallest(500,Mu_diff)[299], "billions")  
•	print("98th percentile: $", heapq.nsmallest(500,Mu_diff)[199], "billions")  
•	print("99th percentile: $", heapq.nsmallest(500,Mu_diff)[99], "billions")  
