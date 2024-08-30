from flask import Flask, render_template, redirect, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
import pytz
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 280}
db = SQLAlchemy(app)

class MyRecipe(db.Model):
    title = db.Column(db.String(100), nullable=False, primary_key=True)
    ingredients = db.Column(db.String(), nullable=False)
    steps = db.Column(db.String(), nullable=False)
    #password = db.Column(db.String())
    created = db.Column(db.String, default=f"UTC: {datetime.now(pytz.utc).strftime('%H:%M %m/%d/%Y')}")

    def __repr__(self) -> str:
        return f"Recipe {self.title}"

with app.app_context():
    db.create_all()

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        current = request.form['search'].strip()
        existing_recipe = MyRecipe.query.filter_by(title=current).first()
        try:
            if existing_recipe:
                return redirect(url_for("view_recipe", title=current))
            else:
                return redirect(url_for('add_recipe', title=current))
        except Exception as e:
            return f"ERROR: {e}"

    return render_template("index.html")

@app.route("/add", methods=["POST", "GET"])
def add_recipe():
    title = request.args.get('title', '')

    if request.method == "POST":
        title = request.form['title'].strip()
        ingredients = request.form['ingredients']
        steps = request.form['steps']

        existing_recipe = MyRecipe.query.filter_by(title=title).first()
        if existing_recipe:
            return "This recipe already exists."

        new_recipe = MyRecipe(title=title, ingredients=ingredients, steps=steps)

        try:
            db.session.add(new_recipe)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            db.session.rollback()
            return f"ERROR: {e}"
        
    return render_template("add.html", title=title)


@app.route("/<string:title>")
def view_recipe(title: str):
    recipe = MyRecipe.query.filter_by(title=title).first()
    if recipe:
        return render_template("view.html", recipe=recipe)
    else:
        return f"Recipe with title '{title}' not found.", 404

@app.route("/delete/<string:title>")
def delete_recipe(title: str):
    deletion = MyRecipe.query.get_or_404(title)
    try:
        db.session.delete(deletion)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR: {e}"
    
@app.route("/update/<string:title>", methods=["POST", "GET"])
def update_recipe(title: str):
    recipe = MyRecipe.query.get_or_404(title)

    if request.method == "POST":
        try:
            recipe.ingredients = request.form['ingredients']
            recipe.steps = request.form['steps']

            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR: {e}"

    return render_template("update.html", recipe=recipe)

@app.route("/api/items", methods=['GET'])
def get_items():
    recipes = MyRecipe.query.with_entities(MyRecipe.title).all()
    titles = [recipe.title for recipe in recipes]
    return jsonify(titles)

if __name__ == "__main__":
    app.run(debug=True)
