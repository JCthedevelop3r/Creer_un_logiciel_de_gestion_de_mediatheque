function updateCreatorField(creatorType) {
        const creatorLabel = document.getElementById('creator-label');

        // Changer le label et le name de selon le type de média
        switch (creatorType) {
            case 'author':
                creatorLabel.innerText = 'Auteur :';
                break;
            case 'artist':
                creatorLabel.innerText = 'Artiste :';
                break;
            case 'creator':
                creatorLabel.innerText = 'Créateur :';
                break;
            case 'director':
                creatorLabel.innerText = 'Réalisateur :';
                break;
        }
}