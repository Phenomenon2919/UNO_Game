import socket
import json
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1],int(sys.argv[2])))

rc = s.recv(8192)
points = {"S":20, "T":20, "R":20, "W":50, "F":50}

while (rc!="0\n"):
	if rc != "":
		rc = rc.split("||")
		r_winner = dict() 
		p = list()
		nop = int(rc[0])
		for i in range(1,nop+1):
			p.append(i)
		score = dict()
		nor = int(rc[1])
		cr = -1
		sc = 0
		f = 0
		play_sc = [0] * nop 
		
		for i in range(2,len(rc)-1):
			if rc[i]=='0':
				rw=p.pop()
				play_sc[rw-1] = play_sc[rw-1] + sc
				r_winner[cr] = rw
				sc = 0
				for i in range(1,nop+1):
					p.append(i)
				
				card = dict()
				f = 0
			elif f == 0 and rc[i]!='0':
				cr = rc[i]
				f = 1
			elif len(rc[i])!=1:
				gr = rc[i].split(":")
				player = int(gr[0])
							
				for x in gr[1].split(","):
					if x.isdigit():
						sc = sc + int(x)
					elif x in points.keys():
						sc = sc + points[x]
				p.remove(player)
		
		max = play_sc[0]
		win = list()
		for i in range(len(play_sc)):
			if play_sc[i] > max:
				if len(win) != 0:
					del win[:]
				win.append(i+1)
				max = play_sc[i]
			elif play_sc[i] == max:
				win.append(i+1)
		if len(win) == 1:
			o_winner = win[0]
		else:
			o_winner = win
		
		f_sc = dict()
		for i in range(len(play_sc)):
			f_sc[str(i+1)] = play_sc[i] 
		result = {"round_winners": r_winner, "overall_winner": o_winner, "scores": f_sc}
		message = json.dumps(result)+"\n"
		s.send(message)
		rc = s.recv(8192)
