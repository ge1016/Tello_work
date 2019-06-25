from statemachine import StateMachine, State
import time

class TrafficLightMachine(StateMachine):
	green = State('Green', initial = True)
	yellow = State('Yellow')
	red = State('Red')
	
	cycle = green.to(yellow) | yellow.to(red) | red.to(green)
	
	def on_enter_green(self):
		#self.stop()
		time.sleep(50)

	def on_enter_yellow(self):
		#self.go()
		time.sleep(10)
		
	def on_enter_red(self):
		#self.slowdown()
		time.sleep(30)

	def show(self):
		print("now state: ", self.current_state)
		print("is green: ", self.is_green)
		print("is yellow: ", self.is_yellow)
		print("is red: ", self.is_red)

	
traffic_light = TrafficLightMachine()

print( [s.identifier for s in traffic_light.states] )
print( [t.identifier for t in traffic_light.transitions] )

while True:
	traffic_light.cycle()
	traffic_light.show()