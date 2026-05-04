from flask import request, render_template, redirect, url_for, flash, jsonify
from models import db, Product

def register_routes(app):

    @app.route("/")
    def index():
        products = Product.query.all()
        return render_template("index.html", products=products)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        if request.method == "POST":
            product = Product(
                name=request.form["name"],
                price=float(request.form["price"]),
                stock=int(request.form["stock"])
            )
            db.session.add(product)
            db.session.commit()
            flash("Producto creado correctamente", "success")
            return redirect(url_for("index"))

        return render_template("create.html")

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit(id):
        product = Product.query.get_or_404(id)

        if request.method == "POST":
            product.name = request.form["name"]
            product.price = float(request.form["price"])
            product.stock = int(request.form["stock"])

            db.session.commit()
            flash("Producto actualizado correctamente", "primary")
            return redirect(url_for("index"))

        return render_template("edit.html", product=product)

    @app.route("/delete/<int:id>", methods=["POST"])
    def delete(id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        flash("Producto eliminado correctamente", "danger")
        return redirect(url_for("index"))

    @app.route("/api/products", methods=["GET"])
    def api_products():
        products = Product.query.all()
        return jsonify([p.to_dict() for p in products])