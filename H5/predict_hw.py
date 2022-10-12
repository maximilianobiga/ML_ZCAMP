from flask import Flask
from flask import request
from flask import jsonify
import pickle


# # Load the Model (Pickle)
# nombre del modelo
print('importo el modelo')
model_file = 'model2.bin'
dv_file = 'dv.bin'

# abro el modelo y el dict_vectorizer
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)


app = Flask('credit_card')

print("estoy listo para predecir...")


# cliente_dic = {"reports": 0,
#             "share": 0.001694,
#             "expenditure": 0.12,
#             "owner": "yes"}

#cliente = request.get_json(cliente_dic)
# X = dv.transform([cliente_dic])
# X
# y_pred = model.predict_proba(X)[0,1] 
# y_pred
#client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}


@app.route('/predict', methods=['POST'])

# funcion para predecir, de acuerdo al input (cliente), si se da de baja o no

def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1] 
    tarjeta = y_pred >= 0.5
    y_pred

    result = {  'credit_card_aproval_probability': float(y_pred),
                'credit_card_aproval_': bool(tarjeta)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9696)

