from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment

db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500), nullable=False)
    website_link = db.Column(db.String(120))
    searching_talent = db.Column(db.Boolean, default=False)
    search_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue', lazy=False)

    def __repr__(self):
        f'<Venue venue_id: {self.id} venue_name: {self.name} venue_city: {self.city} venue_state: {self.state} venue_address: {self.address} venue_phone: {self.phone} venue_facebook: {self.facebook_link} venue_image: {self.image_link} venue_website: {self.website_link} venue_searching: {self.searching_talent} venue_description: {self.search_description} shows: {self.shows}>'


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    searching_venues = db.Column(db.Boolean, default=False)
    search_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy=False)

    def __repr__(self):
        f'<Artist artist_id: {self.id} artist_name: {self.name} artist_city: {self.city} artist_state: {self.state} artist_phone: {self.phone} artist_genres: {self.genres} artist_facebook: {self.facebook_link} artist_image: {self.image_link} artist_website: {self.website_link} artist_searching: {self.searching_venues} artist_description: {self.search_description} shows: {self.shows}>'


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey(
        'venue.id'), nullable=False)

    def __repr__(self):
        f'<Show show_id: {self.id} show_date: {self.date} show_artist_id: {self.artist_id} show_venue_id: {self.venue_id}>'
