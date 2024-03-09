CREATE DATABASE noteManager

CREATE TABLE classe(id_classe int AUTO_INCREMENT PRIMARY KEY,
                    nom_classe varchar(25))


CREATE TABLE etudiant (
    id_etudiant INT AUTO_INCREMENT PRIMARY KEY,
    nom_etudiant VARCHAR(50),
    prenom_etudiant VARCHAR(50),
    sexe CHAR,
    email VARCHAR(25),
    adresse VARCHAR(25),
    id_classe INT,
    FOREIGN KEY (id_classe) REFERENCES classe(id_classe)
);


CREATE TABLE utilisateur(id int AUTO_INCREMENT PRIMARY key,
                         pseudo varchar(25),
                         mdp varchar(25))

INSERT INTO etudiant (nom_etudiant, prenom_etudiant, sexe, email, adresse, id_classe) VALUES
('Dupont', 'Jean', 'M', 'jean.dupont@example.com', '123 Rue de la Liberté', 1),
('Durand', 'Marie', 'F', 'marie.durand@example.com', '456 Avenue des Fleurs', 2),
('Martin', 'Pierre', 'M', 'pierre.martin@example.com', '789 Boulevard du Soleil', 1),
('Dubois', 'Sophie', 'F', 'sophie.dubois@example.com', '321 Place de la République', 2),
('Lefevre', 'Thomas', 'M', 'thomas.lefevre@example.com', '654 Rue de la Paix', 1),
('Moreau', 'Laura', 'F', 'laura.moreau@example.com', '987 Boulevard des Étoiles', 2),
('Garcia', 'David', 'M', 'david.garcia@example.com', '741 Avenue de la Joie', 1),
('Rodriguez', 'Ana', 'F', 'ana.rodriguez@example.com', '852 Rue du Bonheur', 2),
('Lopez', 'Julien', 'M', 'julien.lopez@example.com', '159 Chemin de la Liberté', 1),
('Sanchez', 'Elena', 'F', 'elena.sanchez@example.com', '753 Avenue de la Victoire', 2);


INSERT INTO utilisateur (pseudo, mdp) VALUES
('utilisateur1', 'motdepasse1'),
('utilisateur2', 'motdepasse2'),
('utilisateur3', 'motdepasse3');