from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, session
import json
import sys
from datetime import datetime
import sqlite3 as sql

node = Flask(__name__)
node.config['SECRET_KEY'] = 'india'
# Using default Flask server-side session isn't needed here as we aren't storing much, 
# but we'll keep the standard session secret key.


@node.route('/')
def  first():
    return  render_template('index.html')

@node.route('/elogin', methods=['POST'])
def  elogin():
    error = None
    if  request.method  ==  'POST':
        username=request.form['username']
        password=request.form['password']
        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "select * from eofficer where username='"+username+"' and password='"+password+"'"
        cur.execute(statement)
        if not cur.fetchone():
            print("Login failed")
            error = 'Invalid username or password. Please try again!'
            return render_template('eoff.html', err=error)
            
        else:
            return  render_template('emenu.html')
            
    return  render_template('eoff.html')


@node.route('/blogin', methods=['POST'])
def  blogin():
    error = None
    if  request.method  ==  'POST':
        username=request.form['username']
        password=request.form['password']
        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "select * from boothofficer where uasername='"+username+"' and password='"+password+"'"
        cur.execute(statement)
        if not cur.fetchone():
            print("Login failed")
            error = 'Invalid username or password. Please try again!'
            return render_template('boff.html', err=error)
            
        else:
            return  render_template('startvote.html')
            
    return  render_template('boff.html')


@node.route('/div2eoff')
def  div2eoff():
    return  render_template('eoff.html')

@node.route('/div2voting')
def  div2voting():
    return  render_template('voting.html')


@node.route('/logout')
def  logout():
    return  render_template('index.html')




@node.route('/div2boff')
def  div2boff():
    return  render_template('boff.html')

@node.route('/div2voter')
def  div2voter():
    return  render_template('newvoter.html')

@node.route('/div2cand')
def  div2cand():
    return  render_template('candidate.html')

@node.route('/div2bak')
def  div2bak():
    return  render_template('emenu.html')

@node.route('/div2Emenu')
def  div2Emenu():
    return  render_template('emenu.html')

@node.route('/div2Bmenu')
def  div2Bmenu():
    return  render_template('startvote.html')


@node.route('/addvoter', methods=['POST'])
def  addvoter():
    print("DEBUG: /addvoter POST request received")
    try:
        # Log all data for debugging
        print("DEBUG: Form keys:", list(request.form.keys()))
        for k, v in request.form.items():
            if k == 'txtIsoTemplate':
                print(f"DEBUG: {k} length: {len(v)}")
            else:
                print(f"DEBUG: {k} = {v}")

        votername = request.form.get('votername')
        voterid = request.form.get('voterid')
        age = request.form.get('age')
        area = request.form.get('area')
        city = request.form.get('city')
        txtIsoTemplate = request.form.get('txtIsoTemplate')
        gender = request.form.get('gender')

        if not all([votername, voterid, age, area, city, txtIsoTemplate, gender]):
            missing = [k for k, v in {
                'votername': votername, 'voterid': voterid, 'age': age, 
                'area': area, 'city': city, 'txtIsoTemplate': txtIsoTemplate, 'gender': gender
            }.items() if not v]
            error_msg = f"Missing fields: {', '.join(missing)}"
            print(f"DEBUG Error: {error_msg}")
            return render_template('newvoter.html', err=error_msg), 400

        if len(txtIsoTemplate) <= 1 and txtIsoTemplate != "MOCK_DATA":
            report = "Finger Not Scanned, Scan and Try again"
            return render_template('newvoter.html', msg=report)

        con = sql.connect("vote.db")
        cur = con.cursor()
        
        # Check if voterid already exists
        cur.execute("SELECT votername FROM voter WHERE voterid=?", (voterid,))
        if cur.fetchone():
            con.close()
            error_msg = f"Voter ID '{voterid}' already exists!"
            print(f"DEBUG Error: {error_msg}")
            return render_template('newvoter.html', err=error_msg)

        records = [(voterid, votername, age, area, city, txtIsoTemplate, "NV", gender)]
        try:
            cur.executemany('INSERT INTO voter VALUES(?,?,?,?,?,?,?,?);', records)
            con.commit()
        except sql.IntegrityError as ie:
            con.close()
            error_msg = f"Database Error: {str(ie)}"
            print(f"DEBUG Error: {error_msg}")
            return render_template('newvoter.html', err=error_msg)
            
        con.close()

        report = "Voter added successfully!"
        return render_template('newvoter.html', msg=report)

    except Exception as e:
        print(f"CRITICAL ERROR in addvoter: {e}")
        import traceback
        traceback.print_exc()
        return f"Internal Server Error: {str(e)}", 500



@node.route('/delVoter', methods=['POST'])
def  delVoter():
    report = None
    if  request.method  ==  'POST':

        con = sql.connect("vote.db")
        cur = con.cursor()

        
        voterid=request.form['voteid']
        
        statement = "delete from voter where voterid='"+voterid+"'"
        cur.execute(statement)

        con.commit()
        report="Voter Deleted"
        # Since we're going to voterlist, we should probably pass data too
        cur.execute("select * from voter")
        data = cur.fetchall()
        con.close()
        return render_template('voterlist.html', data=data, msg=report)
        
    
@node.route('/voterlist')
def  voterlist():

    con = sql.connect("vote.db")
    cur = con.cursor()
    statement = "select * from voter"
    cur.execute(statement)
    data = cur.fetchall()
    con.commit()
    
    return  render_template('voterlist.html',  data  =  data)



@node.route('/searchvoter', methods=['POST'])
def  searchvoter():
    if  request.method  ==  'POST':

        voterid=request.form['voterid']
        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "select * from voter where voterid='"+voterid+"'"
        cur.execute(statement)
        data = cur.fetchall()
        con.commit()
        print(data)

        if len(data)==0:
            report="Voter Not Found"
            return render_template('voting.html', err=report)
        
        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "select * from voter where voterid='"+voterid+"' and status='NV'"
        cur.execute(statement)
        data = cur.fetchall()
        con.commit()

        if len(data)==0:
            report="Already Voted"
            return render_template('voting.html', err=report)
        
        session["voterid"] = voterid
        return render_template('voting.html', code=data[0][5], code2=data[0][1], msg="Voter Authenticated")

        
            

@node.route('/searcheoff', methods=['POST'])
def  searcheoff():
    if  request.method  ==  'POST':

        username=request.form['username']
        password=request.form['password']
        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "select * from eofficer where username='"+username+"' and password='"+password+"'"

        print(statement)
        cur.execute(statement)
        data = cur.fetchall()
        con.commit()
        
        if len(data)==0:
            print("Login failed")
            error = 'Invalid username or password. Please try again!'
            return render_template('eoff.html', err=error)
        
        return render_template('eoff.html', code=data[0][2], msg="Officer Logged In")



@node.route('/searchboff', methods=['POST'])
def  searchboff():
    if  request.method  ==  'POST':

        username=request.form['username']
        password=request.form['password']
        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "select * from boothofficer where uasername='"+username+"' and password='"+password+"'"

        print(statement)
        cur.execute(statement)
        data = cur.fetchall()
        con.commit()
        
        if len(data)==0:
            print("Login failed")
            error = 'Invalid username or password. Please try again!'
            return render_template('boff.html', err=error)
        
        return render_template('boff.html', code=data[0][2], msg="Booth Authenticated")





    
@node.route('/addcandidate', methods=['POST'])
def  addcandidate():
    report = None

    
    if  request.method  ==  'POST':

        
        con = sql.connect("vote.db")
        cur = con.cursor()

        cname=request.form['cname']
        party=request.form['party']
        symbol="../static/images/"+request.form['symbol']

        records = [(cname,party, symbol,0)]

        print(records)
        
        cur.executemany('INSERT INTO Candidate VALUES(?,?,?,?);',records);

        con.commit()
        report="Candidate added"
        return render_template('candidate.html', msg=report)

@node.route('/candlist')
def  candlist():

    con = sql.connect("vote.db")
    cur = con.cursor()
    statement = "select * from candidate"
    cur.execute(statement)
    data = cur.fetchall()

    print(data)
    return  render_template('candlist.html',  data  =  data)


@node.route('/votechart')
def  votechart():

    con = sql.connect("vote.db")
    cur = con.cursor()
    statement = "select * from candidate"
    cur.execute(statement)
    data = cur.fetchall()

    print(data)
    return  render_template('votechart.html',  data  =  data)

@node.route('/result')
def  result():

    con = sql.connect("vote.db")
    cur = con.cursor()
    statement = "select * from candidate"
    cur.execute(statement)
    data = cur.fetchall()

    print(data)
    return  render_template('result.html',  data  =  data)

@node.route('/winner')
def  winner():

    con = sql.connect("vote.db")
    cur = con.cursor()
    
    statement = "SELECT * FROM candidate WHERE votes = (SELECT Max(votes) FROM candidate)" 
    cur.execute(statement)
    data = cur.fetchall()
    print(data)
    report="Winner is "+data[0][0]+" with votes "+str(data[0][3])
    return render_template('emenu.html', msg=report)


@node.route('/resedata')
def  resedata():

    con = sql.connect("vote.db")
    cur = con.cursor()
    
    statement = "update candidate set votes =0"
    cur.execute(statement)
    con.commit()

    statement = "update Voter set status ='NV'"
    cur.execute(statement)
    con.commit()

    return render_template('emenu.html', msg="Data Reset Successful!!")


@node.route('/castvote', methods=['POST'])
def  castvote():
    
    if  request.method  ==  'POST':      
        cname=request.form['cname']
        party=request.form['party']
        report="You Casted Vote for "+cname+"-"+party

        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "update Candidate set votes=votes+1 where Cname='"+cname+"'"
        cur.execute(statement)
        con.commit()

        con = sql.connect("vote.db")
        cur = con.cursor()
        statement = "update Voter set status='V' where voterid='"+session["voterid"]+"'"
        cur.execute(statement)
        con.commit()

        return render_template('voting.html', msg=report)

if __name__== '__main__':

    if len(sys.argv) >= 2:
        port = sys.argv[1]
    else:
        port = 8000

    node.run(host='127.0.0.1', port=port, debug=True)
