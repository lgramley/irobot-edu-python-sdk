from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3
from irobot_edu_sdk.music import Note
import asyncio

# robot = Root(Bluetooth())
robot = Create3(Bluetooth())
speed = robot.MAX_SPEED

#TO RUN: just run the file!!
#to check the battery: run file 27_robot_info.py

@event(robot.when_bumped, [True, True]) #should trigger when either side is bumped
async def pull_catapult(robot):
    print("moving!!")
    print("triggering catapult!!!! :) :) :) :) :) :)")
    await robot.set_lights_on_rgb(0, 255, 0)
    await robot.set_wheel_speeds(speed, speed)
    await robot.move(25)
robot.play()

# jingle_bells = [
#     (659, 0.25), (659, 0.25), (659, .5),   # E E E
#     (659, 0.25), (659, 0.25), (659, .5),   # E E E
#     (659, 0.25), (783, 0.25), (523, 0.25), (587, 0.25), (659, .75),  # E G C D E
#     (698, 0.25), (698, 0.25), (698, 0.25), (698, 0.25),             # F F F F
#     (698, 0.25), (659, 0.25), (659, 0.25), (659, 0.25),             # F E E E
#     (659, 0.25), (587, 0.25), (587, 0.25), (659, 0.25), (587, 0.25), # E D D E D
#     (783, .5),                                                  # G
# ]

# Play the melody
# @event(robot.when_bumped, [True, True])
# async def play_jingle_bells(robot):
#     for note, duration in jingle_bells:
#         await robot.play_note(note, duration*.5)
#         await asyncio.sleep(duration * 0.0001)  # Short pause between notes

# @event(robot.when_bumped, [True, True])
# async def dif_func(robot):
#     print("look at me doing 2 things at once")
# Call the function with your robot instance
# await play_jingle_bells(robot)
# robot.play()