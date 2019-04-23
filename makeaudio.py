import numpy as np
import wave, struct

wf = wave.open('sinwave4input.wave', 'w')
wf.setnchannels( 1 ) # モノラル
wf.setsampwidth( 2 ) # 量子化 2byte=16bit
wf.setframerate(  44100 ) # サンプリング=44.1 kサンプル/s
n = 180 * 44100  # データ数 = 時間（s）× サンプル/s
t = np.linspace(0, 180, n)
y = pow(2, 15) * np.sin( 2 * np.pi * 1000 * t ) / 2 # 1k Hz)
wf.writeframes( struct.pack("h" * n, *y.astype(np.int16)) )
wf.close()

