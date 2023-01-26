from State import State
from services.getUserData import getUserData
# only one state object is created for the entire application
state = State()

# the state object is passed to the getUserData function and the userData object is updated
getUserData(state)

# many others function are going to be created and they will all have access to the state object

print(state.userData)
