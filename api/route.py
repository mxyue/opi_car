from aiohttp import web
import socketio
from src.domain import joystick

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


@sio.on('connect')
async def connect(sid, environ):
    print("connect ", sid)
    await sio.emit('connected', room=sid, data='1')


@sio.on('joystick')
async def joystick_handle(sid, data):
    print("joystick x> ", data[0], 'y>', data[1])
    print("distance: %d" % joystick.distance(data[0], data[1]))
    if data[0] != 0 and data[1] != 0:
        print("angle: %d" % joystick.angle(data[0], data[1]))


@sio.on('joystick_hold')
async def joystick_hold_handle(sid, data):
    print("joystick hold> ", data)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


def start():
    web.run_app(app, port=8070)
