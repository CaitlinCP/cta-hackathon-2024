"""
The main app for 
"""

from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def get_route_input():

    #TODO: Populate bus lines from dictionary
    bus_lines=['171','172']

    try:
        bus_info = {
            'bus_line': request.form.get['bus_line'],
            'user_address': request.form.get['user_address'],
            'use_location': request.form.get['use_location']
        }

        return redirect("/nearest_stop", bus_info=bus_info)
    
    except:
        redirect(request.url)

    return render_template(
        "route_input.html", bus_lines=bus_lines
    )

@app.route("/nearest_stop", methods=['GET'])
def get_nearest_stop():

    try:
        bus_line=request.args.get('bus_line')
        user_address=request.args.get('user_address')
        use_location=request.args.get('use_location')
    
    except Exception as error:
        return jsonify(
            {
                'code': 400,
                'status': 'error',
                'message': f'an exception occurred: f{error}'
            }
        )
    
    return jsonify({
        'bus_line': bus_line,
        'user_address': user_address,
        'use_location': use_location
    })

    #TODO: Call functions

@app.route("/stop_<stop_id>")
def get_stop_time():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)