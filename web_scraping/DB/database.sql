-- Tworzenie tabeli artykułów
CREATE TABLE Artykuly (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tytul VARCHAR(100),
    tresc TEXT
);

-- Tworzenie tabeli streszczeń artykułów
CREATE TABLE Streszczenia (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_artykulu INT,
    streszczenie TEXT,
    FOREIGN KEY (id_artykulu) REFERENCES Artykuly(id)
);
