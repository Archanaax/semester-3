import sim
import sys
import tkinter
print('Program started')
sim.simxFinish(-1) 
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Connected to remoteAPI server')

else:
    print ('Remote API function call returned with error code: ')
_,rm=sim.simxGetObjectHandle(clientID,'RM',sim.simx_opmode_oneshot_wait)
_,lm=sim.simxGetObjectHandle(clientID,'LM',sim.simx_opmode_oneshot_wait)
root=tkinter.Tk()
def onclick(args):
    if args==1:
        sim.simxsetJointTargetvelocity(clientID,rm,2,sim.simx_opmode_streaming)
        sim.simxsetJointTargetvelocity(clientID,lm,2,sim.simx_opmode_streaming)
    if args==2:
        sim.simxSetJointTargetVelocity(clientID,rm,-2,sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(clientID,lm, -2, sim.simx_opmode_streaming)
    if args==3:
        sim.simxSetJointTargetVelocity(clientID, rm, 5, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(clientID, lm, 0, sim.simx_opmode_streaming)
btn1=tkinter.Button(root,text='Front',bg='green',command=lambda:onclick(1))
btn2=tkinter.Button(root,text='back',bg='green',command=lambda:onclick(2))
btn3=tkinter.Button(root,text='Left',bg='green',command=lambda:onclick(3))
btn4=tkinter.Button(root,text='Right',bg='green',command=lambda:onclick(4))
btn5=tkinter.Button(root,text='stop',bg='red',command=lambda:onclick(5))

btn1.pack(side='top')
btn2.pack(side='bottom')
btn3.pack(side='left')
btn4.pack(side='right')
btn5.pack(padx=50,pady=20,side=tkinter.LEFT)
root.mainloop()