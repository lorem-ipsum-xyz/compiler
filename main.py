from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def Bogart():
  return render_template('index.html'),200

@app.route('/api/compiler', methods=['POST'])
def compiler():
  data = request.json
  lang = data.get('lang')
  code = data.get('program')
  Input = data.get("input")
  res = requests.post('https://rextester.com/rundotnet/Run', data={"LanguageChoiceWrapper": int(lang),"EditorChoiceWrapper":3,"LayoutChoiceWrapper":1,"Program":code,"Input": Input,"Privacy":'',"PrivacyUsers":'',"Title":'',"SavedOutput":'',"WholeError":'',"WholeWarning":'',"StatsToSave=":'',"odeGuid":'',"IsInEditMode":False,"IsLive": False}).json()
  return jsonify(res)

if __name__ == '__main__':
  app.run()