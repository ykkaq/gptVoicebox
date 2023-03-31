import pyaudio
import wave

# 録音する時間（秒）
RECORD_SECONDS = 5

# 録音するファイル名
WAVE_OUTPUT_FILENAME = "output.wav"

# 録音するファイルの設定
CHUNK = 1024  # フレームのサイズ
FORMAT = pyaudio.paInt16  # フォーマット
CHANNELS = 1  # チャンネル数（モノラル）
RATE = 44100  # サンプルレート（Hz）

# PyAudioのインスタンスを作成する
p = pyaudio.PyAudio()

# マイクからのストリームを開始する
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording...")

# 録音データを格納するバッファを作成する
frames = []

# 録音する
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# マイクからのストリームを停止する
stream.stop_stream()
stream.close()
p.terminate()

# 録音データをファイルに保存する
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
