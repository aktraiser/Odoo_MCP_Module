#!/bin/bash

# Script de démarrage pour le module Odoo V18
echo "🚀 Démarrage de l'environnement de développement Odoo V18"

# Vérifier si Docker est installé
if ! command -v docker &> /dev/null; then
    echo "❌ Docker n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si Docker Compose est installé
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Arrêter les conteneurs existants
echo "🛑 Arrêt des conteneurs existants..."
docker-compose down

# Démarrer les services
echo "🔄 Démarrage des services..."
docker-compose up -d

# Attendre que les services soient prêts
echo "⏳ Attente du démarrage des services..."
sleep 10

# Vérifier le statut
echo "📊 Statut des services :"
docker-compose ps

echo ""
echo "✅ Environnement prêt !"
echo "🌐 Odoo est accessible sur : http://localhost:8069"
echo "📊 Base de données PostgreSQL sur : localhost:5432"
echo ""
echo "📋 Informations de connexion :"
echo "   - Base de données : odoo"
echo "   - Utilisateur : admin"
echo "   - Mot de passe : admin"
echo ""
echo "🔧 Commandes utiles :"
echo "   - Voir les logs : docker-compose logs -f odoo"
echo "   - Arrêter : docker-compose down"
echo "   - Redémarrer : docker-compose restart"
echo ""
echo "📚 Le module 'Mon Module Simple' sera installé automatiquement" 