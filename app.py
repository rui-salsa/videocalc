from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')


# ROTA 1: Sua calculadora atual
@app.route('/frames', methods=['POST'])
def calcular_frames():
    frame_rate = int(request.form.get('framerate', 0))
    total_frames = int(request.form.get('totalframes', 0))

    #calculo
    horas = total_frames // (frame_rate * 3600)
    minutos = (total_frames % (frame_rate * 3600)) // (frame_rate * 60)
    segundos = (total_frames % (frame_rate * 60)) // frame_rate
    frames_restantes = total_frames % frame_rate

    resultado = f"TC: {horas:02d}:{minutos:02d}:{segundos:02d}:{frames_restantes:02d}"
    return render_template('index.html', res_frames=resultado)


# ROTA 2: Frames para milissegundos
@app.route('/ms', methods=['POST'])
def calcular_ms():
    fps = int(request.form.get('fps_ms', 0))
    frames = int(request.form.get('frames_ms', 0))

    #calculo
    ms = (frames / fps) * 1000 if fps > 0 else 0

    resultado = f"{ms:.2f} ms"
    return render_template('index.html', res_ms=resultado)

# ROTA 3: TEMPO PARA FRAMES
@app.route('/time', methods=['POST'])
def calcular_time():
    fps2 = int(request.form.get('fps2') or 0)
    horas = int(request.form.get('horas') or 0)
    minutos = int(request.form.get('minutos') or 0)
    segundos = int(request.form.get('segundos') or 0)
    frames2 = int(request.form.get('frames2') or 0)

    # calculo
    conv_horas = (fps2 * 60) * 60
    conv_minu_frame = fps2 * 60
    conv_seg_frame = fps2

    horas_frames = horas * conv_horas
    minutos_frames = minutos * conv_minu_frame
    segundos_frames = segundos * conv_seg_frame
    total = horas_frames + minutos_frames + segundos_frames + frames2

    resultado = f'O teu vídeo tem {total} frames.'
    return render_template('index.html', res_time=resultado)


if __name__ == '__main__':
    app.run(debug=True)