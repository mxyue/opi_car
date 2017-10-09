from aiohttp import web
import socketio
from src.service import wheel_service

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


@sio.on('connect')
async def connect(sid, environ):
    print("connect ", sid)
    await sio.emit('connected', room=sid, data='1')


@sio.on('joystick')
async def joystick_handle(sid, data):
    angle = data[0]
    power = data[1]
    wheel_service.control(angle, power)


@sio.on('joystick_hold')
async def joystick_hold_handle(sid, data):
    print("joystick hold> ", data)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


def start():
    web.run_app(app, port=8070)
