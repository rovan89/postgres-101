from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
 )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-nased model for the "Album" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId - Column(Integer, primary_key=True)
    Name = Column(String) 

# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, the point to our engine (the data db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session() 

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all record from the "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")