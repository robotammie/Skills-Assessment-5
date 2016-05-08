"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter(Model.name=="Corvette", Model.brand_name=="Chevrolet").all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Brand.name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model.name,
                              Model.brand_name,
                              Brand.headquarters
                              ).filter(Model.year == year
                              ).all()

    for model in models:
        name, brand, hq = model
        print "%s \t%s\t%s\n" % (name, brand, headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
    using only ONE database query.'''

    models = db.session.query(Brand.name, Model.name).all()

    for model in models:
        brand, model = model
        print "%s \t%s\n" % (brand, model)


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# The above expression returns a query object. In order to actually query
# the database, you would have to add .all(), .one(), .first(), or .count().

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association talbe is a table whose only purpose is to bind two other tables
# together. It is used in situations where there is a "many to many" relationship.
# The assiciation table manages this by binding itself in a "many to one"
# relationship to both tables.
# For instance, one movie may have many actors in it, and one actor might be in
# many movies. Rather than try to link movies and actors together directly, you
# would insert an association table between them, with each line in the new table
# corresponding to one connection between movie and actor (Tom Hanks, Saving
# Private Ryan; Tom Hanks, Big; Matt Damon, Saving Private Ryan)

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Returns a list of brand objects where the brand name is or contains the
    given string"""

    brands = Brand.query.filter(Brand.name.like("%"+mystr+"%")).all()

    return brands


def get_models_between(start_year, end_year):
    """Finds all models introduced between any two years."""

    models = Model.query.filter(Model.year >= start_year,
                                Model.year < end_year).all()

    return models
