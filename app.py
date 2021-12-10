from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/printvalues', methods=['POST'])
def printprime():
    values=[]
    i=2 
    while(1):  
      if(Prime(i)):  
        values.append(i) 
          if(len(values)==30): 
            break 
      i+=1 
    return jsonify({'values': f'The first 30 prime numbers are {values}'})
def Prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)  

if __name__=='__main__':
    app.run()
